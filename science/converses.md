# All-unitary bounds on the block size for useful work

This note proves the converse part of the mean-ergotropy block-size theorem. All logarithms are natural. The bounds concern arbitrary unitaries on the supplied copies, and do not assume that an optimal protocol is a collection of the swaps used for achievability.

## 1. Model and normalization

Fix $`\beta>0`$ and $`\alpha>1`$, and write

```math
H_\alpha=\mathrm{diag}(0,1,\alpha),\qquad
K=\mathrm{diag}(0,0,1),\qquad
\rho_\delta=\frac{e^{-\beta H_\alpha+\delta K}}{Z_\delta},
\qquad \delta>0.
```
The single-copy state is passive when $`\delta<\beta(\alpha-1)`$. On $`n`$ copies let $`H_\alpha^{(n)}=\sum_{j=1}^nH_{\alpha,j}`$, and define

```math
W_n(\delta;\alpha)
=\max_U\mathrm{Tr}\!\left[
H_\alpha^{(n)}(\rho_\delta^{\otimes n}
-U\rho_\delta^{\otimes n}U^\dagger)\right].
```
The maximization is over every unitary on the $`3^n`$-dimensional system. No auxiliary entropy sink, bath, catalyst, or discarded ancilla is supplied. Work denotes the mean system-energy decrease under cyclic driving. Block population $`n`$ is the resource in these statements; gate count, gate arity, duration, and work reliability are separate quantities.

Let $`\gamma_\beta=e^{-\beta H_\alpha}/Z_0`$, and evaluate the following covariances in $`\gamma_\beta`$:

```math
V=\mathrm{Var}(H_\alpha),\qquad
C=\mathrm{Cov}(H_\alpha,K),\qquad
R=\mathrm{Var}(K)-\frac{C^2}{V}>0.
```
If $`\gamma_\beta`$ has populations $`p_0,p_1,p_2`$, a useful explicit identity is

```math
V=p_0p_1+\alpha^2p_0p_2+(\alpha-1)^2p_1p_2,
\qquad R=\frac{p_0p_1p_2}{V}.
\tag{1}
```
Let $`\beta_*(\delta)`$ be the positive inverse temperature near $`\beta`$ for which $`\gamma_{\beta_*}`$ and $`\rho_\delta`$ have equal entropy, and put

```math
w_\infty(\delta;\alpha)
=\mathrm{Tr}H_\alpha(\rho_\delta-\gamma_{\beta_*}).
```
The usual asymptotic ergotropy theorem identifies this with $`\lim_{n\to\infty}W_n/n`$ at fixed $`\delta`$. The converse below only needs its quadratic expansion and its role as an upper bound. Both follow locally without an asymptotic interchange:

```math
\beta_*'(0)=-C/V,\qquad
w_\infty(\delta;\alpha)
=\frac{R}{2\beta}\delta^2+O(\delta^3).
\tag{2}
```
Indeed $`\partial_\beta S(\gamma_\beta)=-\beta V`$, whereas $`\partial_\delta S(\rho_\delta)|_0=\beta C`$. The difference between the first derivatives of the two population vectors is

```math
p_i\left[K_i-\mathbb E K-\frac{C}{V}(H_i-\mathbb E H)\right].
```
The second-order relative-entropy expansion is consequently $`D(\rho_\delta\Vert\gamma_{\beta_*})=R\delta^2/2+O(\delta^3)`$. Equal entropy gives the exact identity $`D=\beta_*w_\infty`$, proving (2). Applying the same relative-entropy identity after any $`n`$-copy unitary also gives $`W_n\le n w_\infty`$.

In particular, there is $`0<\delta_{\rm th}\le\beta(\alpha-1)/2`$, depending only on the fixed $`\alpha,\beta`$, such that

```math
w_\infty(\delta;\alpha)\ge m\delta^2,
\qquad m:=\frac{R}{4\beta},\qquad
0<\delta\le\delta_{\rm th}.
\tag{3}
```
For $`f>0`$, set

```math
N_f(\delta;\alpha)
=\min\{n\ge1:W_n(\delta;\alpha)\ge f n w_\infty(\delta;\alpha)\},
\tag{4}
```
with value $`+\infty`$ if the set is empty. The lower bounds apply to every fixed $`f>0`$; a matching upper bound for a specified range of fractions is supplied by the constructive theorem.

## 2. Two elementary lemmas

### Lemma 1: distance from any passive state bounds every unitary

If $`\sigma`$ is passive for a finite Hamiltonian $`H`$, then

```math
W_H(\rho)\le
(\lambda_{\max}(H)-\lambda_{\min}(H))\,\|\rho-\sigma\|_1.
\tag{5}
```
For any $`U`$, passivity gives $`\mathrm{Tr}H(\sigma-U\sigma U^\dagger)\le0`$. Thus its extracted work on $`\rho`$ is at most

```math
\mathrm{Tr}[(H-U^\dagger H U)(\rho-\sigma)]
\le \|H-U^\dagger HU\|_\infty\|\rho-\sigma\|_1.
```
The operator norm is bounded by the spectral diameter of $`H`$. Maximizing over $`U`$ proves (5). For the present Hamiltonian the diameter is $`n\alpha`$.

We use the standard passivity criterion: a density matrix diagonal in an energy eigenbasis is passive if its probabilities do not increase with increasing energy. This controls all unitaries because their population transition matrices $`(|U_{ij}|^2)`$ are doubly stochastic and the decreasing-probability/increasing-energy arrangement minimizes the energy. Probabilities within an exactly degenerate energy shell need not be equal.

The comparison state $`\sigma`$ may be correlated across the copies. It is only a mathematical witness in (5); the protocol is not supplied with it and is not required to prepare it.

### Lemma 2: normalization and binomial tails

For strictly positive vectors $`u,v`$, with $`Z_u=\sum_i u_i`$ and $`Z_v=\sum_i v_i`$,

```math
\left\|\frac{u}{Z_u}-\frac{v}{Z_v}\right\|_1
\le \frac{2}{Z_u}\|u-v\|_1.
\tag{6}
```
This follows by inserting $`v/Z_u`$ and using $`|Z_u-Z_v|\le\|u-v\|_1`$. In particular, if $`P`$ is already normalized, $`\|P-v/Z_v\|_1\le2\|P-v\|_1`$, without assuming that $`Z_v`$ is close to one in advance.

For $`X\sim\mathrm{Bin}(n,r)`$,

```math
\Pr\{|X-nr|>u\}\le2e^{-2u^2/n},\qquad u>0.
\tag{7}
```
For completeness, a centered Bernoulli variable has log moment-generating function $`\psi`$ with $`\psi(0)=\psi'(0)=0`$ and $`\psi''\le1/4`$. Hence $`\psi(\lambda)\le\lambda^2/8`$; independence and the Chernoff bound, optimized at $`|\lambda|=4u/n`$, give (7).

## 3. Rational spectrum: explicit clipped passive approximation

### Proposition 3

Let $`\alpha=a/b`$ in lowest terms, with integers $`a>b\ge1`$, and set

```math
B:=\frac{\beta}{4b},\qquad
c_{\rm rat}:=\frac{B^2}{2},\qquad
C_{\rm rat}:=4\alpha(1+e^B).
```
For every integer $`n\ge1`$ and $`\delta>0`$ such that $`n\delta^2\le2B`$,

```math
\boxed{\quad
\frac{W_n(\delta;\alpha)}{n}
\le C_{\rm rat}\exp\!\left[-\frac{c_{\rm rat}}{n\delta^2}\right].
\quad}
\tag{8}
```
This finite inequality does not require $`n`$-passivity of the original product state.

**Proof.** Label energy eigenvectors by microstates $`i`$. Write $`E_i`$ for their total energy, $`X_i`$ for their number of level-2 occupations, and $`G_i`$ for their probability under $`\gamma_\beta^{\otimes n}`$. If $`r=\gamma_\beta(2)`$, let

```math
F_i=\delta(X_i-nr),\qquad u_i=G_i e^{F_i},\qquad
v_i=G_i e^{\mathrm{clip}(F_i,-B,B)}.
```
Then $`P_i:=u_i/Z_u`$ is exactly the microstate probability under $`\rho_\delta^{\otimes n}`$. Every strictly positive total-energy difference is at least $`1/b`$. Consequently, for $`E_j>E_i`$,

```math
\log(v_j/v_i)
\le-\beta/b+2B=-\beta/(2b)<0.
```
Thus $`\sigma=\mathrm{diag}(v/Z_v)`$ is passive, including when energy degeneracies occur.

The vectors $`u,v`$ coincide outside

```math
A=\{|X-nr|>B/\delta\}.
```
Jensen's inequality gives $`Z_u=\mathbb E_G e^F\ge1`$. On $`A`$, $`v_i\le e^B G_i`$, so (6) yields

```math
\|P-v/Z_v\|_1
\le2\Pr_P(A)+2e^B\Pr_G(A).
\tag{9}
```
Under $`P`$, $`X`$ is binomial with success probability

```math
r_\delta=\frac{re^\delta}{1-r+re^\delta}.
```
Since $`\frac{d}{d\delta}r_\delta=r_\delta(1-r_\delta)\le1/4`$, one has $`n|r_\delta-r|\le n\delta/4`$. The assumed regime gives

```math
n|r_\delta-r|\le B/(2\delta).
```
Applying (7) under both distributions therefore gives

```math
\Pr_P(A)\le2e^{-B^2/(2n\delta^2)},\qquad
\Pr_G(A)\le2e^{-2B^2/(n\delta^2)}.
```
In particular,

```math
\|P-v/Z_v\|_1
\le4(1+e^B)e^{-B^2/(2n\delta^2)}.
\tag{10}
```
Combining (10) with Lemma 1 proves (8). No uncontrolled partition-function or normalization factor has been omitted. $`\square`$

### Corollary 4: minimum block size for a fixed fraction

Define

```math
A_{\rm rat}:=\frac{c_{\rm rat}}3
=\frac{\beta^2}{96b^2}.
```
For each fixed $`f>0`$, all sufficiently small $`\delta`$ satisfy

```math
\boxed{\quad
N_f(\delta;\alpha)>
\frac{A_{\rm rat}}{\delta^2\log(1/\delta)}.
\quad}
\tag{11}
```
One explicit sufficient smallness regime, in terms of (3), is

```math
0<\delta\le\min\left\{
\delta_{\rm th},\ e^{-\max\{1,B/12\}},
\frac{fm}{2C_{\rm rat}}
\right\}.
\tag{12}
```
Indeed every integer $`n\le A_{\rm rat}/[\delta^2\log(1/\delta)]`$ obeys the regime of Proposition 3, and its extracted fraction is at most

```math
\frac{C_{\rm rat}}{m\delta^2}\,
e^{-3\log(1/\delta)}
=\frac{C_{\rm rat}}m\delta\le f/2.
```
This proves a bound on the minimum over **all** block sizes in the indicated interval; no monotonicity of $`W_n/n`$ is assumed. In particular the lower logarithmic exponent is two. A constructive $`N_f=O(\delta^{-2})`$ bound gives equality of the logarithmic exponent for every fraction covered by that construction.

## 4. Irrational spectrum: an ordered typical subset

Fix $`\mu\ge2`$ and $`\kappa>0`$, and assume

```math
\left|\alpha-\frac pq\right|\ge\frac{\kappa}{q^\mu}
\quad\text{for every }p\in\mathbb Z,\ q\in\mathbb N.
\tag{13}
```
The case $`\mu=2`$ is the badly-approximable condition. For an irrational of irrationality exponent two, (13) holds for every $`\mu=2+\eta`$, with a constant $`\kappa_\eta>0`$ that can depend on $`\eta`$.

### Lemma 5: passive extension without changing the selected probabilities

Suppose a set $`T`$ of energy eigenvectors has no probability/energy inversion: selected probabilities are nonincreasing with their energies. Order the entire eigenbasis by increasing energy, choosing the ordering within degenerate shells so that the selected probabilities are nonincreasing. For the present tilted product distribution put

```math
g_i=\frac{e^{-\beta E_i}}{Z_\delta^n},\qquad
P_i=g_i e^{\delta X_i},
```
and define the positive, not yet normalized vector

```math
v_i=\min\left\{e^{n\delta}g_i,
\inf_{\substack{j\in T\\j\le i}}P_j\right\},
\tag{14}
```
where an empty infimum is $`+\infty`$. Then $`v`$ is nonincreasing, $`v_i=P_i`$ for every $`i\in T`$, and

```math
g_i\le v_i\le e^{n\delta}g_i\quad\text{for every }i.
\tag{15}
```
Both sequences in the minimum in (14) are nonincreasing. At a selected index the infimum equals $`P_i`$, and the other entry is at least $`P_i`$. Moreover, for any selected $`j\le i`$, $`P_j\ge g_j\ge g_i`$, which proves the lower bound in (15). This verifies every assertion, including before the first selected index and inside degenerate shells.

Since both $`P_i,v_i`$ lie between $`g_i`$ and $`e^{n\delta}g_i`$,

```math
|P_i-v_i|\le(e^{n\delta}-1)g_i
\le(e^{n\delta}-1)P_i.
```
Together with agreement on $`T`$, normalization (6) therefore gives

```math
\boxed{\quad
\left\|P-\frac{v}{\sum_jv_j}\right\|_1
\le2(e^{n\delta}-1)\Pr_P(T^c).
\quad}
\tag{16}
```
The normalized vector is passive. Its normalization has not been assumed to preserve the selected values; equality on $`T`$ is used **before** normalization, and (16) bounds the full change after normalization.

### Proposition 6: finite all-unitary bound

Define

```math
t_\mu(\delta)
=\left(\frac{\beta\kappa}{2^{\mu+1}\delta}\right)^{1/\mu},\qquad
d_\mu=2\left(\frac{\beta\kappa}{2^{\mu+1}}\right)^{2/\mu}.
```
For every $`n\ge1`$ and $`\delta>0`$,

```math
\boxed{\quad
\frac{W_n(\delta;\alpha)}n
\le4\alpha(e^{n\delta}-1)
\exp\!\left[-\frac{d_\mu}{n\delta^{2/\mu}}\right].
\quad}
\tag{17}
```
In particular, when $`n\delta\le1`$, the prefactor is at most $`C_{\rm irr}:=4\alpha(e-1)`$.

**Proof.** Under $`P`$, the count $`X`$ is binomial with mean $`nr_\delta`$. Select

```math
T=\{|X-nr_\delta|\le t_\mu(\delta)\}.
```
For two selected microstates let $`q`$ be their difference in $`X`$, and $`\ell`$ their difference in level-1 count. If $`q=0`$, their logarithmic probability difference is exactly minus $`\beta`$ times their energy difference. Otherwise $`|q|\le2t_\mu`$, and (13) implies

```math
|\ell+\alpha q|\ge\frac{\kappa}{|q|^{\mu-1}},\qquad
\delta|q|^\mu\le\frac{\beta\kappa}{2}.
```
Hence

```math
\beta|\ell+\alpha q|>\delta|q|.
\tag{18}
```
The sign of $`-\beta(\ell+\alpha q)+\delta q`$ is opposite to that of the energy difference. The selected spectrum has no inversion. Lemma 5 applies, while (7) gives

```math
\Pr_P(T^c)\le2e^{-2t_\mu(\delta)^2/n}
=2e^{-d_\mu/(n\delta^{2/\mu})}.
```
Lemma 1 and (16) prove (17). The argument is valid even if $`T`$ covers every possible count, in which case the state itself is passive and its work is zero. $`\square`$

### Corollary 7: block-size exponents

Let $`A_\mu=d_\mu/3`$. For every fixed $`f>0`$, all sufficiently small $`\delta`$ satisfy

```math
\boxed{\quad
N_f(\delta;\alpha)>
\frac{A_\mu}{\delta^{2/\mu}\log(1/\delta)}.
\quad}
\tag{19}
```
A sufficient regime is

```math
0<\delta\le\min\left\{
\delta_{\rm th},\ e^{-\max\{1,A_\mu\}},
\frac{fm}{2C_{\rm irr}}
\right\}.
\tag{20}
```
For the block sizes in (19),

```math
n\delta\le\frac{A_\mu\delta^{1-2/\mu}}{\log(1/\delta)}\le1,
```
and (17), divided by (3), bounds the extracted fraction by $`(C_{\rm irr}/m)\delta\le f/2`$. As in the rational proof, this is uniform over every smaller integer block size.

For a badly approximable spectrum, $`\mu=2`$ gives

```math
A_2=\frac{\beta\kappa}{12},\qquad
N_f(\delta;\alpha)>
\frac{\beta\kappa}{12\delta\log(1/\delta)}.
\tag{21}
```
For an irrationality-exponent-two spectrum, applying (19) separately for each $`\eta>0`$ yields

```math
\liminf_{\delta\downarrow0}
\frac{\log N_f(\delta;\alpha)}{\log(1/\delta)}
\ge\frac{2}{2+\eta}.
```
Taking the supremum over $`\eta>0`$ gives a lower logarithmic exponent of one. Combining this with a fixed-fraction constructive bound $`N_f\le C_\varepsilon\delta^{-1-2\varepsilon}`$, valid for every $`\varepsilon>0`$ with the **same allowed fraction** $`f`$, proves exponent one. No constant $`\kappa_\eta`$ uniform in $`\eta`$ is required, and the limits in $`\eta`$ and $`\delta`$ are not interchanged.

## 5. Scope of the converse

The fixed-spectrum statements keep $`\alpha`$ fixed before $`\delta`$ tends to zero. The rational constant depends on its denominator $`b`$; a sequence of rational numbers with growing denominators is not covered uniformly by the rational exponent-two statement. The irrational constants likewise refer to a fixed nominal spectrum. A controlled, uniform extension to an $`O(\delta)`$ neighborhood of a fixed Diophantine spectrum is proved in [calibration analysis](calibration.md).

The logarithm in (11), (19), and (21) comes from converting an exponentially small distance to a passive state into a bound relative to $`w_\infty=\Theta(\delta^2)`$. These proofs establish the logarithmic exponent and the displayed finite inequalities. They do not establish a sharp crossover constant or remove that logarithmic gap.

[Scientific guide](README.md) · [Repository overview](../README.md)
