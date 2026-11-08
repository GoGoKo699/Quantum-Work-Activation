# From Watrous to useful collective work

A collection of small batteries can contain work that no battery yields on its own. The question in this project is how many batteries must be controlled together to recover a fixed share of that work when their state is close to thermal equilibrium. The answer depends on the spacing of their energy levels, even though the available work per supplied copy vanishes quadratically in the same perturbation parameter.

This guide connects the selected educational source to that question. The [scientific account](../science/README.md) contains the precise statements and proofs; the [30-milestone map](MILESTONES.md) organizes the common understanding targets.

## 1. The selected source and the relevant passages

The sole educational anchor is **John Watrous, _The Theory of Quantum Information_ (Cambridge University Press, 2018)**. The [author's book page](https://jhwatrous.github.io/books-and-courses.html) provides the manuscript reading version and errata. Use §§4.3 and 5.1–5.2; earlier state/tensor-product definitions in §2.1 can be consulted when needed. Reading the full book is not a prerequisite.

| Book passage | Purpose in this project |
|---|---|
| §§4.3.1–4.3.2, majorization for vectors and Hermitian operators | Understand why spectral rearrangement minimizes energy over all unitaries. |
| §5.1, classical entropy and relative entropy; Theorem 5.15, Pinsker | Quantify changes in the probability of an occupied level. |
| §5.2.1–5.2.2, quantum entropy, relative entropy and elementary properties | Translate unitary entropy invariance and product states into energy comparisons. |
| §5.2.3, data processing and quantum Pinsker | Bound coherent or correlated outputs without restricting the allowed unitary. |

Watrous uses base-two logarithms. This repository uses natural logarithms throughout: multiply the book's entropy and relative entropy by $`\ln2`$. In this convention binary Pinsker is $`D(p\Vert q)\ge2(p_1-q_1)^2`$, and the thermodynamic identity is $`D=\beta_*w_\infty`$ without a hidden logarithm factor.

The book supplies the information-theoretic foundations. This project supplies the thermodynamic model, the equal-entropy local expansion, integer occupation matching, spectral approximation and the matched-detuning comparison. The infinite-copy work endpoint and research-level imported ingredients retain their own [primary-source attribution](../references/RELATED_WORK.md). Campaioli–Pollock–Vinjanampathy's review remains a scientific reference, rather than a second educational anchor.

## 2. Start with the operation

Consider a three-level system whose energies, in units of its first excitation gap, are $`0,1,\alpha`$, with $`\alpha>1`$. A density matrix specifies its state. For the diagonal states used here, its diagonal entries are simply the probabilities of occupying those energy levels. Fix a positive inverse temperature $`\beta`$ and prepare

```math
H_\alpha=\mathrm{diag}(0,1,\alpha),\qquad
K=\mathrm{diag}(0,0,1),\qquad
\rho_{\delta,\alpha}
=\frac{e^{-\beta H_\alpha+\delta K}}{Z_{\delta,\alpha}}.
```

The factor $`\delta>0`$ increases the relative population of the highest level. It measures a specified departure from the Gibbs state, rather than an arbitrary distance between states. The normalization $`Z_{\delta,\alpha}`$ makes the three probabilities sum to one.

An external control applies a unitary $`U`$. “Cyclic” means that the driving term vanishes at the beginning and end, so the initial and final energies are assessed with the same Hamiltonian. The state need not return to its initial value. For $`n`$ copies the bare Hamiltonian is the sum of the individual Hamiltonians, and the extracted mean work is

```math
W(U)=\mathrm{Tr}(\rho_{\delta,\alpha}^{\otimes n}H_\alpha^{(n)})
-\mathrm{Tr}(U\rho_{\delta,\alpha}^{\otimes n}U^\dagger H_\alpha^{(n)}),
\qquad
W_n=\max_U W(U).
```

A useful elementary operation exchanges two energy eigenstates. If their energies are $`E_\ell\lt E_u`$ and their probabilities are $`P_\ell,P_u`$, exchanging them extracts

```math
(E_u-E_\ell)(P_u-P_\ell).
```

The exchange is favorable precisely when the more energetic state is also more probable. Sorting larger probabilities toward lower energies therefore minimizes the final mean energy. For a diagonal input this sorting is a permutation unitary, and the rearrangement principle shows that allowing all other unitaries cannot do better. This is the operational meaning of ergotropy in the [model](../science/model.md#1-state-energy-and-operations).

For one copy, the probability ratios satisfy

```math
\log\frac{p_0}{p_1}=\beta,\qquad
\log\frac{p_1}{p_2}=\beta(\alpha-1)-\delta.
```

Thus $`0<\delta<\beta(\alpha-1)`$ gives $`p_0>p_1>p_2`$: the state is **passive** and $`W_1=0`$. Nevertheless, the two ratios correspond to different inverse temperatures per unit energy gap when $`\delta>0`$. The state is not Gibbs. Products of its probabilities can consequently develop an inversion across many-copy energies. At $`\delta=0`$ the state is Gibbs and every tensor power remains passive. The [activation analysis](../science/activation.md) makes the distinction exact.

## 3. Translate the notation

| Watrous notation or object | Repository notation | Meaning |
|---|---|---|
| Density operator $`\rho`$ and its eigenvalues | $`\rho_{\delta,\alpha}`$, populations $`p_i`$ | Here the supplied input is diagonal and passive on one copy. |
| Register tensor products | $`n`$ independent copies and $`H_\alpha^{(n)}`$ | Product populations; additive energy. |
| Hermitian-operator majorization | Spectral rearrangement relative to $`H_\alpha^{(n)}`$ | Sorting determines the unrestricted unitary energy optimum. |
| $`H(\rho)`$ in bits | $`S(\rho)`$ in natural units | The symbol $`H_\alpha`$ here is instead the Hamiltonian. |
| Relative entropy $`D`$ with base-two logs | Natural-log $`D`$ | Multiply the book's value by $`\ln2`$. |
| Partial trace and marginals | $`\sigma_j`$ of the output $`\sigma`$ | Individual-copy states may differ even though the input copies are identical. |
| Binary measurement data processing | Measurement $`\{K,I-K\}`$ used in a proof | Bounds the population change without supplying a record to the extraction protocol. |
| Additional thermodynamic objects | $`\gamma_{\beta_*},w_\infty,f,N_f`$ | Equal-entropy Gibbs reference, available mean work, recovered fraction and minimum block. |

The central ratio is $`W_n/(n w_\infty)`$: both numerator and denominator are total block energies. Entropy is invariant under a finite unitary, but the full state spectrum is also invariant. Equality of entropies alone does not make two finite-copy states unitarily interchangeable.

## 4. A complete three-qutrit example

Choose the fixed golden spectrum

```math
\alpha=\varphi=\frac{1+\sqrt5}{2},\qquad
\beta=1,\qquad \delta=\frac15.
```

The populations are numerical evaluations of the exact Gibbs-tilt formula:

```math
(p_0,p_1,p_2)\simeq(0.6210913410,\ 0.2284867354,\ 0.1504219236).
```

They decrease with energy. On three copies, compare two individual product eigenstates:

| Eigenstate | Energy | Probability |
|---|---:|---:|
| $`\lvert\ell\rangle=\lvert1,1,1\rangle`$ | $`3`$ | $`p_1^3\simeq0.01192842153`$ |
| $`\lvert u\rangle=\lvert0,2,2\rangle`$ | $`2\varphi\simeq3.23606797750`$ | $`p_0p_2^2\simeq0.01405328166`$ |

Their energy gap and log-probability ratio are exactly

```math
h=2\varphi-3>0,\qquad
s=\log\frac{p_0p_2^2}{p_1^3}
=\frac25-(2\varphi-3)>0.
```

Apply the prescribed unitary that exchanges $`|\ell\rangle`$ and $`|u\rangle`$ and leaves all orthogonal basis states unchanged. Its exact mean work is

```math
W_{\mathrm{swap}}
=(2\varphi-3)(p_0p_2^2-p_1^3)
\simeq 5.016114341\times10^{-4}.
```

There are three permutations of $`|0,2,2\rangle`$, but only one $`|1,1,1\rangle`$. Exactly one pair is exchanged. Multiplying the work by three would incorrectly reuse the same lower-energy state. For blocks of at most three copies, the strict inversion criterion allows only the fraction $`3/2`$, which gives these two occupation classes. After this single exchange, the spectrum is passive. Thus the displayed expression also equals $`W_3`$ exactly. The integer criterion in [first activation](../science/activation.md#1-exact-first-inversion-criterion) gives $`N_{\mathrm{act}}=3`$: the first admissible numerator and denominator are $`p=3,q=2`$.

To compare this operation with the collective endpoint, solve the equal-entropy Gibbs equation. Numerically,

```math
\beta_*\simeq0.9186900835,\qquad
w_\infty\simeq1.171901458\times10^{-3},\qquad
\frac{W_3}{3w_\infty}\simeq0.1426773644.
```

Three copies unlock positive work, but recover only about **14.27%** of their asymptotic potential. In particular, first activation does not by itself demonstrate one-third recovery. The [verification report](../verification/report.md#independent-and-boundary-checks) checks this parameter choice against full spectral sorting and independent enumeration of all 27 eigenstates. The expressions and the identification of the inverted classes above are analytic; the decimals, including the entropy-matched benchmark, are numerical approximations rather than interval certificates. The case is reproducible with

```bash
python verification/ergotropy.py case --alpha golden --beta 1 --delta 0.2 --n 3
```

There is also a direct interpretation of the mean. In the two-energy-measurement description, extracted work is $`+h`$ with probability $`p_0p_2^2`$, $`-h`$ with probability $`p_1^3`$, and zero otherwise. Their weighted average is exactly $`W_{\mathrm{swap}}`$. The unitary itself uses no measurement result or feedback. A positive mean does not mean every application delivers positive work.

## 5. From the collective endpoint to a block threshold

The equal-entropy Gibbs comparison can be checked without assuming that a finite unitary actually prepares a Gibbs state. Let $`\tau=U\rho_{\delta,\alpha}^{\otimes n}U^\dagger`$ and choose $`\gamma_* =\gamma_{\beta_*,\alpha}`$ with $`S(\gamma_*)=S(\rho_{\delta,\alpha})`$. Unitarity preserves entropy, so

```math
D(\tau\Vert\gamma_*^{\otimes n})
=\beta_*\left[\mathrm{Tr}(\tau H_\alpha^{(n)})
-n\mathrm{Tr}(\gamma_*H_\alpha)\right]\ge0.
```

Here $`D`$ is relative entropy and $`\beta_*>0`$. The final energy is therefore at least the Gibbs comparison energy, giving

```math
0\le\frac{W_n}{n}\le w_\infty,
\qquad
w_\infty=\mathrm{Tr}\!\left[H_\alpha(\rho_{\delta,\alpha}-\gamma_*)\right].
```

The established collective theorem gives $`W_n/n\to w_\infty`$ for each fixed input as $`n\to\infty`$. Finite unitaries preserve the entire density-matrix spectrum, a stronger condition than preserving entropy. Accordingly, the theorem identifies a limiting energy density; it does not assert that a Gibbs product is exactly reachable at every finite $`n`$. The [model's benchmark section](../science/model.md#2-the-benchmark-and-block-size-resource) states the endpoint and its attribution.

The project then fixes a fraction and asks how soon that endpoint becomes useful:

```math
N_f(\delta;\alpha)
=\min\{n\ge1:W_n(\delta;\alpha)\ge f n w_\infty(\delta;\alpha)\}.
```

The input now moves toward equilibrium as $`\delta\downarrow0`$, with $`\alpha,\beta,f`$ fixed. This joint question needs a rate that the fixed-input endpoint theorem alone does not supply.

The normalization also needs care. Under the reference Gibbs state $`\gamma=\gamma_{\beta,\alpha}`$, set

```math
V=\mathrm{Var}_{\gamma}(H_\alpha),\qquad
C=\mathrm{Cov}_{\gamma}(H_\alpha,K),\qquad
R=\mathrm{Var}_{\gamma}(K)-\frac{C^2}{V}>0.
```

The quantity $`R`$ is the variance of the part of the population perturbation left after subtracting its best linear energy dependence. The subtracted part can be absorbed into a temperature shift. The remaining part produces the leading work potential. The [thermodynamic derivation](../science/thermodynamic_scale.md) finds $`\beta_*'(0)=-C/V`$ and

```math
w_\infty(\delta;\alpha)
=\frac{R}{2\beta}\delta^2+O(\delta^3).
```

Thus “a fixed fraction” remains a meaningful comparison even though the available work per copy tends to zero. The coefficient depends on the chosen spectrum and temperature; the comparison uses each system's own benchmark.

## 6. The missing constructive bridge: enough probability to swap

An occupation type $`k=(k_0,k_1,k_2)`$ records how many copies occupy each level, with $`k_0+k_1+k_2=n`$. Its energy, number of eigenstates, and two distinct probabilities are

```math
E(k)=k_1+\alpha k_2,\qquad
g_n(k)=\frac{n!}{k_0!k_1!k_2!},\qquad
P_n(k)=\prod_i p_{i,\delta}^{k_i},\qquad
\mu_n(k)=g_n(k)P_n(k).
```

The probability $`P_n(k)`$ belongs to one eigenstate; $`\mu_n(k)`$ belongs to the whole type. Keeping them distinct prevents the degeneracy mistake exposed by the example.

For integer numerator $`p`$ and denominator $`q`$, translate occupations by

```math
\Delta=(p-q,-p,q),\qquad
h=\alpha q-p,\qquad
s=\delta q-\beta h.
```

Every valid translated pair has energy difference $`h`$ and probability ratio $`e^s`$. Positive work requires both $`h>0`$ and $`s>0`$, or

```math
\alpha-\frac{\delta}{\beta}<\frac pq<\alpha.
```

At first activation, the extreme types $`(0,p,0)`$ and $`(p-q,0,q)`$ fit in a block of only $`p`$ copies. Their probabilities, however, can be extremely small. A useful mean yield needs many disjoint pairs carrying appreciable total probability.

Choose a set of types $`\mathcal A`$ disjoint from its translate $`\mathcal A+\Delta`$. Pair exactly $`\min\{g_n(k),g_n(k+\Delta)\}`$ distinct eigenstates from each class and exchange every pair. This is a well-defined predetermined permutation, with exact extracted work

```math
W(\mathcal A)=h(e^s-1)M_n,\qquad
M_n=\sum_{k\in\mathcal A}
\min\{\mu_n(k),e^{-s}\mu_n(k+\Delta)\}.
```

The minimum enforces the number of available partners, while disjointness prevents reusing an eigenstate. No type register is measured or supplied as an additional resource. [Achievability, Section 2](../science/achievability.md#2-exact-finite-type-matching) proves this identity.

### Why Gaussian occupations determine the scale

Multinomial occupations concentrate around their mean, with fluctuations of order $`\sqrt n`$. A displacement of order $`q`$ can overlap appreciable typical probability when $`n`$ is of order $`q^2`$. The covariance fixes the coefficient. For the energy-preserving tangent direction

```math
v=(\alpha-1,-\alpha,1),\qquad
\sum_i\frac{v_i^2}{\gamma_i}=\frac1R,
```

the standardized displacement approaches $`A=q/\sqrt{nR}`$. Choosing

```math
n=\left\lceil\frac{q^2}{A^2R}\right\rceil
```

keeps this displacement finite. A strip of occupation space and its translate are exactly disjoint; a uniform local Gaussian limit then gives a positive limiting matched mass $`M_n`$. This step converts a possible inversion into a quantitative fraction of available mean work. The [Gaussian strip lemma](../science/achievability.md#3-a-uniform-gaussian-limit-for-the-matched-mass) supplies the limit and its uniformity assumptions.

### Why the rational approximation must be useful

An extremely small energy gap can produce little work even when a swap is favorable. For the irrational construction the approximation is selected inside the narrower band

```math
\frac{1}{4\beta}
\le\frac{\alpha-p/q}{\delta}
\le\frac{3}{4\beta}.
```

Both the energy gain $`h`$ and the population advantage $`s`$ then contribute at order $`\delta q`$. The [Farey-gap argument](../science/achievability.md#6-useful-rational-approximants) proves that such fractions occur at sufficiently small denominators for every sufficiently small mismatch. An unusually good approximant along one subsequence would not supply this guarantee.

For a fixed reduced rational $`\alpha=a/b`$, the first nonzero many-copy energy gap is $`1/b`$. The construction uses that gap, with $`q`$ of order $`\delta^{-1}`$, and therefore $`n`$ of order $`\delta^{-2}`$. For a badly approximable irrational, useful denominators are of order $`\delta^{-1/2}`$, giving blocks of order $`\delta^{-1}`$. The broader irrationality-exponent-two condition permits an arbitrarily small exponent slack around this latter law.

In the irrational case, the strip choice $`A=2`$ yields the analytic limiting lower bound

```math
\liminf_{\delta\downarrow0}
\frac{W(\mathcal A_n)}{n w_\infty}
\ge 3[\Phi(2)-\Phi(1)]
=0.4077153659\ldots>\frac13,
```

where $`\Phi`$ is the standard normal distribution function. The decimal is a numerical evaluation of an analytically certified bound. The rational construction uses a separate strip choice to obtain the same one-third guarantee. These constructions establish a common fixed fraction, with a sufficiently small mismatch threshold that is not optimized for practical use.

## 7. Why an arbitrary unitary cannot beat the exponent

A construction provides an upper bound on the required block size. To show that substantially smaller blocks fail, the proof must constrain every allowed unitary. The [converses](../science/converses.md) do this by finding a passive state $`\sigma`$ close to the full product input:

```math
W_n(\delta;\alpha)
\le n\alpha\,
\|\rho_{\delta,\alpha}^{\otimes n}-\sigma\|_1.
```

The norm is trace norm, and $`n\alpha`$ is the block Hamiltonian's spectral diameter. Since a unitary cannot extract work from $`\sigma`$, closeness to $`\sigma`$ limits what the same unitary can extract from the actual input. This comparison state is a mathematical witness; it is not a supplied catalyst or an additional state prepared by the protocol.

For fixed rational spectra, the inherited CWT entropy-clipping argument strengthens this distance method: comparing the Hamiltonian with the negative logarithm of a normalized passive witness bounds total work without the extensive bandwidth factor. This removes the rational logarithmic loss. Clipping still confines modifications to unlikely occupation tails. For the relevant irrational spectra, a typical set is already correctly ordered by energy; an ordered extension supplies a passive comparison state on the whole space. Concentration bounds control the tails. These arguments explain why a few rare inversions cannot circumvent a bound on finite work fractions.

Combining construction and converse gives the [main theorem](../science/model.md#4-main-theorem-one-third-mean-work-recovery). For fixed $`\alpha>1`$, $`\beta>0`$ and $`0\lt f\le1/3`$:

| Fixed spectrum | Bound or limiting law for $`N_f`$ |
|---|---|
| Reduced rational | $`c/\delta^2\le N_f\le C/\delta^2`$ |
| Irrationality exponent two | $`\log N_f/\log(1/\delta)\to1`$ |
| Badly approximable irrational | $`c/[\delta\log(1/\delta)]\le N_f\le C/\delta`$ |

The rational logarithmic exponent is two. The generic irrational exponent is one, and its hypothesis holds for almost every fixed spectrum in the Lebesgue-measure sense. It is not a theorem for every irrational number. The constants depend on the fixed spectrum, temperature and fraction. The displayed irrational logarithmic gap remains; an exponent theorem does not determine a sharp crossover constant or establish the same law for every target fraction below one.

## 8. An entropy comparison for a changing spectrum

The same information-theoretic tools can compare nearby Hamiltonians without pretending that a moving spectrum has a fixed lattice gap. Put $`\epsilon\ge0`$ and $`t=\delta-\beta\epsilon>0`$. The actual matched input satisfies $`\rho_{\delta,2+\epsilon}=\rho_{t,2}`$. With $`P=\rho_{t,2}^{\otimes n}`$, an arbitrary output $`\sigma=UPU^\dagger`$ and $`L=\mathrm{Tr}[K_n(P-\sigma)]`$, entropy invariance gives

```math
D(\sigma\Vert P)=\delta L-\beta W_\epsilon(U)
=tL-\beta W_0(U).
```

Product-reference decomposition, entropy subadditivity, binary data processing and natural-log Pinsker give

```math
D(\sigma\Vert P)\ge\sum_jD(\sigma_j\Vert\rho_{t,2})
\ge2\sum_j(r_j-r)^2\ge2L^2/n.
```

Here $`r`$ is the input probability of level 2 and $`r_j`$ the corresponding marginal output probability. Thus a nonnegative actual-work optimizer has $`0\le L\le n\delta/2`$. A harmonic optimizer has $`L\ge0`$ as well. Combining the two optimizations proves

```math
W_n(t;2)\le W_n(\delta;2+\epsilon)
\le W_n(t;2)+n\epsilon\delta/2.
```

The [full proof](../science/matched_detuning.md#1-model-and-exact-comparison) includes coherent outputs. No physical measurement or extra record is introduced.

For $`\epsilon=\nu\delta^{3/2}`$, the actual benchmark remains $`R_{2,\beta}\delta^2/(2\beta)+O(\delta^3)`$. The harmonic benchmark at $`t`$ differs, but its ratio to the actual one tends to one. The normalized comparison error is $`O(\sqrt\delta)`$ uniformly in $`n`$. Therefore CWT's inherited harmonic converse and QWA's inherited one-third construction imply $`N_{1/10}=\Theta(\delta^{-2})`$ on this specified path. Two copies are active but recover a vanishing fraction. The order-$`\delta`$ two-copy example remains a boundary, not a contradiction or a full crossover law.

## 9. Physical resources, precision and reliability

The counted resource is the number of supplied copies belonging to one jointly controlled block. Repeating independent blocks reproduces their mean work per copy. A sequence of two-body gates that connects a large collection still uses that whole collection as its block. The count therefore does not measure gate arity, circuit depth or interaction strength. The [operation model](../science/model.md#1-state-energy-and-operations) supplies the known input and allows arbitrary prescribed cyclic unitaries; it introduces no bath, catalyst, ancillary state or feedback record. Preparation cost, control duration and controller cost are outside the optimization. A product-basis permutation has diagonal, separable endpoint states, while a particular implementation path may generate entanglement. The block-size theorem places no lower bound on entanglement generated during the control.

The arithmetic distinction also has a finite-accuracy interpretation. Around a fixed nominal irrationality-exponent-two spectrum, the [calibration theorem](../science/calibration.md) allows

```math
|\widetilde\alpha-\alpha|\le\frac{\delta}{8\beta},\qquad
\rho_{\delta,\widetilde\alpha}
\propto e^{-\beta H_{\widetilde\alpha}+\delta K}.
```

One nominally selected permutation works throughout this interval at the stated scale. The actual state must be exactly the specified tilt for the actual Hamiltonian, with a fixed known energy basis. Independent preparation errors or unknown eigenvectors are different uncertainty models.

An actual spectrum in this interval can be rational. This is compatible with the fixed-rational theorem because its denominator-dependent constants need not remain uniform along a mismatch-dependent sequence. Conversely, detuning a harmonic spectrum along $`\widetilde\alpha=2+\delta/2`$ at $`\beta=1`$ permits one-third recovery with two copies for sufficiently small $`\delta`$. The [exact two-copy boundary](../science/calibration.md#5-harmonic-resonance-an-exact-two-copy-boundary) shows why the order of limits matters.

Finally, the output is **mean work**. In the badly approximable construction, a useful block has size $`\Theta(\delta^{-1})`$, mean output $`\Theta(\delta)`$ and work variance $`\Theta(\delta)`$. Its fluctuations therefore exceed its mean near equilibrium. For this construction, independent repetition needs $`\Theta(\delta^{-1})`$ blocks merely to keep the mean-to-standard-deviation ratio at a nonzero constant, using $`\Theta(\delta^{-2})`$ total specimens. Higher confidence needs an additional reliability analysis. This is a calculation for the explicit protocol, not an optimal reliability bound on all protocols; see [physical interpretation](../science/interpretation.md#mean-work-and-repeated-batch-reliability).

The contribution is a finite-fraction collective-control threshold under a stated thermodynamic model, with an attributed sharp rational reconciliation and a separately checked matched-detuning path. Its scientific route joins the asymptotic work benchmark, typical occupation probability, useful spectral approximations and an all-unitary converse. The [scope discussion](../science/interpretation.md#what-remains-open) identifies the remaining finite-size, precision, control and reliability questions.

[Milestone map](MILESTONES.md) · [Scientific guide](../science/README.md) · [Repository overview](../README.md)
