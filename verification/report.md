# Verification results

The exact-multiplicity rearrangement algorithm passed all 28 checks and evaluated 16 selected scaling/detuning cases, including a full-unitary optimization at 1,280 copies. The data show a close collapse under $`n\delta^2`$ for the harmonic spectrum and under $`n\delta`$ for two corresponding continued-fraction windows of the golden spectrum. These observations check the analytic mechanisms; they do not establish the asymptotic exponents on their own.

All results below use $`\beta=1`$. The extracted fraction is

```math
F_n=\frac{W_n}{n\,w_\infty},
```
where $`w_\infty`$ is obtained from the Gibbs state with the same entropy as the input state. The complete parameters and diagnostic fields are in `data/scaling.json` and `data/scaling.csv`.

## Independent and boundary checks

The compressed calculation was compared with an independent 70-digit enumeration of all $`3^n`$ microstates, for $`n=1,2,3,5,7`$ and three spectra/perturbations: $`(\alpha,\delta)=(2,0.3),(3/2,0.2),(\varphi,0.2)`$. The largest absolute work difference was **2.61 × 10⁻¹⁸**.

For both $`\alpha=2`$ and $`\alpha=\varphi`$, exactly thermal inputs at $`n=1,8,64,256`$ gave zero work. The independent strict inversion criterion gave the following first-activation boundaries, all reproduced by full spectral sorting.

| Spectrum | Perturbation | First active block | Work immediately below | Work at first active block |
|---|---:|---:|---:|---:|
| $`\alpha=2`$ | 0.30 | 7 | 0 | 9.36906 × 10⁻⁶ |
| $`\alpha=2`$ | 0.25 | 9 | 0 | 7.12568 × 10⁻⁷ |
| $`\alpha=\varphi`$ | 0.10 | 8 | 0 | 3.80781 × 10⁻⁷ |
| $`\alpha=\varphi`$ | 0.20 | 3 | 0 | 5.01611 × 10⁻⁴ |

At $`\alpha=2,\delta=1/4,n=7`$, the candidate first inversion is an exact probability tie. The code correctly returns zero rather than treating the boundary as strictly active.

Across the scaling suite, type probabilities and transported probabilities both summed to one at the printed precision. The largest discrepancy between the type-distribution mean energy and $`n\operatorname{tr}(\rho H)`$ was **5.69 × 10⁻¹⁴**. The four two-copy detuning calculations agree with their closed formula to within **1.90 × 10⁻¹⁹**. These are observed numerical checks, not interval-certified error bounds at all block sizes.

## Fixed harmonic spectrum

Here $`\alpha=2`$ is held fixed. Halving $`\delta`$ and multiplying $`n`$ by four approximately preserves the extracted fraction.

| $`n\delta^2`$ | $`\delta=0.1`$: block $`n`$ | Fraction | $`\delta=0.05`$: block $`n`$ | Fraction |
|---:|---:|---:|---:|---:|
| 0.8 | 80 | 0.011558 | 320 | 0.010709 |
| 1.6 | 160 | 0.121279 | 640 | 0.113228 |
| 3.2 | 320 | 0.385774 | 1280 | 0.369538 |

The last row exceeds one third in both cases. The first active block is therefore not a useful proxy for the block required to recover a substantial fraction of the available mean work.

## Fixed golden spectrum

Here $`\alpha=\varphi=(1+\sqrt5)/2`$ remains fixed. Irrational spectra can show continued-fraction oscillations; a single smooth crossover function is not claimed. To compare the same approximation regime, the two perturbations are chosen near

```math
\delta_q=2(\varphi-p/q),\qquad (p,q)=(8,5),(21,13),
```
and then rounded to the exact decimal inputs printed in the data. Blocks are $`n=Lq^2`$, with $`L=2,4,7`$. This phase-aligned choice is disclosed rather than treated as an unselected sweep.

| $`L`$ | $`\delta=0.036067977499790`$: $`n`$ | $`n\delta`$ | Fraction | $`\delta=0.0052987467305589`$: $`n`$ | $`n\delta`$ | Fraction |
|---:|---:|---:|---:|---:|---:|---:|
| 2 | 50 | 1.80340 | 0.601463 | 338 | 1.79098 | 0.593418 |
| 4 | 100 | 3.60680 | 0.803122 | 676 | 3.58195 | 0.799947 |
| 7 | 175 | 6.31190 | 0.898998 | 1183 | 6.26842 | 0.896133 |

The nearly matching fractions occur at nearly matching $`n\delta`$, despite a factor of about 6.81 between the perturbations. This is consistent with the recurrence of useful rational approximants at denominators of order $`\delta^{-1/2}`$. The broad exponent claim still rests on the number-theoretic and all-unitary analytic arguments, not on these two windows.

## Two-copy detuning boundary

This is a different family, with a Hamiltonian that changes as $`\alpha(\delta)=2+\delta/2`$. A single swap between one $`|0,2\rangle`$ state and $`|1,1\rangle`$ gives

```math
W_2=(\alpha-2)(p_0p_2-p_1^2).
```
Full sorting equals this formula for the selected parameters.

| $`\delta`$ | $`\alpha`$ | $`W_2`$ | $`W_2/(2w_\infty)`$ |
|---:|---:|---:|---:|
| 0.1000 | 2.05000 | 1.5212880 × 10⁻⁴ | 0.433846 |
| 0.0500 | 2.02500 | 3.7732156 × 10⁻⁵ | 0.433730 |
| 0.0250 | 2.01250 | 9.3955696 × 10⁻⁶ | 0.433647 |
| 0.0125 | 2.00625 | 2.3442114 × 10⁻⁶ | 0.433599 |

The work shrinks quadratically while a nonzero fraction remains accessible with two copies. This illustrates the nonuniformity of the fixed-spectrum limit. It is not evidence that every small detuning removes the collective-size barrier.

For this choice $`\beta=1`$ and detuning coefficient $`\nu=1/2`$, the closed limiting fraction derived in [calibration analysis](../science/calibration.md) is

```math
\frac14\left(1+\frac{3e^{-1}}{1+e^{-1}+e^{-2}}\right)\simeq0.433546.
```
The displayed two-copy data approach that value. There is one exchanged lower-energy microstate; the degeneracy of the $`|0,2\rangle,|2,0\rangle`$ energy does not supply a second $`|1,1\rangle`$ state and does not introduce a factor of two in $`W_2`$.

## Scope

The calculation optimizes average work under unrestricted block unitaries for known diagonal inputs. It does not charge compilation, gate count, driving time, control precision, or work-storage entropy. It does not establish reliable positive output from one block or a reduced total specimen count for that reliability. No fit of a power-law exponent was performed.
