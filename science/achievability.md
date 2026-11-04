# A finite work fraction from typical occupation classes

This note proves the constructive bounds for the near-equilibrium qutrit model. In particular, the common target fraction can be chosen to be **one third**, for every fixed inverse temperature and every spectrum covered by the corresponding theorem. The proof does not rely on a numerical estimate of an unspecified small constant.

The charged resource is the number of copies processed in one joint batch. An arbitrary predetermined cyclic unitary on that batch is allowed. No bath, catalyst, refreshed ancilla, postselection, or measurement record is introduced. The construction is a permutation of energy eigenstates, and work denotes its mean energy decrease. No claim about efficient circuit synthesis, physical gate arity, controller cost, or reliable single-run work follows from the bounds below.

Occupation-class transport and finite-fraction collective work extraction are established methods; a close source is [Perarnau-Llobet and Uzdin, *New Journal of Physics* **21**, 083023 (2019)](https://arxiv.org/abs/1810.02237). The contribution proved here is the specified joint-limit batch-size bound, including its explicit fraction, rather than the general use of permutations or typical types.

## 1. Model and normalization

Fix $`\beta>0`$ and $`\alpha>1`$, and write

```math
H_\alpha=\mathrm{diag}(0,1,\alpha),\qquad
K=\mathrm{diag}(0,0,1),\qquad
\rho_\delta=\frac{e^{-\beta H_\alpha+\delta K}}{Z_\delta},
\qquad \delta\downarrow0.
```
The three populations are denoted by $`p_{i,\delta}`$, $`i=0,1,2`$. Their limit is the full-rank Gibbs vector $`p_i=e^{-\beta E_i}/Z_0`$. The single-copy state is passive when $`0<\delta<\beta(\alpha-1)`$.

Let $`W_n(\delta;\alpha)`$ be the maximum mean energy decrease under a unitary on $`\rho_\delta^{\otimes n}`$. Let $`w_\infty(\delta;\alpha)`$ denote the energy difference from the Gibbs state with the same entropy. Its identification with the asymptotic ergotropy density is inherited from [Alicki and Fannes, *Physical Review E* **87**, 042123 (2013)](https://arxiv.org/abs/1211.1209). Define

```math
V=\mathrm{Var}_{p}(H_\alpha),\qquad
C=\mathrm{Cov}_{p}(H_\alpha,K),\qquad
R=\mathrm{Var}_{p}(K)-\frac{C^2}{V}>0.
```
The normalization used below is

```math
w_\infty(\delta;\alpha)
=\frac{R}{2\beta}\delta^2+O(\delta^3).
\tag{1}
```
For completeness, the equal-entropy inverse temperature satisfies $`\beta_*'(0)=-C/V`$: the entropy derivatives in the population-tilt and temperature directions are $`\beta C`$ and $`-\beta V`$, respectively. The relative-entropy identity

```math
D(\rho_\delta\Vert\gamma_{\beta_*(\delta)})
=\beta_*(\delta)\,w_\infty(\delta;\alpha)
```
and its second-order Taylor expansion give (1). Positivity of $`R`$ follows because $`K`$ is not affine in $`H_\alpha`$ on the three occupied levels.

Write

```math
N_f(\delta;\alpha)
=\min\{n\ge1: W_n(\delta;\alpha)\ge f n w_\infty(\delta;\alpha)\}.
```
The constructive conclusions proved here are:

1. If $`\alpha=a/b`$ is a fixed reduced rational, then $`N_{1/3}(\delta;\alpha)=O(\delta^{-2})`$.
2. If, for every $`\eta>0`$, there is $`\kappa_\eta>0`$ such that
   ```math
   \left|\alpha-\frac p q\right|\ge\frac{\kappa_\eta}{q^{2+\eta}}
   \quad(p\in\mathbb Z,\ q\ge1),
   \tag{2}
   ```
   then $`N_{1/3}(\delta;\alpha)=O_\epsilon(\delta^{-1-2\epsilon})`$ for every $`\epsilon\in(0,1/2)`$.
3. If $`\alpha`$ is badly approximable, so (2) holds with exponent exactly two and a fixed $`\kappa>0`$, then $`N_{1/3}(\delta;\alpha)=O(\delta^{-1})`$.

All constants and sufficiently-small-$`\delta`$ thresholds may depend on the fixed spectrum and temperature. Condition (2) holds for Lebesgue-almost-every fixed $`\alpha`$. When combined with the separate all-unitary converses, these bounds give minimum-batch exponents two and one, respectively. The converse is not inferred from the particular permutation used here.

## 2. Exact finite type matching

A type is an occupation vector $`k=(k_0,k_1,k_2)`$ with nonnegative integer entries summing to $`n`$. Its energy, multiplicity, probability per microstate, and total type probability are

```math
E(k)=k_1+\alpha k_2,\qquad
g_n(k)=\frac{n!}{k_0!k_1!k_2!},\qquad
P_n(k)=\prod_{i=0}^2p_{i,\delta}^{k_i},\qquad
\mu_n(k)=g_n(k)P_n(k).
```
Given integers $`p,q>0`$, set

```math
\Delta=(p-q,-p,q),\qquad
h=\alpha q-p,\qquad
s=\delta q-\beta h.
\tag{3}
```
Whenever both types are valid,

```math
E(k+\Delta)-E(k)=h,
\qquad
\frac{P_n(k+\Delta)}{P_n(k)}=e^s.
\tag{4}
```

### Lemma 1. Exact paired work

Suppose $`h>0`$ and $`s>0`$. Let $`\mathcal A`$ be any collection of types such that $`\mathcal A\cap(\mathcal A+\Delta)=\varnothing`$. There is a predetermined permutation unitary whose extracted mean work is exactly

```math
W(\mathcal A)
=h(e^s-1)\,
\sum_{k\in\mathcal A}
\min\{\mu_n(k),e^{-s}\mu_n(k+\Delta)\}.
\tag{5}
```
An invalid shifted type is assigned probability zero in this expression.

**Proof.** For every valid pair $`k,k+\Delta`$, pair and exchange $`\min\{g_n(k),g_n(k+\Delta)\}`$ distinct microstates from the two type classes. Source and target classes are disjoint, and translation is injective, so no microstate participates in two exchanges. Complete the permutation by the identity on all unused microstates. Every paired exchange lowers the mean energy by

```math
h\,[P_n(k+\Delta)-P_n(k)]
=h(e^s-1)P_n(k).
```
Finally,

```math
P_n(k)\min\{g_n(k),g_n(k+\Delta)\}
=\min\{\mu_n(k),e^{-s}\mu_n(k+\Delta)\}.
```
This proves (5). The labels of the types are used to define a linear operator; they are not measured or stored in an additional register. $`\square`$

## 3. A uniform Gaussian limit for the matched mass

The following lemma converts (5) into an explicit, nonvanishing work fraction. It also permits a nominal rather than actual probability vector to define the permutation.

Use two coordinates $`k=(k_1,k_2)`$, with $`k_0=n-k_1-k_2`$. For an interior probability vector $`p=(p_0,p_1,p_2)`$, let

```math
\Sigma(p)
=\begin{pmatrix}
p_1(1-p_1)&-p_1p_2\\
-p_1p_2&p_2(1-p_2)
\end{pmatrix}.
\tag{6}
```
This covariance is positive definite and has determinant $`p_0p_1p_2`$.

### Lemma 2. Gaussian strip limit

Consider any sequence of multinomial type distributions $`\mu_n`$ with probabilities $`p^{(n)}\to p`$, where every component of $`p`$ is positive. Let integer shifts $`d_n\in\mathbb Z^2`$, symmetric positive definite matrices $`G_n`$, centers $`c_n\in\mathbb R^2`$, and scores $`s_n`$ satisfy

```math
\frac{d_n}{\sqrt n}\longrightarrow v\ne0,
\qquad
G_n\longrightarrow\Sigma(p)^{-1},
\qquad
\frac{c_n-n(p^{(n)}_1,p^{(n)}_2)}{\sqrt n}\longrightarrow0,
\qquad
s_n\longrightarrow s\ge0.
\tag{7}
```
Define

```math
A_n=\sqrt{\frac{d_n^TG_nd_n}{n}},\qquad
Y_n(k)=\frac{d_n^TG_n(k-c_n)}{\sqrt n\sqrt{d_n^TG_nd_n}},
```
and select the half-open strip

```math
\mathcal A_n=\{k:\ -A_n\le Y_n(k)<0\}.
\tag{8}
```
Only valid multinomial types contribute to sums; invalid shifted types again have probability zero. Put

```math
A=\sqrt{v^T\Sigma(p)^{-1}v}>0.
```
Then $`\mathcal A_n\cap(\mathcal A_n+d_n)=\varnothing`$, and

```math
\sum_{k\in\mathcal A_n}
\min\{\mu_n(k),e^{-s_n}\mu_n(k+d_n)\}
\longrightarrow
M_s(A):=\int_{-A}^{0}\min\{\phi(x),e^{-s}\phi(x+A)\}\,dx,
\tag{9}
```
where $`\phi(x)=(2\pi)^{-1/2}e^{-x^2/2}`$.

The convergence holds uniformly over families for which the limits in (7) are uniform, the limiting probabilities stay in a compact subset of the open simplex, and the limiting nonzero shifts stay in a compact set bounded away from zero.

**Proof.** First, $`Y_n(k+d_n)=Y_n(k)+A_n`$. Hence the selected and translated strips lie in $`[-A_n,0)`$ and $`[0,A_n)`$, respectively, and are exactly disjoint.

We give the local limit argument explicitly to identify its uniformity. On every fixed bounded set of

```math
z=\frac{k-n(p^{(n)}_1,p^{(n)}_2)}{\sqrt n},
```
Stirling's formula and the Taylor expansion of the multinomial relative entropy give, uniformly there,

```math
\mu_n(k)
=\frac1n\,\varphi_{\Sigma(p)}(z)\,[1+o(1)],
\tag{10}
```
where $`\varphi_\Sigma`$ is the centered two-dimensional normal density. To see the quadratic form directly, set $`z_0=-z_1-z_2`$. The exponent is

```math
-\frac12\sum_{i=0}^2\frac{z_i^2}{p_i}+o(1)
=-\frac12z^T\Sigma(p)^{-1}z+o(1),
```
and the prefactor is $`(2\pi n\sqrt{p_0p_1p_2})^{-1}[1+o(1)]`$. For a probability vector bounded away from the simplex boundary, the Taylor and Stirling remainders are uniform on each bounded set. The same statement applies to the shifted type because $`d_n/\sqrt n`$ is bounded.

Using (10), the sum in (9), restricted to a bounded region, is a Riemann sum for

```math
\int_{\mathcal S}
\min\{\varphi_\Sigma(z),e^{-s}\varphi_\Sigma(z+v)\}\,dz,
```
where

```math
\mathcal S=
\left\{z:\ -A\le\frac{v^T\Sigma^{-1}z}{A}<0\right\}.
```
The boundary of this strip has zero Gaussian measure. The contribution outside a radius-$`L`$ region is at most the original multinomial tail, because the minimum in (9) is at most $`\mu_n(k)`$. Its probability is bounded uniformly by $`\mathrm{tr}\Sigma(p^{(n)})/L^2`$. Thus the region can be enlarged after taking the local limit; invalid type boundaries are at distance of order $`\sqrt n`$ in the standardized coordinates and cause no extra term.

Finally whiten the coordinates by $`x=\Sigma^{-1/2}z`$, and choose the first coordinate in the direction $`\Sigma^{-1/2}v/A`$. The shift is $`A`$ in that coordinate and zero in the orthogonal one. The Gaussian density factors, the latter coordinate integrates to one, and the integral becomes exactly $`M_s(A)`$. The same bounded-region and tail argument proves the stated uniformity. $`\square`$

For later use, the two Gaussian densities cross at

```math
x_*=-\frac A2-\frac s A.
```
Consequently

```math
M_s(A)=
\begin{cases}
\Phi(x_*)-\Phi(-A)+e^{-s}[\Phi(A)-\Phi(x_*+A)],
&0\le s\lt A^2/2,\\[2mm]
e^{-s}[\Phi(A)-1/2],&s\ge A^2/2,
\end{cases}
\tag{11}
```
where $`\Phi`$ is the standard normal distribution function. In particular,

```math
M_0(A)=2[\Phi(A)-\Phi(A/2)]>0.
\tag{12}
```

## 4. The qutrit tangent direction fixes the batch scale

The occupation shift in (3), divided by $`q`$, tends to

```math
d=(\alpha-1,-\alpha,1)
```
whenever $`p/q\to\alpha`$. Its two-coordinate representation is $`v_0=(-\alpha,1)`$. An elementary covariance identity gives

```math
v_0^T\Sigma(p)^{-1}v_0
=\frac{(\alpha-1)^2}{p_0}+\frac{\alpha^2}{p_1}+\frac1{p_2}
=\frac1R.
\tag{13}
```
For example, $`V=p_0p_1+\alpha^2p_0p_2+(\alpha-1)^2p_1p_2`$ and $`R=p_0p_1p_2/V`$, which verify (13) directly.

Thus, for any fixed strip parameter $`A>0`$, choosing

```math
n=\left\lceil\frac{q^2}{A^2R}\right\rceil
\tag{14}
```
and using $`G_n=\Sigma(p)^{-1}`$ and the actual mean as center produces the limiting strip width $`A`$ in Lemma 2. A center differing from the actual mean by $`o(\sqrt n)`$, or a convergent nominal metric, gives the same limit.

## 5. Rational spectra: a uniform one-third fraction

Let $`\alpha=a/b`$ with coprime positive integers $`a>b`$, and write

```math
u=\frac\beta b>0.
```
Choose $`q=q_\delta`$ to be the first positive integer satisfying

```math
aq\equiv1\pmod b,
\qquad q\ge\frac{2u}{\delta},
```
and set $`p=(aq-1)/b`$. Then

```math
h=\frac1b,
\qquad
\delta q=2u+O(\delta),
\qquad
s=u+O(\delta)>0.
\tag{15}
```
The constants in the $`O(\delta)`$ terms depend only on $`b`$. In particular, $`q<2u/\delta+b`$.

Choose $`n`$ by (14) and the Gaussian strip of Lemma 2. Equations (1), (5), and (9) show that the constructed work satisfies

```math
\frac{W(\mathcal A_n)}{n w_\infty}
\longrightarrow
F(u,A):=\frac{A^2(e^u-1)}{2u}\,M_u(A).
\tag{16}
```
This is a finite positive limit for every fixed $`u,A>0`$. The following choices give a uniform lower bound exceeding one third:

```math
A=
\begin{cases}
5/2,&0\lt u\le2,\\
\sqrt{2u},&u\ge2.
\end{cases}
\tag{17}
```
Either choice is admissible at $`u=2`$.

### The range $`0\lt u\le2`$

Put $`c=(1-e^{-2})/2>0.43`$. Since

```math
\frac{e^u-1}{u}\ge1,
\qquad
\frac{1-e^{-u}}u\ge c,
```
formula (16), with $`A=5/2`$, implies

```math
F(u,5/2)
\ge\frac{25}{8}\int_{-5/2}^{0}
\min\{\phi(x),c\phi(x+5/2)\}\,dx.
\tag{18}
```
On $`[-5/2,-8/5]`$, the minimum is $`\phi(x)`$, because $`e^{-7/8}<0.43\lt c`$. On $`[-3/2,0]`$, it is $`c\phi(x+5/2)`$, because $`e^{-5/8}>1/2>c`$. Retaining just these two disjoint intervals gives

```math
F(u,5/2)
\ge\frac{25}{8}\left[
\Phi(5/2)-\Phi(8/5)
+c\{\Phi(5/2)-\Phi(1)\}\right].
\tag{19}
```
The elementary bounds

```math
\Phi(5/2)>0.992,\qquad
\Phi(8/5)<0.947,\qquad
\Phi(1)<0.843
\tag{20}
```
therefore imply

```math
F(u,5/2)
>\frac{25}{8}\,[0.045+0.43\times0.149]
=0.34084375>\frac13.
\tag{21}
```
The inequalities in (20) do not require an empirical normal table; elementary certificates are provided in Section 9.

### The range $`u\ge2`$

With $`A=\sqrt{2u}`$, the second branch of (11) applies at equality. Hence

```math
F(u,\sqrt{2u})
=(1-e^{-u})[\Phi(\sqrt{2u})-1/2]
\ge(1-e^{-2})[\Phi(2)-1/2]
>0.40592>\frac13.
\tag{22}
```
Here we used $`e^{-2}<0.14`$ and $`\Phi(2)>0.972`$.

### Rational conclusion

For every fixed $`\beta>0`$ and reduced rational $`\alpha=a/b>1`$, the constructed fraction has a limiting lower bound strictly exceeding one third. Therefore, for all sufficiently small $`\delta`$,

```math
W_n(\delta;\alpha)\ge\frac13 n w_\infty(\delta;\alpha)
```
at the explicitly selected batch size

```math
n=\left\lceil\frac{q_\delta^2}{A^2R}\right\rceil
\le\left\lceil\frac{(2\beta/(b\delta)+b)^2}{A^2R}\right\rceil.
\tag{23}
```
This proves $`N_{1/3}(\delta;\alpha)=O(\delta^{-2})`$. The bound is constructive but is not asserted to optimize the finite prefactor.

## 6. Useful rational approximants

For an irrational spectrum it is not enough to find an exceptionally accurate rational approximation. We require the approximation error to lie inside a specified interval of width proportional to $`\delta`$, so that both the energy gain and the population advantage contribute at the required order.

### Lemma 3. An approximation inside a prescribed small interval

Fix an irrational $`\alpha`$, numbers $`0<\theta_-<\theta_+`$, and write $`L=\theta_+-\theta_-`$. Suppose

```math
\left|\alpha-\frac p q\right|\ge\frac\kappa{q^\mu}
\quad\text{for all }p\in\mathbb Z,\ q\ge1,
\tag{24}
```
where $`\mu\ge2`$. If the interval

```math
I_\delta=[\alpha-\theta_+\delta,\alpha-\theta_-\delta]
```
contains no reduced fraction with denominator at most $`Q`$, then, for all sufficiently small $`\delta`$,

```math
L\delta\le
2\left[\frac{2(1+\theta_+/L)}\kappa\right]^{1/(\mu-1)}
Q^{-\mu/(\mu-1)}.
\tag{25}
```
**Proof.** Translate by $`\lfloor\alpha\rfloor`$, so that the interval lies inside $`(0,1)`$ for small $`\delta`$. If it contains no order-$`Q`$ Farey fraction, it lies in one gap between adjacent such fractions. Let their denominators be $`b,d`$. The elementary Farey-neighbor identities are

```math
\Delta_F=\frac1{bd},\qquad b+d>Q.
```
Write $`b=\min(b,d)`$, relabeling the endpoints if needed; thus $`d>Q/2`$. Since the whole interval lies in the gap,

```math
\Delta_F\ge L\delta.
```
The distance from $`\alpha`$ to the endpoint of denominator $`b`$ is at most

```math
\Delta_F+\theta_+\delta
\le(1+\theta_+/L)\Delta_F
\le\frac{2(1+\theta_+/L)}{bQ}.
```
Combining this with (24) gives

```math
b\ge\left[\frac{\kappa Q}{2(1+\theta_+/L)}\right]^{1/(\mu-1)}.
```
Substitution into $`\Delta_F\le2/(bQ)`$ proves (25). If an endpoint of the desired interval is itself a Farey fraction, the required approximation already exists and the empty-gap alternative does not arise. $`\square`$

### Consequence for condition (2)

Fix $`\epsilon\in(0,1/2)`$ and set

```math
Q=\left\lfloor\delta^{-1/2-\epsilon}\right\rfloor.
\tag{26}
```
Apply Lemma 3 with $`\mu=2+\eta`$, choosing $`\eta>0`$ so small that

```math
(1/2+\epsilon)\frac{2+\eta}{1+\eta}>1.
```
For example, $`\eta=\epsilon`$ suffices. The right side of (25) is then $`o(\delta)`$, a contradiction. Hence every interval with fixed $`0<\theta_-<\theta_+`$ contains a fraction of denominator at most (26), for all sufficiently small $`\delta`$.

### Consequence for badly approximable spectra

Take $`\mu=2`$, $`\theta_-=1/(4\beta)`$, and $`\theta_+=3/(4\beta)`$. Formula (25) reads

```math
\frac{\delta}{2\beta}\le\frac{10}{\kappa Q^2}
```
if the interval is empty. Choosing

```math
Q=\left\lceil\sqrt{\frac{40\beta}{\kappa\delta}}\right\rceil
\tag{27}
```
contradicts this inequality. Thus a useful approximation is available with $`q=O(\delta^{-1/2})`$, with an explicit denominator bound.

## 7. Generic irrational spectra: more than one third at exponent one

Choose $`p/q`$ in the interval furnished by Lemma 3 with

```math
r_\delta:=\frac{\alpha-p/q}{\delta}
\in\left[\frac1{4\beta},\frac3{4\beta}\right].
\tag{28}
```
Then

```math
h=\delta q r_\delta,
\qquad
s=\delta q(1-\beta r_\delta),
\qquad
hs\ge\frac{3}{16\beta}\delta^2q^2.
\tag{29}
```
The denominator tends to infinity, since a fixed irrational cannot be approached by a bounded collection of denominators as $`\delta\to0`$. Under (26) or (27), $`\delta q\to0`$, so $`s\to0`$.

Choose the strip parameter $`A=2`$ and

```math
n=\left\lceil\frac{q^2}{4R}\right\rceil.
\tag{30}
```
Lemma 2 gives paired mass $`M_0(2)+o(1)`$. Since $`(e^s-1)/s\to1`$, equations (1), (5), and (29) give

```math
\begin{aligned}
\frac{W(\mathcal A_n)}{n w_\infty}
&= 2\beta A^2 r_\delta(1-\beta r_\delta)\,M_0(A)+o(1)\\
&\ge\frac38 A^2 M_0(A)+o(1)\\
&=3[\Phi(2)-\Phi(1)]+o(1)\\
&=0.4077153659\ldots+o(1).
\end{aligned}
\tag{31}
```
The remainder is uniform over the interval (28); convergence of $`r_\delta`$ itself is unnecessary. In particular, the lower bound is eventually larger than one third.

If (2) holds, then (26) and (30) prove

```math
N_{1/3}(\delta;\alpha)
\le\left\lceil\frac{\lfloor\delta^{-1/2-\epsilon}\rfloor^2}{4R}\right\rceil
=O_\epsilon(\delta^{-1-2\epsilon})
\tag{32}
```
for every fixed $`\epsilon\in(0,1/2)`$. The yield fraction is independent of $`\epsilon`$; only the sufficiently-small-$`\delta`$ threshold and approximation constants can deteriorate.

For a badly approximable spectrum, the explicit bound (27) instead gives

```math
N_{1/3}(\delta;\alpha)
\le\left\lceil\frac1{4R}
\left\lceil\sqrt{\frac{40\beta}{\kappa\delta}}\right\rceil^2\right\rceil
=O(\delta^{-1}).
\tag{33}
```

### Why the condition covers almost every fixed spectrum

For fixed $`\eta>0`$ and $`\alpha`$ restricted to a bounded interval, the total length of intervals of radius $`q^{-2-\eta}`$ about denominator-$`q`$ rationals is $`O(q^{-1-\eta})`$. Its sum over $`q`$ is finite. Borel--Cantelli therefore implies that almost every $`\alpha`$ has only finitely many approximations violating the lower bound with coefficient one. Reducing the coefficient to the positive minimum over those finitely many exceptions yields some $`\kappa_\eta>0`$. Intersecting these full-measure sets over a countable sequence $`\eta\downarrow0`$ gives (2). Rationals themselves form a null set and are excluded here.

This is the usual full-measure class of irrationals of irrationality exponent two. The construction does not assert a uniform onset threshold across all members of that class or a result for every irrational number.

## 8. Interface with nominal calibration and preparation

Lemma 2 is deliberately formulated with a nominal center and metric. For example, suppose a nominal spectrum $`\alpha`$ is used to choose the numerator, denominator, batch size, strip, and the ordering of microstates within each type. Let the actual spectrum be $`\alpha'`$ and its actual input be the matched Gibbs tilt $`\rho_\delta(\alpha')`$.

If the nominal useful-approximation interval is narrowed to

```math
\frac{\alpha-p/q}{\delta}
\in\left[\frac{3}{8\beta},\frac{5}{8\beta}\right],
```
then $`|\alpha'-\alpha|\le\delta/(8\beta)`$ keeps the actual slope inside (28). Smoothness of the populations gives a displacement of the actual mean from the nominal one of order $`n\delta`$. Relative to the $`\sqrt n`$ scale this is $`O(\delta q)`$, which tends to zero in the irrational construction. The actual covariance and nominal metric converge to the same limit. Consequently the exact same permutation has the uniform limiting paired mass in (31).

The permutation really is the same: the selected type classes are determined using nominal quantities, and $`\min\{g_n(k),g_n(k+\Delta)\}`$ and the chosen microstate ordering depend only on integer type counts, not on the actual populations. The likelihood score and resulting work are evaluated for the actual state after the permutation is fixed.

The [calibration analysis](calibration.md) specifies the full uncertainty model and its converse. This interface does not establish robustness against arbitrary correlated preparation errors, an unknown independent population tilt, or an $`O(\delta)`$ neighborhood of a rational-spectrum lower bound. The last claim would be false: detunings proportional to $`\delta`$ can change the rational onset nonuniformly.

## 9. Elementary certificates for the numerical constants

The proof only needs coarse strict bounds, not the decimal evaluation in (31).

- The normalizing factor satisfies $`(2\pi)^{-1/2}<0.399`$.
- For $`x>0`$, integration by parts gives the elementary Mills upper bound $`1-\Phi(x)<\phi(x)/x`$. Since $`e^{-2}<0.14`$, this yields $`\Phi(2)>1-0.4\times0.14/2=0.972`$.
- Likewise $`e^{-25/8}\lt e^{-3}<0.05`$ gives $`\Phi(5/2)>1-0.4\times0.05/(5/2)=0.992`$.
- The inequality $`e^{-z}\le1-z+z^2/2`$, for $`z\ge0`$, gives
  ```math
  \int_0^1e^{-t^2/2}\,dt\le1-\frac16+\frac1{40}=\frac{103}{120},
  ```
  and hence $`\Phi(1)<1/2+0.399(103/120)<0.843`$.
- The fourth-order upper Taylor polynomial gives
  ```math
  \int_0^{8/5}e^{-t^2/2}\,dt
  \le x-\frac{x^3}{6}+\frac{x^5}{40}-\frac{x^7}{336}+\frac{x^9}{3456}
  \bigg|_{x=8/5}<\frac{28}{25}.
  ```
  Therefore $`\Phi(8/5)<1/2+0.399(28/25)=0.94688<0.947`$.

The exponential estimates used here and in (18)--(22) follow directly from the exponential series; in particular $`e^{-7/8}<0.43`$, $`e^{-5/8}>1/2`$, and $`e^{-2}<0.14`$. Thus (21) and (22) are analytic lower bounds. Similarly, (31) is bounded below, before its vanishing remainder, by $`3(0.972-0.843)=0.387>1/3`$.

## 10. Scope of the resulting achievability theorem

The finite permutation and its work identity are exact. The one-third guarantee is asymptotic in $`\delta`$: for each fixed spectrum and temperature, it holds beyond a finite threshold supplied by the uniform limit argument. This note does not supply a practical numerical value for that threshold or an optimal constant multiplying the batch size.

The Gaussian strip supplies a rigorous common fraction of one third. Convergence to unit yield at these batch scales is not established and is not needed for the minimum-batch exponent at the stated fraction.

The result is about finite mean work from typical probability mass. Its work distribution still has positive and negative jumps. Any statement about reliability, fluctuation suppression, total copies over repeated batches, or implementable control depth requires its own resource model and proof.

[Scientific guide](README.md) · [Repository overview](../README.md)
