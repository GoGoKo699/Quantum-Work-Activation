# Spectral calibration and the order of limits

The main theorem fixes one Hamiltonian before the thermal mismatch tends to zero. This note gives a quantitative calibration extension around a fixed Diophantine spectrum and an explicit boundary at the harmonic spectrum. All work quantities are mean ergotropies under arbitrary cyclic unitaries on the supplied copies.

## 1. Exact preparation contract

Fix a nominal $`\alpha>1`$ and $`\beta>0`$. An actual spectral parameter $`\widetilde\alpha>1`$ specifies

```math
H_{\widetilde\alpha}=\mathrm{diag}(0,1,{\widetilde\alpha}),\qquad
\rho_\delta({\widetilde\alpha})=\frac{e^{-\beta H_{\widetilde\alpha}+\delta K}}{Z_\delta({\widetilde\alpha})},
\qquad K=\mathrm{diag}(0,0,1).
\tag{1}
```
The preparation in this note is exactly matched to the actual Hamiltonian in (1). Every copy has the same $`{\widetilde\alpha}`$ and the same state. The eigenbasis is fixed and known. No assumption about an arbitrary unknown state, uncontrolled preparation noise, or uncertain eigenvectors is introduced.

Write $`W_n(\delta;{\widetilde\alpha})`$, $`w_\infty(\delta;{\widetilde\alpha})`$, and $`N_f(\delta;{\widetilde\alpha})`$ as in [converses.md](converses.md), always using the actual $`H_{\widetilde\alpha}`$ in the energy objective and the actual state in (1). A calibration neighborhood is a set of such fully specified instances. The constructive result below uses one and the same permutation for every instance in that neighborhood; it does not require a preparation-independent guarantee.

## 2. Uniform thermodynamic normalization

For $`{\widetilde\alpha}`$ in any sufficiently small fixed compact interval $`J\subset(1,\infty)`$ around $`\alpha`$, define $`R({\widetilde\alpha})`$ using the Gibbs state of $`H_{\widetilde\alpha}`$ at the fixed $`\beta`$:

```math
R({\widetilde\alpha})=\mathrm{Var}_{\gamma_\beta({\widetilde\alpha})}(K)
-\frac{\mathrm{Cov}_{\gamma_\beta({\widetilde\alpha})}(H_{\widetilde\alpha},K)^2}
{\mathrm{Var}_{\gamma_\beta({\widetilde\alpha})}(H_{\widetilde\alpha})}.
```
The probabilities remain strictly positive on $`J`$, and the variance of $`H_{\widetilde\alpha}`$ is bounded away from zero. The equal-entropy equation therefore defines $`\beta_*(\delta,{\widetilde\alpha})`$ as a smooth function in a common neighborhood of $`\{0\}\times J`$, because its derivative with respect to $`\beta_*`$ is $`-\beta_*\mathrm{Var}(H_{\widetilde\alpha})\ne0`$. Taylor's theorem on that compact neighborhood gives

```math
w_\infty(\delta;{\widetilde\alpha})=\frac{R({\widetilde\alpha})}{2\beta}\delta^2+O_J(\delta^3),
\tag{2}
```
where the remainder is uniform in $`{\widetilde\alpha}\in J`$. Also $`\min_JR({\widetilde\alpha})>0`$.

In particular, if $`|{\widetilde\alpha}-\alpha|\le c\delta`$, with fixed $`c<\infty`$, smoothness of $`R`$ improves (2) to

```math
\boxed{\quad
w_\infty(\delta;{\widetilde\alpha})=\frac{R(\alpha)}{2\beta}\delta^2+O_c(\delta^3)
\quad}
\tag{3}
```
uniformly throughout the calibration interval. For all sufficiently small $`\delta`$,

```math
\frac{R(\alpha)}{4\beta}\delta^2
\le w_\infty(\delta;{\widetilde\alpha})
\le\frac{3R(\alpha)}{4\beta}\delta^2.
\tag{4}
```
Thus calibration of this size does not change the leading thermodynamic resource density.

## 3. A constructive margin that tolerates calibration error

Choose a rational $`p/q`$ relative to the nominal spectrum in the narrower interval

```math
\frac{3\delta}{8\beta}
\le\alpha-\frac pq\le
\frac{5\delta}{8\beta}.
\tag{5}
```
Assume

```math
|{\widetilde\alpha}-\alpha|\le\frac{\delta}{8\beta}.
\tag{6}
```
Every state in this interval is single-copy passive when $`0<\delta<8\beta(\alpha-1)/9`$, since then $`\delta<\beta(\widetilde\alpha-1)`$ holds uniformly.

For the occupation shift $`\Delta=(p-q,-p,q)`$, its actual energy gap and actual log probability ratio are

```math
h_{\widetilde\alpha}={\widetilde\alpha}q-p,\qquad
s_{\widetilde\alpha}=\delta q-\beta h_{\widetilde\alpha}.
```
Conditions (5)-(6) imply the exact, simultaneous bounds

```math
\frac{\delta q}{4\beta}\le h_{\widetilde\alpha}\le\frac{3\delta q}{4\beta},
\qquad
\frac{\delta q}{4}\le s_{\widetilde\alpha}\le\frac{3\delta q}{4},
\qquad
h_{\widetilde\alpha}s_{\widetilde\alpha}\ge\frac{3\delta^2q^2}{16\beta}.
\tag{7}
```
The last inequality uses the minimum of $`r(1-\beta r)`$ on $`[1/(4\beta),3/(4\beta)]`$, rather than multiplying the separate lower bounds. Every selected type swap remains productive throughout the interval.

### Why the same types and the same permutation work

Let $`p_i(\delta,{\widetilde\alpha})`$ denote the single-copy populations. Direct differentiation gives

```math
\partial_{\widetilde\alpha} p_i(\delta,{\widetilde\alpha})
=-\beta p_i(\delta,{\widetilde\alpha})(\mathbf 1_{i=2}-p_2(\delta,{\widetilde\alpha})),
\qquad
|\partial_{\widetilde\alpha} p_i|\le\beta/4.
\tag{8}
```
Consequently (6) implies $`|p_i(\delta,{\widetilde\alpha})-p_i(\delta,\alpha)|\le\delta/32`$. For $`n=\Theta(q^2)`$, the discrepancy between the nominal and actual mean count vectors, divided by $`\sqrt n`$, is $`O(\delta q)`$. It tends to zero whenever $`\delta q\to0`$.

The uniform [Gaussian strip limit, Lemma 2](achievability.md#lemma-2-gaussian-strip-limit), therefore applies with the strip center and metric chosen from the nominal populations. Its hypotheses hold for every sequence of actual values satisfying (6): the actual probabilities tend to the same interior Gibbs vector, the nominal center differs from the actual center by $`o(\sqrt n)`$, and the nominal metric tends to the same limiting covariance metric. The multiplicities of the type classes depend only on their counts, so their microstate pairing can also be chosen identically for every $`{\widetilde\alpha}`$.

In particular, put $`R_0=R(\alpha)`$, choose

```math
n=\left\lceil\frac{q^2}{4R_0}\right\rceil,
```
and use the strip of standardized displacement two. The matched probability mass tends to

```math
M(2)=2[\Phi(2)-\Phi(1)],
```
where $`\Phi`$ is the standard normal distribution function. Combining that lemma, (3), and (7) gives the uniform constructive estimate

```math
\boxed{\quad
\frac{W_n(\delta;{\widetilde\alpha})}{n w_\infty(\delta;{\widetilde\alpha})}
\ge 3[\Phi(2)-\Phi(1)]-o(1)
=0.407715\ldots-o(1).
\quad}
\tag{9}
```
Uniformity can also be stated without an unstated uniform central-limit theorem: if (9) failed uniformly, a violating sequence $`\delta_j\downarrow0`$, $`{\widetilde\alpha}_j`$ satisfying (6) would satisfy every hypothesis of the triangular-array strip lemma, a contradiction. The permutation used in this argument is the nominal one, not a permutation subsequently optimized for each $`{\widetilde\alpha}_j`$.

### Denominator bounds

For a fixed irrationality-exponent-two $`\alpha`$, the useful-approximant lemma supplies a rational in (5) with

```math
q\le\delta^{-1/2-\varepsilon}
```
for each fixed $`0<\varepsilon<1/2`$ and all sufficiently small $`\delta`$. Narrowing the interval from the one used for an unperturbed construction changes only constants in the Farey-gap proof. In particular $`q\to\infty`$ and $`\delta q\to0`$, as required above. Thus (9) yields, uniformly over (6),

```math
N_f(\delta;{\widetilde\alpha})\le C_\varepsilon\delta^{-1-2\varepsilon},
\qquad 0\lt f\le1/3.
\tag{10}
```
For a badly approximable nominal $`\alpha`$ with constant $`\kappa`$, one can give an explicit order bound. Set

```math
Q=\left\lceil\sqrt{\frac{112\beta}{\kappa\delta}}\right\rceil.
\tag{11}
```
If the interval in (5) contained no order-$`Q`$ rational, it would lie in one Farey gap of length $`D=1/(uv)\ge\delta/(4\beta)`$, with $`u+v>Q`$. Taking $`u=\min(u,v)`$, one has $`v>Q/2`$. The distance of $`\alpha`$ from the endpoint of denominator $`u`$ is at most

```math
D+5\delta/(8\beta)\le(7/2)D\le7/(uQ).
```
Bad approximability implies $`\kappa/u^2\le7/(uQ)`$, hence $`u\ge\kappa Q/7`$ and $`D\le14/(\kappa Q^2)\le\delta/(8\beta)`$, a contradiction. The usual translation of the Farey sequence covers intervals outside $`[0,1]`$; for small $`\delta`$ the present interval stays away from an integer because $`\alpha`$ is fixed and irrational. Thus $`q\le Q=O(\delta^{-1/2})`$, and (9) gives the uniform upper bound $`N_f=O(\delta^{-1})`$.

## 4. The all-unitary converse survives the same calibration window

The converse does not require the actual number $`{\widetilde\alpha}`$ to be irrational. It uses only the finite-scale separation inherited from the fixed nominal $`\alpha`$.

Suppose, for some $`\mu\ge2`$,

```math
|\alpha-p/q|\ge\kappa/q^\mu\qquad(p\in\mathbb Z,\ q\ge1),
```
and allow the more general error $`|{\widetilde\alpha}-\alpha|\le c\delta`$, with fixed $`c\ge0`$. Define

```math
t_{\mu,c}(\delta)
=\left[\frac{\beta\kappa}
{2^{\mu+1}(1+\beta c)\delta}\right]^{1/\mu},
\qquad
d_{\mu,c}
=2\left[\frac{\beta\kappa}
{2^{\mu+1}(1+\beta c)}\right]^{2/\mu}.
\tag{12}
```
Select the actual typical count window $`|X-np_2(\delta,{\widetilde\alpha})|\le t_{\mu,c}`$. For any two selected microstates with count differences $`(\ell,q)`$, $`q\ne0`$,

```math
\begin{aligned}
\beta|\ell+{\widetilde\alpha}q|-\delta|q|
&\ge\frac{\beta\kappa}{|q|^{\mu-1}}
-(1+\beta c)\delta|q|\\
&\ge\frac{\beta\kappa}{2|q|^{\mu-1}}>0.
\end{aligned}
\tag{13}
```
The selected spectrum is therefore ordered under the actual Hamiltonian and the actual matched state. In particular, a new exact energy degeneracy with different selected $`X`$-counts cannot occur inside this window. The passive-extension lemma and binomial tail argument in [converses.md](converses.md) apply unchanged, giving the finite inequality

```math
\boxed{\quad
\frac{W_n(\delta;{\widetilde\alpha})}n
\le4{\widetilde\alpha}(e^{n\delta}-1)
\exp\!\left[-\frac{d_{\mu,c}}{n\delta^{2/\mu}}\right].
\quad}
\tag{14}
```
For small enough $`\delta`$, $`{\widetilde\alpha}\le\alpha+1`$. In the regime $`n\delta\le1`$, the prefactor is consequently bounded by $`4(\alpha+1)(e-1)`$, uniformly in $`{\widetilde\alpha}`$. Using the uniform lower bound (4) and the same comparison with $`\delta^3`$ as in Corollary 7 of the converse note proves, for every fixed $`f>0`$,

```math
\boxed{\quad
N_f(\delta;{\widetilde\alpha})>
\frac{d_{\mu,c}}{3\delta^{2/\mu}\log(1/\delta)}
\quad}
\tag{15}
```
for all sufficiently small $`\delta`$, uniformly over $`|{\widetilde\alpha}-\alpha|\le c\delta`$. The smallness threshold may depend on $`\alpha,\beta,\kappa,\mu,c,f`$, but not on the choice of actual $`{\widetilde\alpha}`$ within the interval.

### Uniform calibration conclusion

For a fixed irrationality-exponent-two nominal $`\alpha`$, combine (10) and (15), with $`c=1/(8\beta)`$, first for each fixed exponent slack and then let the slack tend to zero. For every fixed $`0\lt f\le1/3`$,

```math
\boxed{\quad
\sup_{|{\widetilde\alpha}-\alpha|\le\delta/(8\beta)}
\left|\frac{\log N_f(\delta;{\widetilde\alpha})}{\log(1/\delta)}-1\right|
\longrightarrow0.
\quad}
\tag{16}
```
For a badly approximable nominal spectrum the stronger uniform bounds are

```math
\frac{c_1}{\delta\log(1/\delta)}
\lt N_f(\delta;{\widetilde\alpha})\le\frac{c_2}{\delta}.
\tag{17}
```
These statements permit a different actual $`{\widetilde\alpha}`$ at each $`\delta`$, including rational actual values. They are stronger than classifying the actual parameter as rational or irrational at one finite resolution: the relevant protection is its finite-scale proximity to one fixed Diophantine spectrum.

## 5. Harmonic resonance: an exact two-copy boundary

The corresponding calibration-uniform exponent-two statement is false around the harmonic spectrum. Fix $`0<\nu<1/\beta`$ and let

```math
{\widetilde\alpha}_\delta=2+\nu\delta,\qquad
x=e^{-\beta},\qquad
s=(1-\beta\nu)\delta,\qquad
Z_\delta=1+x+x^2e^s.
```
The matched state has populations $`(1,x,x^2e^s)/Z_\delta`$. When $`0\lt s<\beta`$ it is single-copy passive. In two copies, $`|02\rangle,|20\rangle`$ have energy $`{\widetilde\alpha}_\delta`$ and probability $`x^2e^s/Z_\delta^2`$, while $`|11\rangle`$ has energy $`2`$ and probability $`x^2/Z_\delta^2`$. This is the only inversion between the ordered energy sectors. Swapping $`|11\rangle`$ with either one of the two higher-energy basis states is therefore optimal, and gives the exact formula

```math
\boxed{\quad
W_2(\delta;{\widetilde\alpha}_\delta)
=\nu\delta\,\frac{x^2}{Z_\delta^2}
\left(e^{(1-\beta\nu)\delta}-1\right).
\quad}
\tag{18}
```
Let $`Z_0=1+x+x^2`$, $`\gamma_1=x/Z_0`$, and let $`R_2`$ be the residual variance at the harmonic Gibbs state. Then

```math
R_2=\frac{x^2}{Z_0(1+4x+x^2)},\qquad
\frac{\gamma_1^2}{R_2}=1+3\gamma_1.
```
Using the uniform normalization (3), (18) yields

```math
\lim_{\delta\downarrow0}
\frac{W_2(\delta;{\widetilde\alpha}_\delta)}{2w_\infty(\delta;{\widetilde\alpha}_\delta)}
=F_\nu:=\beta\nu(1-\beta\nu)(1+3\gamma_1)>0.
\tag{19}
```
Thus $`N_f(\delta;{\widetilde\alpha}_\delta)=2`$ for all sufficiently small $`\delta`$, whenever $`0\lt f\lt F_\nu`$. The equality follows because a single copy remains passive.

A concrete comparison uses exactly the radius from (6): choose $`\nu=1/(8\beta)`$. Then $`|{\widetilde\alpha}_\delta-2|=\delta/(8\beta)`$ and

```math
F_\nu=\frac7{64}(1+3\gamma_1)>\frac7{64}>\frac1{10}.
```
Consequently

```math
N_{1/10}(\delta;2+\delta/(8\beta))=2
```
for all sufficiently small $`\delta`$, whereas the fixed harmonic spectrum $`\alpha=2`$ has the exponent-two block-size law for the same fraction. This is a nonuniform spectral limit. It is not a claim that every nonzero detuning, every sign of detuning, or every vanishing detuning rate has this effect.

This comparison uses the fraction $`1/10`$, which is within the theorem's range $`0\lt f\le1/3`$; it does not assert a one-third yield within the radius $`\delta/(8\beta)`$. A one-third example is available with a wider radius of the same order: at $`\beta=1`$, choose $`\nu=1/2`$. Then $`{\widetilde\alpha}_\delta=2+\delta/2`$ and $`F_\nu=(1+3\gamma_1)/4=0.433546\ldots>1/3`$, so $`N_{1/3}(\delta;2+\delta/2)=2`$ for sufficiently small $`\delta`$.

## 6. Operational interpretation and limits

The generic exponent-one law tolerates an explicitly stated, polynomially shrinking spectral calibration window, with the state matched to each actual Hamiltonian. The rational theorem concerns a fixed commensurate spectrum; its denominator-dependent bound cannot be extended across the same calibration window without additional conditions. Known structural instability of passivity is relevant background, and the two-copy example is presented as a boundary of the theorem rather than as an independent discovery of activation.

All quantities here are mean work. In the generic strip construction $`s_{\widetilde\alpha}\to0`$, so the probabilities of positive and negative work events become close even though their difference gives a fixed fraction of the available mean work. None of (9), (16), or (19) is a claim about a deterministic work output or a reduction in the total number of samples needed for a reliable accumulated-work signal. Nor do these results bound the arity or implementation cost of physical gates realizing the permitted global permutation.

[Scientific guide](README.md) · [Repository overview](../README.md)
