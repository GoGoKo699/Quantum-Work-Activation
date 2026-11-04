#!/usr/bin/env python3
"""Exact-multiplicity spectral sorting for a product of passive qutrits.

The finite-dimensional minimization over all unitaries is solved by assigning
the decreasing eigenvalues of rho**tensor(n) to increasing energies.  This
program performs precisely that assignment, retaining multinomial
multiplicities as arbitrary-precision integers.  It never enumerates 3**n
microstates in the main algorithm.

The supported spectra are (0, 1, alpha), with alpha a rational number supplied
as a decimal/fraction string, or alpha=(1+sqrt(5))/2 supplied as "golden".
Beta and delta are exact rational input strings.  Rational sorting keys are
integers.  For the golden spectrum, a floating sort is followed by an exact
integer check of every adjacent quadratic-algebraic key; an uncertified order
raises an error rather than silently producing a result.

Multiplicities and ordering are exact.  Probabilities and mean work are
numerical: type probabilities use normalized, mode-centered long-double
binomial recurrences, and signed energy changes are accumulated with fsum.
The asymptotic work normalization is evaluated with 70-digit Decimal arithmetic.
The independent tiny-system check enumerates microstates with Decimal.

Dependencies: Python >=3.11, numpy.  No SciPy or arbitrary-precision package.
"""

from __future__ import annotations

import argparse
import csv
import itertools
import json
import math
import platform
import sys
import time
from dataclasses import dataclass
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path

import numpy as np


DPS = 70


@dataclass(frozen=True)
class Model:
    alpha: str
    beta: str = "1"
    delta: str = "0.1"

    @property
    def golden(self) -> bool:
        return self.alpha == "golden"

    @property
    def rational_alpha(self) -> Fraction:
        if self.golden:
            raise ValueError("The golden spectrum is irrational.")
        return Fraction(self.alpha)

    def decimal_values(self):
        alpha = (1 + Decimal(5).sqrt()) / 2 if self.golden else decimal_fraction(self.rational_alpha)
        return alpha, decimal_fraction(Fraction(self.beta)), decimal_fraction(Fraction(self.delta))

    def validate(self) -> None:
        with localcontext() as context:
            context.prec = DPS
            alpha, beta, delta = self.decimal_values()
            if alpha <= 1 or beta <= 0 or delta < 0:
                raise ValueError("Require alpha>1, beta>0, delta>=0.")
            if delta > beta * (alpha - 1):
                raise ValueError("The requested single-copy state is not passive.")


def decimal_fraction(value: Fraction):
    return Decimal(value.numerator) / value.denominator


def thermodynamic_data(model: Model) -> dict:
    """Compute p, the equal-entropy Gibbs temperature, and w_infinity."""
    model.validate()
    with localcontext() as context:
        context.prec = DPS
        alpha, beta, delta = model.decimal_values()
        energies = (Decimal(0), Decimal(1), alpha)
        weights = (Decimal(1), (-beta).exp(), (-beta * alpha + delta).exp())
        z = sum(weights)
        p = tuple(w / z for w in weights)
        entropy = -sum(x * x.ln() for x in p)

        def gibbs(b):
            weights_b = tuple((-b * e).exp() for e in energies)
            z_b = sum(weights_b)
            return tuple(w / z_b for w in weights_b)

        def entropy_at(b):
            g = gibbs(b)
            return -sum(x * x.ln() for x in g)

        if delta == 0:
            beta_star, g, winf = beta, p, Decimal(0)
        else:
            lo, hi = Decimal(0), max(Decimal(1), 2 * beta)
            while entropy_at(hi) > entropy:
                hi *= 2
            # Bisection avoids a poorly conditioned derivative at beta=0.
            for _ in range(260):
                middle = (lo + hi) / 2
                if entropy_at(middle) > entropy:
                    lo = middle
                else:
                    hi = middle
            beta_star = (lo + hi) / 2
            g = gibbs(beta_star)
            # Equal entropy gives this nonnegative relative-entropy formula.
            relative_entropy = sum(p_i * (p_i / g_i).ln() for p_i, g_i in zip(p, g))
            winf = relative_entropy / beta_star
        return {
            "alpha_value": float(alpha),
            "beta_star": float(beta_star),
            "probabilities": [float(x) for x in p],
            "probabilities_decimal": [str(x) for x in p],
            "entropy": float(entropy),
            "single_copy_energy": float(sum(p_i * e for p_i, e in zip(p, energies))),
            "asymptotic_work_per_copy": float(winf),
            "asymptotic_work_decimal": str(winf),
        }


def binomial_probabilities(n: int, p: np.longdouble) -> np.ndarray:
    """Normalized recurrence about the mode; never exponentiate n log(p)."""
    result = np.zeros(n + 1, dtype=np.longdouble)
    if p == 0:
        result[0] = 1
        return result
    if p == 1:
        result[n] = 1
        return result
    mode = min(n, int(np.floor((n + 1) * p)))
    result[mode] = 1
    odds = p / (1 - p)
    for k in range(mode, n):
        result[k + 1] = result[k] * (n - k) * odds / (k + 1)
    for k in range(mode, 0, -1):
        result[k - 1] = result[k] * k / ((n - k + 1) * odds)
    result /= np.sum(result, dtype=np.longdouble)
    return result


def enumerate_types(n: int, thermodynamics: dict):
    number = (n + 1) * (n + 2) // 2
    k1 = np.empty(number, dtype=np.int32)
    k2 = np.empty(number, dtype=np.int32)
    masses = np.empty(number, dtype=np.longdouble)
    multiplicities = [0] * number
    p = [np.longdouble(x) for x in thermodynamics["probabilities_decimal"]]
    level_two = binomial_probabilities(n, p[2])
    conditional_one = p[1] / (p[0] + p[1])
    index, choose_two = 0, 1
    for b in range(n + 1):
        remaining = n - b
        row = binomial_probabilities(remaining, conditional_one)
        stop = index + remaining + 1
        k1[index:stop] = np.arange(remaining + 1, dtype=np.int32)
        k2[index:stop] = b
        masses[index:stop] = level_two[b] * row
        multiplicity = choose_two
        for a in range(remaining + 1):
            multiplicities[index + a] = multiplicity
            if a < remaining:
                multiplicity = multiplicity * (remaining - a) // (a + 1)
        index = stop
        if b < n:
            choose_two = choose_two * (n - b) // (b + 1)
    if sum(multiplicities) != 3**n:
        raise AssertionError("The exact type multiplicities do not sum to 3**n.")
    return k1, k2, masses, multiplicities


def quadratic_sign(a: int, b: int) -> int:
    """Exact sign of a+b*sqrt(5), for integers a,b."""
    if b == 0:
        return (a > 0) - (a < 0)
    if a == 0:
        return (b > 0) - (b < 0)
    if a > 0 and b > 0:
        return 1
    if a < 0 and b < 0:
        return -1
    difference = a * a - 5 * b * b
    return ((difference > 0) - (difference < 0)) * (1 if a > 0 else -1)


def exact_integer_keys(k1, k2, slope: Fraction):
    bound = int(k1.max()) * (abs(slope.numerator) + slope.denominator)
    if bound < np.iinfo(np.int64).max:
        return slope.denominator * k1.astype(np.int64) + slope.numerator * k2.astype(np.int64)
    # Unusual input denominators retain exactness without an int64 overflow.
    return np.array(
        [slope.denominator * int(a) + slope.numerator * int(b) for a, b in zip(k1, k2)],
        dtype=object,
    )


def certify_golden_order(order, k1, k2, offset: Fraction) -> None:
    """Certify ascending k1+(golden-offset)*k2 by exact integer arithmetic."""
    numerator, denominator = offset.numerator, offset.denominator
    previous = int(order[0])
    for item in order[1:]:
        current = int(item)
        da = int(k1[current]) - int(k1[previous])
        db = int(k2[current]) - int(k2[previous])
        a = 2 * denominator * da + (denominator - 2 * numerator) * db
        b = denominator * db
        if quadratic_sign(a, b) < 0:
            raise ArithmeticError("Floating sorting failed the exact quadratic order certificate.")
        previous = current


def spectral_orders(model: Model, k1, k2):
    offset = Fraction(model.delta) / Fraction(model.beta)
    if not model.golden:
        target_key = exact_integer_keys(k1, k2, model.rational_alpha)
        source_key = exact_integer_keys(k1, k2, model.rational_alpha - offset)
        target = np.argsort(target_key, kind="stable")
        # Energy breaks exact probability ties without changing the optimum.
        source = np.lexsort((target_key, source_key))
        return source, target, "exact integer rational keys"
    alpha = (1 + math.sqrt(5)) / 2
    target = np.argsort(k1 + alpha * k2, kind="stable")
    source = np.argsort(k1 + (alpha - float(offset)) * k2, kind="stable")
    certify_golden_order(target, k1, k2, Fraction(0))
    certify_golden_order(source, k1, k2, offset)
    return source, target, "every adjacent quadratic key checked with exact integers"


def energy_difference(model: Model, da: int, db: int) -> float:
    if not model.golden:
        alpha = model.rational_alpha
        return (alpha.denominator * da + alpha.numerator * db) / alpha.denominator
    a, b = 2 * da + db, db
    root_five = math.sqrt(5)
    if a * b < 0:
        # Rationalization avoids cancellation for a small nonzero energy gap.
        return (a * a - 5 * b * b) / (2 * (a - b * root_five))
    return (a + b * root_five) / 2


def full_work(n: int, model: Model, thermodynamics: dict | None = None) -> dict:
    if n < 1:
        raise ValueError("n must be positive.")
    start = time.perf_counter()
    thermo = thermodynamics or thermodynamic_data(model)
    k1, k2, masses, multiplicities = enumerate_types(n, thermo)
    source, target, certificate = spectral_orders(model, k1, k2)
    i = j = 0
    source_index, target_index = int(source[0]), int(target[0])
    source_left = multiplicities[source_index]
    target_left = multiplicities[target_index]
    terms = []
    transported_mass_terms = []
    number = len(source)
    while i < number:
        take = min(source_left, target_left)
        # Python's arbitrary-integer division computes the bounded ratio without
        # converting either huge multiplicity to a potentially overflowing float.
        fraction = take / multiplicities[source_index]
        mass = float(masses[source_index] * fraction)
        da = int(k1[source_index]) - int(k1[target_index])
        db = int(k2[source_index]) - int(k2[target_index])
        terms.append(mass * energy_difference(model, da, db))
        transported_mass_terms.append(mass)
        source_left -= take
        target_left -= take
        if source_left == 0:
            i += 1
            if i < number:
                source_index = int(source[i])
                source_left = multiplicities[source_index]
        if target_left == 0:
            j += 1
            if j < number:
                target_index = int(target[j])
                target_left = multiplicities[target_index]
    if j != number or source_left or target_left:
        raise AssertionError("The integer transport did not exhaust both spectra.")
    work = math.fsum(terms)
    absolute_transport_work = math.fsum(abs(x) for x in terms)
    mass_total = float(np.sum(masses, dtype=np.longdouble))
    transported_mass = math.fsum(transported_mass_terms)
    initial_energy = float(np.sum(masses * (k1 + np.longdouble(thermo["alpha_value"]) * k2), dtype=np.longdouble))
    expected_energy = n * thermo["single_copy_energy"]
    winf = thermo["asymptotic_work_per_copy"]
    # This is a conservative diagnostic threshold, not a rigorous interval bound.
    tolerance = 1e-11 * max(1.0, n * thermo["alpha_value"], absolute_transport_work)
    if work < -tolerance or work > n * winf + tolerance:
        raise ArithmeticError("The numerical work violates its thermodynamic bounds.")
    return {
        "alpha": model.alpha,
        "alpha_value": thermo["alpha_value"],
        "beta": model.beta,
        "delta": model.delta,
        "n": n,
        "type_count": number,
        "transport_blocks": len(terms),
        "work": work,
        "work_per_copy": work / n,
        "asymptotic_work_per_copy": winf,
        "fraction": work / (n * winf) if winf > 0 else None,
        "n_delta": n * float(Fraction(model.delta)),
        "n_delta_squared": n * float(Fraction(model.delta)) ** 2,
        "type_probability_sum": mass_total,
        "transported_probability_sum": transported_mass,
        "initial_energy_error": initial_energy - expected_energy,
        "absolute_transport_work": absolute_transport_work,
        "diagnostic_absolute_tolerance": tolerance,
        "ordering_certificate": certificate,
        "seconds": time.perf_counter() - start,
    }


def brute_force_work(n: int, model: Model) -> float:
    """Independent definition-level microstate calculation for tiny n."""
    with localcontext() as context:
        context.prec = DPS
        alpha, beta, delta = model.decimal_values()
        energies = (Decimal(0), Decimal(1), alpha)
        weights = (Decimal(1), (-beta).exp(), (-beta * alpha + delta).exp())
        z = sum(weights)
        probabilities = tuple(w / z for w in weights)
        spectrum = []
        for sequence in itertools.product(range(3), repeat=n):
            energy = sum(energies[x] for x in sequence)
            probability = math.prod(probabilities[x] for x in sequence)
            spectrum.append((energy, probability))
        initial = sum(e * p for e, p in spectrum)
        passive = sum(
            e * p for e, p in zip(sorted(e for e, _ in spectrum), sorted((p for _, p in spectrum), reverse=True))
        )
        return float(initial - passive)


def first_activation(model: Model, maximum_n: int) -> int | None:
    """Independent integer inversion criterion, including strict boundaries."""
    offset = Fraction(model.delta) / Fraction(model.beta)
    for p in range(1, maximum_n + 1):
        for q in range(1, p):
            if model.golden:
                gap_positive = quadratic_sign(q - 2 * p, q) > 0
                # alpha*q-p < offset*q is strict, as is population inversion.
                a = (q - 2 * p) * offset.denominator - 2 * offset.numerator * q
                gap_small = quadratic_sign(a, q * offset.denominator) < 0
            else:
                gap = model.rational_alpha * q - p
                gap_positive, gap_small = gap > 0, gap < offset * q
            if gap_positive and gap_small:
                return p
    return None


def run_checks() -> dict:
    checks = []
    brute_models = [Model("2", delta="0.3"), Model("3/2", delta="0.2"), Model("golden", delta="0.2")]
    for model in brute_models:
        thermo = thermodynamic_data(model)
        for n in (1, 2, 3, 5, 7):
            compressed = full_work(n, model, thermo)
            brute = brute_force_work(n, model)
            difference = abs(compressed["work"] - brute)
            passed = difference < 2e-12
            checks.append({"kind": "brute_force", "alpha": model.alpha, "delta": model.delta, "n": n,
                           "compressed_work": compressed["work"], "brute_work": brute,
                           "absolute_difference": difference, "passed": passed})
    for alpha in ("2", "golden"):
        model = Model(alpha, delta="0")
        thermo = thermodynamic_data(model)
        for n in (1, 8, 64, 256):
            result = full_work(n, model, thermo)
            checks.append({"kind": "thermal", "alpha": alpha, "n": n, "work": result["work"],
                           "passed": result["work"] == 0 and abs(result["type_probability_sum"] - 1) < 1e-14})
    for model in (Model("2", delta="0.3"), Model("2", delta="0.25"),
                  Model("golden", delta="0.1"), Model("golden", delta="0.2")):
        activation = first_activation(model, 30)
        if activation is None:
            raise AssertionError("The chosen activation check has no inversion below 30 copies.")
        before = full_work(activation - 1, model)
        at = full_work(activation, model)
        checks.append({"kind": "activation", "alpha": model.alpha, "delta": model.delta,
                       "predicted_first_n": activation, "work_before": before["work"], "work_at": at["work"],
                       "passed": abs(before["work"]) < 2e-14 and at["work"] > 1e-15})
    # At delta=1/4 the seven-copy pair is tied, so strict first activation is n=9.
    tie = full_work(7, Model("2", delta="0.25"))
    checks.append({"kind": "exact_probability_tie", "alpha": "2", "delta": "0.25", "n": 7,
                   "work": tie["work"], "passed": abs(tie["work"]) < 2e-14})
    summary = {"all_passed": all(x["passed"] for x in checks), "check_count": len(checks), "checks": checks}
    if not summary["all_passed"]:
        raise AssertionError(json.dumps(summary, indent=2))
    return summary


def scaling_cases():
    # Rational family: equal n*delta^2 across two perturbation strengths.
    for delta, sizes in (("0.1", (80, 160, 320)), ("0.05", (320, 640, 1280))):
        for n in sizes:
            yield "rational_scaling", Model("2", delta=delta), n
    # Golden family: follow two lower-convergent windows to avoid claiming a
    # universal crossover curve where continued-fraction oscillations remain.
    # delta=2*(golden-p/q), rounded to the stated exact decimal input.
    for p, q in ((8, 5), (21, 13)):
        with localcontext() as context:
            context.prec = DPS
            delta = format(2 * ((1 + Decimal(5).sqrt()) / 2 - Decimal(p) / q), ".14g")
        for factor in (2, 4, 7):
            yield "golden_convergent_window", Model("golden", delta=delta), factor * q * q
    # The Hamiltonian changes with delta here; this is a separate boundary case.
    for delta in ("0.1", "0.05", "0.025", "0.0125"):
        alpha = str(Fraction(2) + Fraction(delta) / 2)
        yield "two_copy_detuning", Model(alpha, delta=delta), 2


def detuning_formula(model: Model) -> float:
    with localcontext() as context:
        context.prec = DPS
        alpha, beta, delta = model.decimal_values()
        weights = (Decimal(1), (-beta).exp(), (-beta * alpha + delta).exp())
        z = sum(weights)
        p0, p1, p2 = (w / z for w in weights)
        return float((alpha - 2) * (p0 * p2 - p1 * p1))


def environment() -> dict:
    return {"python": sys.version, "platform": platform.platform(), "numpy": np.__version__,
            "normalization_precision_digits": DPS,
            "longdouble_epsilon": float(np.finfo(np.longdouble).eps)}


def write_json(path: Path, data) -> None:
    path.write_text(json.dumps(data, indent=2, allow_nan=False) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("check", "scaling", "all", "case"))
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).parent / "data")
    parser.add_argument("--alpha", default="2")
    parser.add_argument("--beta", default="1")
    parser.add_argument("--delta", default="0.1")
    parser.add_argument("--n", type=int, default=10)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    if args.mode == "case":
        print(json.dumps(full_work(args.n, Model(args.alpha, args.beta, args.delta)), indent=2))
        return
    if args.mode in ("check", "all"):
        checks = run_checks()
        write_json(args.output_dir / "checks.json", {"environment": environment(), **checks})
        print(json.dumps({"checks_passed": checks["all_passed"], "count": checks["check_count"]}), flush=True)
    if args.mode in ("scaling", "all"):
        results = []
        cache = {}
        for family, model, n in scaling_cases():
            if model not in cache:
                cache[model] = thermodynamic_data(model)
            result = {"family": family, **full_work(n, model, cache[model])}
            if family == "two_copy_detuning":
                result["two_copy_formula"] = detuning_formula(model)
                result["formula_absolute_difference"] = abs(result["work"] - result["two_copy_formula"])
            results.append(result)
            print(json.dumps(result, allow_nan=False), flush=True)
            # Checkpoint each completed case so an interrupted run preserves data.
            write_json(args.output_dir / "scaling.json", {"environment": environment(), "results": results})
        fieldnames = list(dict.fromkeys(key for row in results for key in row))
        with (args.output_dir / "scaling.csv").open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)


if __name__ == "__main__":
    main()
