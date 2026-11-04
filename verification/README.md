# Numerical verification

`ergotropy.py` evaluates the full unitary ergotropy of the known product state

```math
\rho_\delta=\frac{\exp[-\beta\,\mathrm{diag}(0,1,\alpha)+\delta\,\mathrm{diag}(0,0,1)]}{Z_\delta}.
```
It solves the spectral rearrangement problem. It does not evaluate only the particular swaps used in an achievability proof.

## Reproduce

Python 3.11 or later and NumPy are sufficient for the numerical calculation. The recorded run used Python 3.12.14 and NumPy 2.3.5. The optional figure also needs Matplotlib.

```bash
python verification/ergotropy.py all --output-dir verification/data
python verification/plot_results.py
```

These commands assume the current directory contains `verification/`. Each completed scaling case is checkpointed to JSON. The CSV is written when the suite finishes. To run one case:

```bash
python verification/ergotropy.py case --alpha 2 --beta 1 --delta 0.05 --n 1280
python verification/ergotropy.py case --alpha golden --beta 1 --delta 0.0052987467305589 --n 338
```

Input decimals and fractions are interpreted as exact rational numbers. The string `golden` denotes the algebraic number $`(1+\sqrt5)/2`$, rather than its floating-point approximation.

## What is exact

There are $`(n+1)(n+2)/2`$ occupation types. Their multinomial multiplicities are arbitrary-precision integers, computed by recurrences and checked to sum exactly to $`3^n`$. The algorithm transports integer numbers of eigenvalues between sorted type blocks; splitting a multiplicity block involves no approximation of its integer size.

For rational $`\alpha,\beta,\delta`$, both energy and probability ranks use integer keys. For the golden spectrum, floating-point sorting proposes an order, after which **every adjacent pair is checked using the exact sign of an integer expression $`a+b\sqrt5`$**. An incorrect order raises an error. Exact probability ties are resolved in energy order and do not create spurious work at a passivity boundary.

## What is numerical

Probability masses use normalized binomial recurrences centered at their modes, evaluated in NumPy's `longdouble` type. This avoids factorial overflow and exponentiating differences between large logarithms. Energy differences for the golden spectrum use rationalization when direct subtraction would lose precision. Signed transported work is accumulated with `math.fsum`. The equal-entropy Gibbs normalization is calculated with 70 decimal digits using Python's standard-library `Decimal` module.

The final energy and work values are numerical approximations, not rigorous interval enclosures. The `diagnostic_absolute_tolerance` field is a conservative consistency threshold, not a proved error bar. The brute-force checks and the probability/energy diagnostics quantify the observed accuracy. Platforms on which `longdouble` equals `double` may have somewhat different rounding errors; its machine epsilon is recorded in the JSON metadata.

The run includes a case at $`n=1280`$, with 821,121 types. Although the number of types is quadratic, their integer multiplicities have up to order $`n`$ bits. Consequently the exact-count representation can require order $`n^3`$ bits of storage; this implementation makes no near-linear memory claim.

## Files

- `data/checks.json`: 28 definition-level, thermal, and activation-boundary checks.
- `data/scaling.json` and `data/scaling.csv`: the 16 selected scaling and detuning cases, including parameters and diagnostics.
- `report.md`: the results, their interpretation, and the limits of the numerical evidence.
- `plot_results.py`: reproduces `figures/work_scaling.png` and `figures/work_scaling.pdf` from the saved JSON.

The data support finite-size consistency checks. They do not prove a limiting exponent, eliminate logarithmic gaps, or establish a universal crossover curve.
