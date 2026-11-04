# Thirty milestones for quantum work activation

**How large must one jointly controlled block be to recover a fixed fraction of a passive qutrit state's available mean work as that state approaches equilibrium?** This map develops the objects, mechanism, proofs and operational boundaries needed to understand the [main theorem](../science/model.md#4-main-theorem-one-third-mean-work-recovery).

The milestones are common scientific understanding targets for any reader. Their order follows the project, and their dependencies describe how the argument fits together. The [scientific guide](../science/README.md) provides a direct specialist route to the authoritative account.

## Allocation and source convention

| Phase | Milestones | Progression |
|---|---|---|
| Background/preliminaries | M01–M12 | From energy and allowed operations to passivity, the work benchmark, occupation statistics and the precise block-size question |
| Narrative/innovation | M13–M30 | From an individual inverted pair to transport of typical probability, universal lower bounds, calibration and the contribution's physical scope |

The allocation is **12 background milestones and 18 narrative milestones**. The problem connects four bodies of ideas: ergotropy, equilibrium response, probability concentration and spectral approximation. The first phase brings those foundations into one resource question. The larger second phase is needed because an extraction construction, a lower bound against every unitary, and a calibration statement answer different parts of that question. The final milestones integrate the result with exact examples, numerical evidence, resource accounting and prior work. This map covers the connected scientific story; specialist calculations remain in their canonical topic pages.

The sole educational anchor is **Francesco Campaioli, Felix A. Pollock and Sai Vinjanampathy, _Quantum Batteries_, arXiv:1805.05507v1**: [HTML](https://arxiv.org/html/1805.05507v1), Section II, “Work extraction”; [PDF](https://arxiv.org/pdf/1805.05507v1), pp. 1–4. The principal source locations are Eqs. (4)–(11) and Figure 3. The [anchor bridge](ANCHOR_BRIDGE.md) translates notation and explains the steps supplied by this project beyond that foundation. Equation numbers below are local to the linked source.

**Source-reading correction.** The prose introducing the anchor's Eq. (8) calls it a “lower bound,” but the displayed inequality is an **upper bound**. The corresponding relation used here is $`W_n/n\le w_\infty`$, as stated in [Model, Section 2](../science/model.md#2-the-benchmark-and-block-size-resource). The project supplies its own near-equilibrium expansion, arithmetic bounds and calibration analysis. Primary research attribution remains in [Related work](../references/RELATED_WORK.md); those references do not introduce additional educational anchors.

## Phase I — Background/preliminaries

### M01 — Energy, populations and the physical state

**Central question.** What specifies the energy available in a known qutrit state?

**Understanding target.** Identify the roles of the Hamiltonian, its energy eigenbasis and the populations of a diagonal density matrix. Explain why energy differences matter for extraction, and how fixing the first excitation to one leaves the dimensionless spectral parameter $`\alpha>1`$.

**Dependencies and story role.** Entry point. Establishes the local physical objects before introducing operations or comparisons between spectra.

**Conceptual connection.** The average energy in the anchor's work definition becomes a concrete three-level population calculation for $`H_\alpha=\mathrm{diag}(0,1,\alpha)`$.

**Source pointers.** [Anchor, Section II, opening and Eq. (4)](https://arxiv.org/html/1805.05507v1); [Model, Section 1](../science/model.md#1-state-energy-and-operations).

### M02 — Cyclic control and mean extracted work

**Central question.** What operation is allowed, and what output does its work value measure?

**Understanding target.** Explain the initial-minus-final energy convention for a prescribed cyclic unitary. Identify the supplied state and its classical specification, and distinguish the counted block population from duration, controller energy and circuit complexity.

**Dependencies and story role.** Uses M01. Turns a state description into a physical optimization task with a definite resource boundary.

**Conceptual connection.** The unitary work expression fixes what the project optimizes; the allowed resources determine which later comparisons are meaningful.

**Source pointers.** [Anchor, Section II, Eqs. (4)–(6)](https://arxiv.org/html/1805.05507v1); [Model, Section 1](../science/model.md#1-state-energy-and-operations); [Converses, Section 1](../science/converses.md#1-model-and-normalization).

### M03 — Passivity as an ordering principle

**Central question.** Why can a state contain energy and still yield no work under the allowed operations?

**Understanding target.** Explain how decreasing populations assigned to increasing energies minimize energy on a unitary orbit. Relate ergotropy to spectral rearrangement and understand why a diagonal input admits an optimal permutation while the optimization still includes all unitaries.

**Dependencies and story role.** Uses M01–M02. Supplies the ordering principle behind both constructive swaps and universal impossibility bounds.

**Conceptual connection.** Passivity is a constraint on energy/population ordering, so useful work requires a defect in that ordering somewhere in the controlled block.

**Source pointers.** [Anchor, Section II, Eqs. (6)–(7) and the intervening passivity criterion](https://arxiv.org/html/1805.05507v1); [Model, Section 1](../science/model.md#1-state-energy-and-operations); [Converses, Lemma 1](../science/converses.md#lemma-1-distance-from-any-passive-state-bounds-every-unitary).

### M04 — Gibbs states and complete passivity

**Central question.** What separates a passive state from one that stays passive at every copy number?

**Understanding target.** Distinguish single-copy passivity from complete passivity in the full-support setting of this project. Explain why a three-level system permits passive non-Gibbs populations, and why approaching a Gibbs state creates a natural limit in which useful extraction becomes difficult.

**Dependencies and story role.** Uses M03. Introduces the equilibrium reference and the reason collective activation is possible.

**Conceptual connection.** The project approaches a completely passive reference through states that are individually passive but thermally mismatched.

**Source pointers.** [Anchor, Section II, discussion following Eq. (8)](https://arxiv.org/html/1805.05507v1); [Model, Section 1](../science/model.md#1-state-energy-and-operations); [Related work, ergotropy and complete passivity](../references/RELATED_WORK.md#ergotropy-complete-passivity-and-the-asymptotic-benchmark).

### M05 — A controlled departure from equilibrium

**Central question.** What does the mismatch parameter change, and why does one copy remain passive?

**Understanding target.** Interpret $`\rho_{\delta,\alpha}\propto\exp(-\beta H_\alpha+\delta K)`$ with $`K=\mathrm{diag}(0,0,1)`$ as a tilt of the upper-level population. Explain the condition $`0<\delta<\beta(\alpha-1)`$, the Gibbs limit at $`\delta=0`$, and the distinction between changing the state and changing the Hamiltonian.

**Dependencies and story role.** Uses M01–M04. Specifies the concrete family to which every later asymptotic statement refers.

**Conceptual connection.** The same population tilt that preserves local passivity can compete with a small many-copy energy gap.

**Source pointers.** [Model, Section 1](../science/model.md#1-state-energy-and-operations); [Activation, Section 1](../science/activation.md#1-exact-first-inversion-criterion); [anchor bridge](ANCHOR_BRIDGE.md).

### M06 — Copies, joint blocks and collective access

**Central question.** What changes when several independently prepared copies belong to one controlled system?

**Understanding target.** Explain the product input and additive Hamiltonian. Distinguish independent repetition of a block protocol from one unitary that connects a larger collection, even if that unitary is synthesized from gates of small arity.

**Dependencies and story role.** Uses M02–M05. Enlarges the local model to the resource whose size will be bounded.

**Conceptual connection.** Collective access changes the ordering problem across product eigenstates; it does not change the preparation into an initially correlated resource.

**Source pointers.** [Anchor, Section II, Eqs. (9)–(11)](https://arxiv.org/html/1805.05507v1); [Model, Sections 1–2](../science/model.md#1-state-energy-and-operations).

### M07 — Occupation classes and probability weight

**Central question.** How can a large product spectrum be described without losing the distinction between likelihood and probability mass?

**Understanding target.** Distinguish a microstate, its occupation type $`k=(k_0,k_1,k_2)`$, the multinomial multiplicity of that type, and its total probability. Explain why identical energy and probability per microstate allow compression, while type multiplicities remain essential to the amount of work.

**Dependencies and story role.** Uses M05–M06. Provides the representation that joins the many-copy energy spectrum to the probability distribution.

**Conceptual connection.** A favorable pair of type labels is useful only to the extent that actual microstates and probability mass can be matched.

**Source pointers.** [Achievability, Section 2](../science/achievability.md#2-exact-finite-type-matching); [Activation, Section 1](../science/activation.md#1-exact-first-inversion-criterion); [Verification, “What is exact”](../verification/README.md#what-is-exact).

### M08 — The equal-entropy work benchmark

**Central question.** What defines the total mean-work potential against which a finite block should be judged?

**Understanding target.** Explain why the relevant Gibbs reference has the input state's entropy and generally a shifted inverse temperature $`\beta_*`$. Distinguish the finite-copy upper bound from its attainment per copy as the block size tends to infinity at a fixed input state.

**Dependencies and story role.** Uses M03–M06. Supplies the global thermodynamic benchmark before asking how rapidly it becomes accessible.

**Conceptual connection.** The endpoint inherited from asymptotic ergotropy becomes the denominator in the project's finite-fraction question.

**Source pointers.** [Anchor, Section II, Eqs. (8), (10)–(11) and Figure 3](https://arxiv.org/html/1805.05507v1); [Model, Section 2](../science/model.md#2-the-benchmark-and-block-size-resource); [Thermodynamic scale, Section 1](../science/thermodynamic_scale.md#1-equal-entropy-gibbs-state).

### M09 — The quadratic thermodynamic signal

**Central question.** How much work remains when the passive input is only slightly different from equilibrium?

**Understanding target.** Explain how adjusting the Gibbs temperature removes the energy-aligned part of the perturbation. Interpret the residual variance $`R>0`$ and the expansion $`w_\infty=R\delta^2/(2\beta)+O(\delta^3)`$ through the equal-entropy relative-entropy identity.

**Dependencies and story role.** Uses M05 and M08. Establishes the small signal that every successful extraction and every converse must resolve.

**Conceptual connection.** Comparing spectra at a fixed work fraction is meaningful because their available work densities vanish at the same quadratic order, although their coefficients differ.

**Source pointers.** [Thermodynamic scale, Sections 1–2](../science/thermodynamic_scale.md#2-relative-entropy-and-the-quadratic-coefficient); [Thermodynamic scale, Section 4](../science/thermodynamic_scale.md#4-what-the-normalization-compares); [anchor bridge](ANCHOR_BRIDGE.md).

### M10 — Spectral arithmetic at a fixed Hamiltonian

**Central question.** How can rational and irrational level spacings produce different accessible many-copy gaps?

**Understanding target.** Relate a rational $`\alpha=a/b`$ to the nonzero gap floor $`1/b`$. Distinguish a badly approximable irrational's fixed quadratic lower bound from the exponent-two condition with a separate constant for every positive exponent slack. Keep the spectrum fixed when interpreting these conditions.

**Dependencies and story role.** Uses M06–M07. Supplies the arithmetic language needed to compare the gaps competing with the population tilt.

**Conceptual connection.** Rational approximation translates the spacing of product energies into quantitative restrictions on occupation displacements.

**Source pointers.** [Model, Section 3](../science/model.md#3-spectral-conditions); [Activation, Section 2](../science/activation.md#2-activation-scales); [Achievability, Section 6](../science/achievability.md#6-useful-rational-approximants).

### M11 — Typical probability and rare inversions

**Central question.** Why does the existence of a favorable transition say so little about its contribution to average work?

**Understanding target.** Explain the $`\sqrt n`$ scale of occupation fluctuations and the concentration of probability around typical counts. Distinguish a rare inverted pair from a region carrying a nonvanishing amount of probability, and recognize why both construction and converse require probability estimates.

**Dependencies and story role.** Uses M07 and M09. Connects the local ordering criterion to the weight of the many-copy distribution.

**Conceptual connection.** Arithmetic supplies possible displacements; concentration determines whether those displacements reach enough probability to matter relative to the quadratic benchmark.

**Source pointers.** [Activation, Section 3](../science/activation.md#3-why-first-activation-does-not-set-the-mean-work-block-scale); [Achievability, Section 3](../science/achievability.md#3-a-uniform-gaussian-limit-for-the-matched-mass); [Converses, Lemma 2](../science/converses.md#lemma-2-normalization-and-binomial-tails).

### M12 — The precise resource question

**Central question.** Which minimum is the theorem trying to determine, and in which order are the limits taken?

**Understanding target.** Interpret

```math
N_f(\delta;\alpha)=\min\{n\ge1:W_n(\delta;\alpha)\ge f n w_\infty(\delta;\alpha)\}.
```

Keep $`\alpha`$, $`\beta`$ and the fraction $`f`$ fixed while $`\delta\downarrow0`$. Distinguish this problem from first activation, from the fixed-input limit defining $`w_\infty`$, and from a reliable total-output requirement.

**Dependencies and story role.** Integrates M01–M11. Completes the background by combining the physical model, benchmark, arithmetic and probability into one well-defined question.

**Conceptual connection.** Figure 3 of the anchor motivates finite-copy access to an asymptotic endpoint; the project asks for its block scale when the endpoint itself vanishes.

**Source pointers.** [Anchor, Section II, Eqs. (10)–(11) and Figure 3](https://arxiv.org/html/1805.05507v1); [Model, Sections 2 and 4](../science/model.md#2-the-benchmark-and-block-size-resource); [Thermodynamic scale, Section 4](../science/thermodynamic_scale.md#4-what-the-normalization-compares).

## Phase II — Narrative/innovation

### M13 — A productive occupation displacement

**Central question.** What makes one pair of many-copy states yield positive mean work when swapped?

**Understanding target.** Interpret $`\Delta=(p-q,-p,q)`$, the energy gap $`h=\alpha q-p`$, and the log-probability advantage $`s=\delta q-\beta h`$. Explain why both $`h>0`$ and $`s>0`$ are necessary and why equality in either condition gives zero work.

**Dependencies and story role.** Uses M05, M07, M10 and M12. Starts the research narrative with its elementary physical mechanism.

**Conceptual connection.** The energy/probability ordering of passivity becomes a one-sided interval for a rational approximation to the spectrum.

**Source pointers.** [Activation, Section 1](../science/activation.md#1-exact-first-inversion-criterion); [Achievability, Section 2, Eqs. (3)–(5)](../science/achievability.md#2-exact-finite-type-matching).

### M14 — The first positive-work block

**Central question.** How early can any inversion occur, and why is that not yet the sought work fraction?

**Understanding target.** Explain why the smallest block realizing a candidate displacement has size $`p`$. Recover the first-activation exponents one for a fixed rational spectrum and one half for an irrationality-exponent-two spectrum, while retaining the possibility that the resulting work has negligible probability weight.

**Dependencies and story role.** Uses M10–M13. Establishes the first threshold and exposes the additional problem the finite-fraction theorem must solve.

**Conceptual connection.** An exact ordering change answers an existence question; useful mean work additionally depends on the distribution of the affected states.

**Source pointers.** [Activation, Sections 1–3](../science/activation.md#1-exact-first-inversion-criterion); [Verification, activation-boundary checks](../verification/report.md#independent-and-boundary-checks).

### M15 — Exact matching becomes a legitimate protocol

**Central question.** How can many favorable type pairs be combined into one unitary without counting the same microstate twice?

**Understanding target.** Explain why disjoint source and translated type sets permit a predetermined permutation. Interpret the minimum of the two multiplicities and the exact paired-work identity as the amount of probability that can actually be transported. Recognize that type labels define the operator without a measurement or feedback record.

**Dependencies and story role.** Uses M07 and M13–M14. Upgrades the individual inversion into a finite, resource-consistent extraction construction.

**Conceptual connection.** The finite combinatorial matching provides the physical protocol to which the later probability limit applies.

**Source pointers.** [Achievability, Section 2, Lemma 1 and Eq. (5)](../science/achievability.md#lemma-1-exact-paired-work); [Model, Section 1](../science/model.md#1-state-energy-and-operations).

### M16 — A nonvanishing overlap of typical states

**Central question.** Which collection of disjoint swaps moves an appreciable amount of probability?

**Understanding target.** Explain the role of a half-open strip in standardized occupation coordinates: translating it produces an exactly disjoint partner strip. Interpret the Gaussian overlap $`M_s(A)`$ as the limiting matched mass, and distinguish that controlled limit from assuming every typical microstate can be exchanged.

**Dependencies and story role.** Uses M11 and M15. Converts a valid finite protocol into a quantitative yield mechanism.

**Conceptual connection.** The local central-limit geometry supplies the probability weight missing from a first-activation argument.

**Source pointers.** [Achievability, Section 3, Lemma 2 and Eqs. (8)–(12)](../science/achievability.md#lemma-2-gaussian-strip-limit).

### M17 — One geometry fixes the benchmark and block scale

**Central question.** Why must the block size grow like the square of the useful displacement?

**Understanding target.** Connect the energy-preserving occupation direction $`v=(\alpha-1,-\alpha,1)`$ to the residual variance in M09. Explain the identity $`\sum_i v_i^2/\gamma_i=1/R`$ and the standardized displacement $`q/\sqrt{nR}`$, so a fixed overlap width leads to $`n`$ proportional to $`q^2`$.

**Dependencies and story role.** Uses M09, M13 and M16. Joins the thermodynamic normalization and the transport geometry into the scale-setting mechanism.

**Conceptual connection.** The same component of the state perturbation that cannot be absorbed into temperature also measures distance along a nearly energy-preserving occupation shift.

**Source pointers.** [Thermodynamic scale, Section 3](../science/thermodynamic_scale.md#3-the-same-coefficient-in-occupation-space); [Achievability, Section 4, Eqs. (13)–(14)](../science/achievability.md#4-the-qutrit-tangent-direction-fixes-the-batch-scale).

### M18 — Useful work at a rational spectrum

**Central question.** How can the fixed gap floor still support a common finite work fraction?

**Understanding target.** Explain how the congruence choice fixes $`h=1/b`$ while choosing $`q`$ of order $`\delta^{-1}`$ creates a population advantage. Combine that choice with the strip geometry to obtain $`N_{1/3}=O(\delta^{-2})`$. Understand why the strict limiting margin above one third yields an eventual guarantee for every fixed temperature.

**Dependencies and story role.** Uses M10 and M15–M17. Gives the first complete achievability result.

**Conceptual connection.** A lattice gap, a controlled population ratio and enough typical mass together determine the rational construction.

**Source pointers.** [Achievability, Section 5, Eqs. (15)–(23)](../science/achievability.md#5-rational-spectra-a-uniform-one-third-fraction); [Achievability, Section 10](../science/achievability.md#10-scope-of-the-resulting-achievability-theorem).

### M19 — Useful approximation requires an interval

**Central question.** Why is an exceptionally small energy gap insufficient, and how is a productive gap found?

**Understanding target.** Explain why both energy gain and population advantage must remain effective. Interpret the prescribed approximation-error interval as a balance between them. Describe how a Farey-gap argument and the Diophantine lower bound guarantee a denominator within the required scale throughout that interval.

**Dependencies and story role.** Uses M10, M13 and M17. Supplies the arithmetic ingredient that changes the block scale beyond the rational case.

**Conceptual connection.** The approximation task is chosen by the work objective: accuracy must leave enough energy to extract as well as enough population inversion.

**Source pointers.** [Achievability, Section 6, Lemma 3 and Eqs. (24)–(27)](../science/achievability.md#6-useful-rational-approximants); [Achievability, Section 7, Eqs. (28)–(29)](../science/achievability.md#7-generic-irrational-spectra-more-than-one-third-at-exponent-one).

### M20 — A common fraction at the irrational scale

**Central question.** Does the arithmetic improvement survive after requiring an appreciable amount of extracted work?

**Understanding target.** Combine useful approximants with the Gaussian overlap to obtain a limiting constructed fraction exceeding one third. Explain the upper scales $`O_\epsilon(\delta^{-1-2\epsilon})`$ for exponent-two irrationals and $`O(\delta^{-1})`$ for badly approximable spectra. For every fixed $`0<\epsilon<1/2`$, keep the allowed fraction independent of that exponent slack.

**Dependencies and story role.** Uses M16–M19. Completes the constructive half of the arithmetic comparison.

**Conceptual connection.** The denominator improvement becomes a mean-work block improvement because the same transport geometry retains a fixed fraction.

**Source pointers.** [Achievability, Section 7, Eqs. (28)–(33)](../science/achievability.md#7-generic-irrational-spectra-more-than-one-third-at-exponent-one); [Achievability, full-measure argument](../science/achievability.md#why-the-condition-covers-almost-every-fixed-spectrum).

### M21 — A converse for every unitary

**Central question.** How can one rule out better protocols without enumerating all possible unitaries?

**Understanding target.** Explain why closeness to any passive state bounds the optimum extracted work by the Hamiltonian's spectral diameter times the trace norm of the difference. Recognize that the passive comparison state can be correlated and serves as a mathematical witness, with no added preparation resource.

**Dependencies and story role.** Uses M03, M09 and M12. Introduces a proof principle independent of the explicit construction.

**Conceptual connection.** Passivity and continuity convert a statement about almost-ordered probabilities into a limitation on every physical protocol in the allowed set.

**Source pointers.** [Converses, Section 2, Lemmas 1–2, Eqs. (5)–(7)](../science/converses.md#2-two-elementary-lemmas); [Model, proof route](../science/model.md#proof-route).

### M22 — The rational lower bound and its logarithm

**Central question.** Why does no much smaller rational-spectrum block recover a fixed fraction?

**Understanding target.** Explain how clipping the population tilt preserves the rational energy ordering and modifies only sufficiently rare count fluctuations. Compare the exponentially small passive-state distance with the quadratic work benchmark, obtaining a lower block bound proportional to $`1/[\delta^2\log(1/\delta)]`$ throughout the excluded range.

**Dependencies and story role.** Uses M09–M11 and M21. Provides a universal counterpart to M18 and explains the origin of the logarithmic gap.

**Conceptual connection.** The lattice gap protects almost all of the input against useful extraction at smaller blocks, even after first activation has occurred.

**Source pointers.** [Converses, Section 3, Proposition 3 and Corollary 4, Eqs. (8)–(12)](../science/converses.md#3-rational-spectrum-explicit-clipped-passive-approximation).

### M23 — Ordered typical sets at irrational spectra

**Central question.** What replaces a fixed gap floor when the product spectrum has arbitrarily small gaps?

**Understanding target.** Explain how a Diophantine bound protects ordering within a suitable typical count window. Understand why extending that ordered subset to a normalized passive state requires controlling both the omitted tails and normalization. Relate the resulting lower scale to the approximation exponent and its slack.

**Dependencies and story role.** Uses M10–M11 and M21. Supplies the universal lower bound that matches the irrational construction at logarithmic-exponent precision.

**Conceptual connection.** A finite range of likely occupation differences needs finite-scale separation, even though the entire irrational spectrum has no positive gap floor.

**Source pointers.** [Converses, Section 4, Lemma 5, Proposition 6 and Corollary 7, Eqs. (13)–(21)](../science/converses.md#4-irrational-spectrum-an-ordered-typical-subset).

### M24 — The main theorem with its exact quantifiers

**Central question.** What follows when construction and universal converse are combined?

**Understanding target.** State the result for fixed $`\alpha>1`$, $`\beta>0`$ and $`0<f\le1/3`$: the logarithmic block exponent is two for a fixed rational spectrum and one for every fixed irrationality-exponent-two spectrum. Retain the logarithmic gaps in the rational and badly approximable bounds, the dependence of constants on fixed parameters, and the restriction on the recovered fraction.

**Dependencies and story role.** Integrates M18, M20 and M22–M23. Establishes the complete fixed-spectrum conclusion before examining its stability and physical meaning.

**Conceptual connection.** The theorem is a matching statement about a resource exponent; it does not require the explicit permutation to be optimal at each finite size.

**Source pointers.** [Model, Section 4](../science/model.md#4-main-theorem-one-third-mean-work-recovery); [Converses, Corollary 7](../science/converses.md#corollary-7-block-size-exponents); [Converses, Section 5](../science/converses.md#5-scope-of-the-converse).

### M25 — One nominal protocol across a calibration interval

**Central question.** Can the same designed permutation work when the actual spectral parameter is known only to finite accuracy?

**Understanding target.** Explain the matched preparation assumption and the window $`|\widetilde\alpha-\alpha|\le\delta/(8\beta)`$. Understand why narrowing the nominal approximation interval leaves productive margins for every actual instance, and why the nominal strip center, metric and integer microstate pairing define one common protocol.

**Dependencies and story role.** Uses M16–M20 and M24. Extends the constructive mechanism from one exact spectrum to a controlled family of instances.

**Conceptual connection.** The approximation interval supplies a tolerance margin, while smooth population changes are smaller than the relevant occupation fluctuations.

**Source pointers.** [Calibration, Sections 1–3, Eqs. (1)–(11)](../science/calibration.md#1-exact-preparation-contract); [Achievability, Section 8](../science/achievability.md#8-interface-with-nominal-calibration-and-preparation).

### M26 — Uniform calibration and the order of limits

**Central question.** Why does the generic exponent survive even if an actual calibrated spectrum is rational?

**Understanding target.** Explain how finite-scale separation inherited from the fixed nominal irrational controls the actual typical set. Combine the uniform converse and construction to interpret the uniform exponent-one limit across the stated window. Distinguish a varying family of rational actual spectra from the theorem at one fixed rational spectrum.

**Dependencies and story role.** Uses M23–M25. Completes the robustness statement with an all-unitary limitation and resolves the apparent arithmetic discontinuity.

**Conceptual connection.** The relevant protection concerns occupation differences at the scale of the task; a rational/irrational label alone does not specify a uniform asymptotic limit.

**Source pointers.** [Calibration, Section 4, Eqs. (12)–(17)](../science/calibration.md#4-the-all-unitary-converse-survives-the-same-calibration-window); [Interpretation, calibration and limits](../science/interpretation.md#calibration-and-the-order-of-limits).

### M27 — A harmonic boundary visible in two copies

**Central question.** Why cannot the rational exponent-two law be extended uniformly to every shrinking spectral neighborhood?

**Understanding target.** Explain the exact inversion between the two-copy sectors with energies $`2`$ and $`2+\nu\delta`$. Connect its work to the quadratic benchmark: the family $`2+\delta/(8\beta)`$ has $`N_{1/10}=2`$ eventually, while the one-third example uses $`\beta=1`$ and the wider detuning $`2+\delta/2`$.

**Dependencies and story role.** Uses M13, M24 and M26. Tests the scope of the theorem with a complete counterexample to an unjustified uniform extension.

**Conceptual connection.** Moving the Hamiltonian with the mismatch can create a useful resonance that the fixed-spectrum limit does not contain.

**Source pointers.** [Calibration, Section 5, Eqs. (18)–(19)](../science/calibration.md#5-harmonic-resonance-an-exact-two-copy-boundary); [Verification, two-copy boundary](../verification/report.md#two-copy-detuning-boundary).

### M28 — What the numerical evidence establishes

**Central question.** Which parts of the analytic mechanism can finite-size calculation independently check?

**Understanding target.** Explain why full spectral rearrangement evaluates the optimum over unitaries, rather than only the constructed swaps. Distinguish exact integer multiplicities and certified ordering from numerical probability masses and final work values. Interpret thermal, activation, scaling and detuning checks as finite evidence with a defined precision boundary.

**Dependencies and story role.** Uses M03, M07, M14 and M24–M27. Connects the proof narrative to an independently reproducible view of the complete optimization.

**Conceptual connection.** Agreement across exact boundaries and finite regimes checks implementation and mechanism; asymptotic exponents and unresolved logarithmic factors still require the proofs.

**Source pointers.** [Verification, reproduction and accuracy](../verification/README.md); [Verification results](../verification/report.md); [Related work, contribution](../references/RELATED_WORK.md#contribution-after-these-comparisons).

### M29 — Mean work, absolute output and reliable repetition

**Central question.** What operational advantage does a smaller controlled block provide, and what resource claim does it leave open?

**Understanding target.** Distinguish recovered fraction from absolute work per block and from reliable total output. Explain why the badly approximable construction yields mean work of order $`\delta`$ per block with variance of the same order, so independent repetition can restore a total specimen scale of order $`\delta^{-2}`$ for a fixed mean-to-standard-deviation ratio.

**Dependencies and story role.** Uses M02, M09, M20 and M24. Translates the exponent theorem into its physical resource meaning.

**Conceptual connection.** The block improvement concerns joint control of mean extraction. The repetition calculation is specific to the constructed protocol and supplies no universal optimal reliability bound.

**Source pointers.** [Interpretation, work fraction and absolute output](../science/interpretation.md#work-fraction-and-absolute-output); [Interpretation, repeated-batch reliability](../science/interpretation.md#mean-work-and-repeated-batch-reliability); [Related work, collective extraction and work concentration](../references/RELATED_WORK.md#fixed-fraction-collective-extraction-and-work-concentration).

### M30 — The connected contribution and its boundary

**Central question.** What has the project added to the established theory of collective work extraction?

**Understanding target.** Give one coherent explanation joining the vanishing thermodynamic signal, useful spectral approximants, transport of typical mass and passive-state converses. Locate the fixed-fraction exponent law, matched-preparation calibration result and harmonic boundary within prior work. Retain the open logarithmic gaps, higher fractions, exceptional irrational spectra, effective thresholds, broader preparation errors and implementation/reliability questions.

**Dependencies and story role.** Integrates M12–M29. Completes the narrative from a local inversion to a global statement about collective control, its evidence and its limits.

**Conceptual connection.** The anchor supplies the ergotropy endpoint and collective setting; this project quantifies access to a fixed fraction as equilibrium is approached, with an explicit dependence on spectral arithmetic.

**Source pointers.** [Model, Sections 4–5](../science/model.md#4-main-theorem-one-third-mean-work-recovery); [Interpretation](../science/interpretation.md); [Related work, contribution and attribution](../references/RELATED_WORK.md#contribution-after-these-comparisons); [anchor bridge](ANCHOR_BRIDGE.md).

[Repository overview](../README.md) · [Scientific guide](../science/README.md) · [Anchor bridge](ANCHOR_BRIDGE.md)
