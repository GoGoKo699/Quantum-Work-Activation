# The available work near equilibrium

The asymptotic work density is the energy difference to the Gibbs state with the same entropy. This [endpoint is established prior work](../references/RELATED_WORK.md#asymptotic-work). Here we compute its near-equilibrium coefficient and connect that coefficient to the occupation-space geometry used in the extraction construction.

All expectations in this page without an explicit subscript are under $`\gamma=\gamma_{\beta,\alpha}`$. The spectrum and $`\beta>0`$ are fixed.

## 1. Equal-entropy Gibbs state

Write

```math
V=\mathrm{Var}_{\gamma}(H_\alpha),\qquad
C=\mathrm{Cov}_{\gamma}(H_\alpha,K),\qquad
R=\mathrm{Var}_{\gamma}(K)-\frac{C^2}{V}.
```
The Gibbs state has full support and three distinct energies, so $`V>0`$. Moreover $`K`$ is not affine in $`H_\alpha`$ on the three energies. Consequently $`R>0`$.

The entropy of the Gibbs family obeys

```math
\frac{d}{d\beta}S(\gamma_{\beta,\alpha})=-\beta V.
```
Since this derivative is nonzero, the implicit-function theorem gives a smooth positive $`\beta_*(\delta)`$ near zero such that

```math
S(\rho_{\delta,\alpha})=S(\gamma_{\beta_*(\delta),\alpha}),
\qquad
\beta_*(0)=\beta.
```
For the tilted state,

```math
S(\rho_{\delta,\alpha})
=\beta\,\langle H_\alpha\rangle_\delta
-\delta\,\langle K\rangle_\delta+\log Z_{\delta,\alpha}.
```
Differentiating at zero gives $`S'_{\rho}(0)=\beta C`$. The equal-entropy condition therefore yields

```math
\beta_*'(0)=-\frac{C}{V}.
```

## 2. Relative entropy and the quadratic coefficient

Whenever a state $`\rho`$ and a Gibbs state $`\gamma_{\beta_*}`$ have the same entropy,

```math
D(\rho\Vert\gamma_{\beta_*})
=\beta_*\left(
\mathrm{Tr}\rho H_\alpha
-\mathrm{Tr}\gamma_{\beta_*}H_\alpha
\right).
```
The first-order score of $`\rho_{\delta,\alpha}`$ relative to its equal-entropy Gibbs state is the centered residual

```math
r_i=K_i-\langle K\rangle
-\frac{C}{V}(E_i-\langle H_\alpha\rangle).
```
It has mean zero and variance $`R`$. Expanding the relative entropy of these finite, full-support distributions gives

```math
D(\rho_{\delta,\alpha}\Vert
\gamma_{\beta_*(\delta),\alpha})
=\frac12 R\delta^2+O(\delta^3).
```
Dividing by the smooth positive $`\beta_*(\delta)`$ proves

```math
w_\infty(\delta;\alpha)
=\frac{R}{2\beta}\delta^2+O(\delta^3).
```
In particular, after reducing $`\delta_0`$ if necessary,

```math
w_\infty(\delta;\alpha)\ge \frac{R}{4\beta}\delta^2
\qquad(0<\delta<\delta_0).
```
All derivatives and remainder bounds are uniform when $`\alpha`$ ranges over a sufficiently small compact neighborhood of a fixed $`\alpha_0>1`$. This supplies the uniform normalization in the [calibration theorem](calibration.md).

## 3. The same coefficient in occupation space

Let $`\gamma_i`$ be the three Gibbs probabilities and define

```math
v=(\alpha-1,-\alpha,1).
```
This vector preserves total occupation and energy:

```math
\sum_i v_i=0,\qquad \sum_i E_i v_i=0.
```
The residual $`r`$ above satisfies

```math
\sum_i\gamma_i r_i=0,\qquad
\sum_iE_i\gamma_i r_i=0.
```
The common null space is one-dimensional, so $`\gamma_i r_i=t v_i`$ for a scalar $`t`$. Taking the inner product with $`K`$ gives $`t=R`$, because $`v_2=1`$. Hence

```math
r_i=\frac{R v_i}{\gamma_i},
\qquad
R=\sum_i\gamma_i r_i^2
=R^2\sum_i\frac{v_i^2}{\gamma_i}.
```
Therefore

```math
\boxed{\quad
\sum_i\frac{v_i^2}{\gamma_i}=\frac1R.
\quad}
```
For multinomial occupations, the expression on the left is the squared Gaussian length of a unit displacement in the energy-preserving direction. This identity is why a shift of order $`q`$ at block size $`n`$ has standardized size $`q/\sqrt{nR}`$, and why the extraction bound can be normalized by the same thermodynamic $`R`$.

## 4. What the normalization compares

The coefficient $`R/(2\beta)`$ depends on the fixed temperature and spectrum. The theorem compares a fraction of each system's own available work; it does not identify those coefficients across different Hamiltonians.

For fixed $`\delta`$, the asymptotic benchmark takes $`n\to\infty`$. The minimum-block question then studies how quickly that fraction becomes accessible as $`\delta\to0`$. The proof uses the exact Gibbs benchmark and its local expansion, rather than interchanging these two limits.

For a moving spectrum, [matched detuning](matched_detuning.md#2-normalize-with-the-actual-hamiltonian) checks both the actual-Hamiltonian expansion and its ratio to an effective harmonic benchmark. The equality of input populations alone does not equate their thermodynamic work benchmarks.

[Scientific guide](README.md) · [Repository overview](../README.md)
