# Physical mechanism and scope

The [main theorem](model.md) concerns a collective-control requirement: how many systems have to be available to the same prescribed unitary before a fixed share of their mean-work potential becomes accessible. It separates three quantities that need not have the same scaling: the first block with positive work, the block recovering a finite fraction, and the total number of specimens used for a reliable output.

## Why the spectral arithmetic enters

An occupation type records how many copies occupy each of the three levels. Moving between two types with difference

```math
\Delta=(p-q,-p,q)
```
changes their energy by $`h=\alpha q-p`$ and their log probability per microstate by $`s=\delta q-\beta h`$. Both must be positive for the swap to extract work. A useful displacement therefore balances the energy gap against the small departure from equilibrium.

For a fixed rational spectrum $`\alpha=a/b`$, every nonzero energy gap is at least $`1/b`$. A population inversion across such a gap needs $`q`$ of order $`\delta^{-1}`$. For a generic irrational spectrum, a useful approximation can have $`h`$ of order $`\delta q`$ already at denominators whose logarithmic exponent is one half. The [Farey argument](achievability.md#6-useful-rational-approximants) finds approximants in a whole interval of useful errors, so the conclusion does not depend on an isolated exceptionally small gap.

The displacement also has to pass through configurations with appreciable probability. Occupation fluctuations have width of order $`\sqrt n`$. To shift typical mass by a vector of size $`q`$, the construction uses $`n`$ of order $`q^2`$. This squares the denominator scale: exponent two for rational spectra, exponent one for generic irrational spectra. The [Gaussian strip proof](achievability.md#3-a-uniform-gaussian-limit-for-the-matched-mass) makes this reasoning quantitative and certifies a common recovered fraction of one third.

This picture alone is a construction. The [all-unitary bounds](converses.md) supply the necessary converse: at every strictly smaller logarithmic block exponent, the product input is close enough to a passive spectrum that no unitary can recover a fixed fraction. The bounds retain their logarithmic gaps, so they do not determine every subleading crossover scale.

## Work fraction and absolute output

For every fixed spectrum in the theorem, the available work per copy is

```math
w_\infty=\frac{R}{2\beta}\delta^2+O(\delta^3).
```
At a badly approximable spectrum, the constructed block has $`n=\Theta(\delta^{-1})`$, so its total mean extracted work is $`\Theta(\delta)`$. At a rational spectrum, the constructed block has $`n=\Theta(\delta^{-2})`$, and its total mean work is $`\Theta(1)`$. The comparison concerns the fraction of the available work per supplied copy, at a given thermal mismatch. It does not promise the same absolute work in a single smaller block.

The [first-activation criterion](activation.md) needs only one inverted pair. Its corresponding exponents are one and one half. Such a pair may lie in a very small tail of the occupation distribution, which is why merely establishing positive work does not establish a useful yield fraction.

## Mean work and repeated-batch reliability

For the diagonal input and a permutation protocol, two projective energy measurements would assign an extracted-work random variable $`X`$. This is a way to describe the work distribution; the extraction protocol itself does not perform or use those measurements.

Let $`M`$ be the probability mass of paired lower-energy microstates in the exact construction. Their paired upper-energy partners have total probability $`e^sM`$. Then

```math
\Pr(X=h)=e^sM,\qquad
\Pr(X=-h)=M,\qquad
\Pr(X=0)=1-(1+e^s)M.
```
Consequently,

```math
\mathbb E X=h(e^s-1)M,\qquad
\operatorname{Var}(X)
=h^2(e^s+1)M-h^2(e^s-1)^2M^2.
```
For the badly approximable construction, $`q=\Theta(\delta^{-1/2})`$, $`h,s=\Theta(\sqrt\delta)`$, and $`M`$ tends to a positive constant. Thus the mean is $`\Theta(\delta)`$, while the variance is also $`\Theta(\delta)`$. A single block has fluctuations larger than its mean as equilibrium is approached.

For $`m`$ independently repeated copies of this block protocol, the ratio of the total mean to its standard deviation is of order $`\sqrt{m\delta}`$. Keeping that ratio at a nonzero constant therefore requires $`m=\Theta(\delta^{-1})`$, hence $`\Theta(\delta^{-2})`$ total specimens for this construction. Higher confidence changes the required constants or growth. This calculation is a property of this explicit protocol; it is not an optimal reliability bound for every protocol.

The connection to [collective work-concentration results](../references/RELATED_WORK.md#fixed-fraction-collective-extraction-and-work-concentration) is therefore consistent: a smaller block for a fixed fraction of **mean** work need not reduce the complete specimen budget for reliable positive output.

## Calibration and the order of limits

The fixed-spectrum theorem compares limits taken at different fixed Hamiltonians. Its rational constants depend on the denominator. It cannot be applied uniformly to rational approximations whose denominators themselves grow as $`\delta`$ shrinks.

The [calibration theorem](calibration.md) makes a positive finite-accuracy statement around a fixed nominal irrationality-exponent-two spectrum. If the actual value lies within $`\delta/(8\beta)`$, the same nominal permutation has enough margin to retain one-third recovery at the stated scale. Its all-unitary converse is also uniform there. The actual value may be rational; that causes no contradiction with a theorem that keeps each rational spectrum fixed before taking the limit.

The preparation condition matters: every actual instance is exactly the specified Gibbs tilt for its actual Hamiltonian, with the same known basis. Arbitrary population errors, correlations or eigenvector uncertainty are not included.

Near the harmonic value, a different limit can occur. The exact two-copy example

```math
\widetilde\alpha=2+\frac{\delta}{8\beta}
```
has $`N_{1/10}=2`$ for all sufficiently small $`\delta`$, despite lying in a window of the same radius. For $`\beta=1`$, the wider but still order-$`\delta`$ detuning $`\widetilde\alpha=2+\delta/2`$ gives $`N_{1/3}=2`$. These statements refer to the explicit detuning families, not all nearby spectra.

## What remains open

The stated result leaves several distinct questions:

- **Subleading block scales.** The lower and upper bounds differ by a logarithm for rational and badly approximable spectra. The present proofs do not remove that gap.
- **Higher fractions.** The constructive argument proves a common target of one third. It does not establish the same exponent at every fraction below one or in a limit where the target tends to one.
- **Other arithmetic classes.** Exceptionally well approximable irrationals require a separate analysis; the generic theorem does not cover every irrational.
- **Effective finite-size thresholds.** The exact finite matching formula is available, but the Gaussian-limit proof does not optimize a usable numerical mismatch threshold for its one-third guarantee.
- **Broader preparation uncertainty.** The calibrated result assumes the matched state family. More general preparation errors need their own resource and error definitions.
- **Implementable control and reliability.** Circuit synthesis, control precision beyond the specified spectral window, time, controller energy, and optimal reliable-work specimen budgets are separate operational questions.

The [related-work account](../references/RELATED_WORK.md) identifies the inherited ergotropy endpoint, activation mechanism, typical-type methods and prior arithmetic effects. The [numerical report](../verification/report.md) gives finite-size consistency checks of the complete optimization; it does not replace these scope conditions.

[Scientific guide](README.md) · [Repository overview](../README.md)
