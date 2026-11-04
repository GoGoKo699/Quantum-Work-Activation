# Scientific guide

The central object is the smallest jointly controlled block that recovers a fixed fraction of a passive state's available mean work near equilibrium. The [main theorem](model.md#4-main-theorem-one-third-mean-work-recovery) gives exponent two for a fixed rational spectrum and exponent one for a full-measure class of fixed irrational spectra, for every fixed fraction up to one third.

## Reading route

1. **[Model and main results](model.md):** define the input, operations, mean-work objective and block-size resource. The theorem keeps the temperature, spectrum and target fraction fixed while the thermal mismatch tends to zero.
2. **[Thermodynamic scale](thermodynamic_scale.md):** derive the quadratic work benchmark and the residual variance that also fixes the occupation-space geometry.
3. **[First activation](activation.md):** identify the first inverted pair, then distinguish its existence from a useful amount of probability.
4. **[Achievability](achievability.md):** transport a finite amount of typical probability with disjoint swaps. A Gaussian strip gives an explicit one-third fraction, and a Farey-gap argument supplies useful spectral approximants.
5. **[Converses](converses.md):** approximate the product input by a passive state. Clipping and ordered extension bound the work of every possible unitary, including unitaries unrelated to the construction.
6. **[Calibration](calibration.md):** keep one nominally defined protocol productive throughout a shrinking uncertainty interval, and examine an exactly solvable harmonic boundary.
7. **[Interpretation](interpretation.md):** combine the mathematical steps into the physical consequence and retain the limitations concerning fluctuations, control and asymptotic thresholds.

The topic pages are the authoritative scientific account. Equation numbers are local to their pages. The [literature comparison](../references/RELATED_WORK.md) separates imported results and proof methods from the stated contribution. The [numerical report](../verification/report.md) and [reproduction instructions](../verification/README.md) give a complementary finite-size check.

## Dependencies and evidence

| Result | Necessary ingredients | Evidence location |
|---|---|---|
| Work per copy is quadratic in the thermal mismatch | Equal-entropy Gibbs state and relative-entropy expansion | [Thermodynamic scale](thermodynamic_scale.md) |
| One-third recovery at the stated upper block scales | Exact integer type matching, Gaussian strip limit, useful rational approximants | [Achievability](achievability.md) |
| No smaller logarithmic block exponent suffices | Distance to a passive state and concentration of occupation counts | [Converses](converses.md) |
| Generic exponent survives a calibrated interval | Margins in the approximation slope and uniform population geometry | [Calibration, Sections 3–4](calibration.md#3-a-constructive-margin-that-tolerates-calibration-error) |
| Harmonic detuning can yield useful two-copy work | Complete two-copy ordering and an exact population difference | [Calibration, Section 5](calibration.md#5-harmonic-resonance-an-exact-two-copy-boundary) |
| Numerical consistency of the exact optimization | Full spectral rearrangement and independent small-system enumeration | [Verification](../verification/README.md) |

The calibration statement assumes preparation matched to the actual Hamiltonian. The lower and upper block bounds retain a logarithmic gap, and the construction has an asymptotic small-mismatch threshold whose practical value is not optimized. The [scope discussion](interpretation.md#what-remains-open) records the corresponding open questions.

[Repository overview](../README.md)
