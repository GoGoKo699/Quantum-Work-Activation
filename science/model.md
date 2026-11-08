# Model and main results

A passive state has no extractable work under a cyclic unitary acting on one copy. Several copies can nevertheless yield work. The question here is how many copies must belong to the same controlled block to recover a fixed fraction of the asymptotic mean work when the state approaches equilibrium.

The single-copy state and Hamiltonian are known. The resource being counted is the population of a jointly processed block. This model is the standard ergotropy setting of [Allahverdyan, Balian and Nieuwenhuizen](../references/RELATED_WORK.md#ergotropy) and [Alicki and Fannes](../references/RELATED_WORK.md#asymptotic-work).

## 1. State, energy and operations

Set the first excitation energy to one and use natural logarithms. Fix $`\alpha>1`$ and $`\beta>0`$, and write

```math
H_\alpha=\mathrm{diag}(0,1,\alpha),\qquad
K=\mathrm{diag}(0,0,1),\qquad
\rho_{\delta,\alpha}
=\frac{\exp(-\beta H_\alpha+\delta K)}{Z_{\delta,\alpha}}.
```
The perturbation parameter satisfies $`\delta>0`$ and tends to zero. For

```math
0<\delta<\beta(\alpha-1),
```
the three populations are decreasing with energy, so one copy is passive. The reference Gibbs state is $`\gamma_{\beta,\alpha}=\rho_{0,\alpha}`$.

On $`n`$ copies, the Hamiltonian is the noninteracting sum

```math
H_\alpha^{(n)}=\sum_{j=1}^{n}H_{\alpha,j}.
```
A protocol is an arbitrary prescribed unitary on these $`n`$ systems. Equivalently, an external driving term may act during a finite interval and vanish at both endpoints. There is no thermal bath, catalyst, ancillary state or feedback record in the optimization. Preparation and classical knowledge of the input are supplied. The duration, circuit complexity and physical controller are outside the charged block-size resource.

The ergotropy is

```math
W_n(\delta;\alpha)
=\mathrm{Tr}[\rho_{\delta,\alpha}^{\otimes n}\,H_\alpha^{(n)}]
-\min_U\mathrm{Tr}[
U\,\rho_{\delta,\alpha}^{\otimes n}\,U^\dagger\,H_\alpha^{(n)}
].
```
It is an average energy decrease. The input is diagonal, so a permutation of energy eigenstates attains the optimum. The lower bounds nevertheless apply to every unitary, including coherent operations.

## 2. The benchmark and block-size resource

Let $`\beta_*(\delta;\alpha)>0`$ be the inverse temperature whose Gibbs state has the same entropy as $`\rho_{\delta,\alpha}`$. Define

```math
w_\infty(\delta;\alpha)
=\mathrm{Tr}\!\left[
H_\alpha\left(\rho_{\delta,\alpha}
-\gamma_{\beta_*(\delta;\alpha),\alpha}\right)
\right].
```
The [established asymptotic ergotropy theorem](../references/RELATED_WORK.md#asymptotic-work) gives

```math
0\le \frac{W_n(\delta;\alpha)}{n}\le w_\infty(\delta;\alpha),
\qquad
\lim_{n\to\infty}\frac{W_n(\delta;\alpha)}{n}
=w_\infty(\delta;\alpha)
```
for each fixed positive $`\delta`$. The endpoint is inherited; the present question concerns the smallest block approaching a fixed fraction of it as $`\delta`$ vanishes.

For a fixed fraction $`f\in(0,1)`$, put

```math
N_f(\delta;\alpha)
=\min\left\{n\ge1:
W_n(\delta;\alpha)\ge f n w_\infty(\delta;\alpha)
\right\}.
```
Processing independent blocks of size $`n`$ repeats the rate $`W_n/n`$. A circuit of small-arity gates that connects an arbitrarily large collection belongs to that larger block; gate arity is not the meaning of $`N_f`$.

The [thermodynamic expansion](thermodynamic_scale.md) is

```math
w_\infty(\delta;\alpha)
=\frac{R_{\alpha,\beta}}{2\beta}\delta^2+O_{\alpha,\beta}(\delta^3),
\qquad
R_{\alpha,\beta}
=\mathrm{Var}_{\gamma}(K)
-\frac{\mathrm{Cov}_{\gamma}(H_\alpha,K)^2}
{\mathrm{Var}_{\gamma}(H_\alpha)}>0.
```
Thus all spectral cases are compared at the same order of available work per input copy.

## 3. Spectral conditions

A fixed irrational number $`\alpha`$ has irrationality exponent two in the sense used here if, for every $`\eta>0`$, some $`\kappa_\eta>0`$ satisfies

```math
\left|\alpha-\frac pq\right|
\ge \frac{\kappa_\eta}{q^{2+\eta}}
```
for all integers $`p`$ and positive integers $`q`$. This condition holds for Lebesgue-almost-every real $`\alpha`$; the [elementary measure argument](achievability.md) is included with the construction.

The stronger badly approximable condition is the existence of $`\kappa>0`$ such that

```math
\left|\alpha-\frac pq\right|
\ge \frac{\kappa}{q^2}
```
for all $`p,q`$. Quadratic irrationals, including the golden ratio, satisfy it.

## 4. Main theorem: one-third mean-work recovery

Fix $`\alpha>1`$, $`\beta>0`$, and $`0\lt f\le1/3`$. All limits below take $`\delta\downarrow0`$ with these quantities fixed.

**Rational spectrum.** If $`\alpha=a/b`$ is reduced, there are positive constants $`c,C,\delta_0`$ such that

```math
\frac{c}{\delta^2}
\le N_f(\delta;\alpha)
\le \frac{C}{\delta^2},
\qquad 0<\delta<\delta_0.
```
The lower bound is inherited from [Collective-Work-Thresholds](converses.md#corollary-4a-the-inherited-sharp-rational-bound); the upper bound is this repository's [one-third construction](achievability.md#5-rational-spectra-a-uniform-one-third-fraction). Their combination is $`N_f=\Theta(\delta^{-2})`$. In particular,

```math
\lim_{\delta\downarrow0}
\frac{\log N_f(\delta;\alpha)}{\log(1/\delta)}=2.
```
**Generic irrational spectrum.** If $`\alpha`$ has irrationality exponent two, then

```math
\lim_{\delta\downarrow0}
\frac{\log N_f(\delta;\alpha)}{\log(1/\delta)}=1.
```
Equivalently, for every $`\epsilon>0`$, all sufficiently small $`\delta`$ satisfy

```math
\delta^{-1+\epsilon}\le N_f(\delta;\alpha)
\le\delta^{-1-\epsilon}.
```
**Badly approximable spectrum.** Under the stronger condition, positive constants $`c,C,\delta_0`$ give

```math
\frac{c}{\delta\log(1/\delta)}
\le N_f(\delta;\alpha)
\le\frac{C}{\delta},
\qquad 0<\delta<\delta_0.
```
Constants depend on the fixed spectrum, temperature and fraction. In the generic case they may also depend on the exponent slack. The rational bounds match up to constants. The irrational statements determine logarithmic exponents; their displayed logarithmic gaps are retained.

### Proof route

The [construction](achievability.md) pairs a nonvanishing amount of probability in translated occupation classes. An explicit Gaussian overlap bound makes one-third recovery sufficient for the theorem. Rational spectra use their first nonzero many-copy energy gap. Generic spectra use rational approximations in an interval that balances the energy gain and population inversion.

The [converses](converses.md) compare the full product input with passive states. For fixed rational spectra, the inherited CWT relative-entropy clipping estimate removes an extensive bandwidth factor and gives a sharp lower block scale; the older trace-distance estimate remains a valid weaker bound. Irrational spectra permit an ordered extension of a typical set. These arguments cover the optimum over all unitaries.

## 5. Calibration statement and limits

The [calibration result](calibration.md) gives a uniform version of the exponent-one law around a nominal irrationality-exponent-two spectrum. The actual spectrum and its prepared state may vary with $`\delta`$, provided

```math
|\widetilde\alpha-\alpha|\le\frac{\delta}{8\beta},
\qquad
\rho_{\delta,\widetilde\alpha}
\propto \exp(-\beta H_{\widetilde\alpha}+\delta K).
```
The fraction $`0\lt f\le1/3`$ remains fixed. This matched preparation condition is part of the result.

The rational theorem is a fixed-spectrum statement. An explicit two-copy detuning example in the same account shows why its lower bound cannot be extended indiscriminately to shrinking neighborhoods of a harmonic spectrum.

## 6. A matched path near the harmonic point

Fix $`\beta,\nu>0`$ and let $`\alpha_\delta=2+\nu\delta^{3/2}`$, with the input exactly $`\rho_{\delta,\alpha_\delta}`$. The [matched-detuning theorem](matched_detuning.md) proves

```math
N_{1/10}(\delta;\alpha_\delta)=\Theta(\delta^{-2}).
```

Writing $`\epsilon=\nu\delta^{3/2}`$ and $`t=\delta-\beta\epsilon>0`$, its new finite comparison is

```math
W_n(t;2)\le W_n(\delta;2+\epsilon)
\le W_n(t;2)+n\epsilon\delta/2.
```

The actual work benchmark is $`w_\infty(\delta;\alpha_\delta)=R_{2,\beta}\delta^2/(2\beta)+O(\delta^3)`$. Its ratio to the harmonic benchmark at $`t`$ tends to one, and the normalized comparison error is $`O(\sqrt\delta)`$ uniformly in $`n`$. The inherited harmonic converse and one-third construction therefore transfer to fraction $`1/10`$. Two copies are active but recover a vanishing fraction. This path does not replace the order-$`\delta`$ counterexample and establishes no full crossover law.

The [first-activation threshold](activation.md) concerns any positive work and is smaller than the fixed-fraction block scale. The [interpretation](interpretation.md) separates both from work reliability, gate cost and extraction time.

[Scientific guide](README.md) · [Repository overview](../README.md)
