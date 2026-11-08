# Matched detuning near the harmonic spectrum

The fixed-rational theorem concerns a Hamiltonian held fixed as its input approaches equilibrium. A changing Hamiltonian needs a separate argument. This page proves a finite entropy comparison, checks the actual thermodynamic benchmark, and settles the path $`\alpha_\delta=2+\nu\delta^{3/2}`$ at recovered fraction $`1/10`$. The [order-$`\delta`$ two-copy counterexample](calibration.md#5-harmonic-resonance-an-exact-two-copy-boundary) remains valid.

## 1. Model and exact comparison

Fix $`\beta>0`$, use natural logarithms and put

```math
H_2=\mathrm{diag}(0,1,2),\qquad K=\mathrm{diag}(0,0,1),\qquad
H_{2+\epsilon}=H_2+\epsilon K.
```

The supplied state is matched to the actual Hamiltonian:

```math
\rho_{\delta,2+\epsilon}
=\frac{e^{-\beta H_{2+\epsilon}+\delta K}}{Z}
=\frac{e^{-\beta H_2+tK}}{Z}
=\rho_{t,2},\qquad t=\delta-\beta\epsilon.
```

On $`n`$ independent copies, $`W_n(\delta;2+\epsilon)`$ is the largest mean energy decrease under an arbitrary cyclic unitary, evaluated with $`H_{2+\epsilon}^{(n)}`$. There is no bath, ancillary machine, discarded system, catalyst or feedback. The harmonic quantity $`W_n(t;2)`$ evaluates the same input with $`H_2^{(n)}`$ instead. The [model](model.md) defines the benchmark $`w_\infty`$ and minimum block $`N_f`$.

**Finite entropy comparison.** For every $`\delta>0`$, $`\epsilon\ge0`$ with $`t=\delta-\beta\epsilon>0`$, and every integer $`n\ge1`$,

```math
\boxed{
W_n(t;2)\le W_n(\delta;2+\epsilon)
\le W_n(t;2)+\frac{n\epsilon\delta}{2}.
}
```

Both inequalities concern optima over all quantum unitaries. The estimate is uniform in $`n`$; no lower bound on the actual product-spectrum gaps is assumed.

### Entropy controls the occupation change

Let $`P=\rho_{t,2}^{\otimes n}`$, $`\sigma=UPU^\dagger`$, $`K_n=\sum_jK_j`$, and define

```math
L=\mathrm{Tr}[K_n(P-\sigma)],\qquad
W_\epsilon(U)=\mathrm{Tr}[H_{2+\epsilon}^{(n)}(P-\sigma)],\qquad
W_0(U)=\mathrm{Tr}[H_2^{(n)}(P-\sigma)].
```

The energy and relative-entropy identities are exact:

```math
W_\epsilon(U)=W_0(U)+\epsilon L,\qquad
D(\sigma\Vert P)=\delta L-\beta W_\epsilon(U)=tL-\beta W_0(U).
```

The second identity follows by substituting $`\log P=-\beta H_{2+\epsilon}^{(n)}+\delta K_n-n\log Z`$ and using $`S(\sigma)=S(P)`$.

Write $`\rho=\rho_{t,2}`$ and let $`\sigma_j`$ be the marginal of $`\sigma`$ on copy $`j`$. Product-reference relative entropy decomposes as

```math
D(\sigma\Vert\rho^{\otimes n})
=\sum_jD(\sigma_j\Vert\rho)+\sum_jS(\sigma_j)-S(\sigma)
\ge\sum_jD(\sigma_j\Vert\rho).
```

The last term is nonnegative by entropy subadditivity. Apply data processing to the binary measurement $`\{K,I-K\}`$. With $`r=\mathrm{Tr}(K\rho)`$ and $`r_j=\mathrm{Tr}(K\sigma_j)`$, binary Pinsker in natural logarithms gives

```math
D(\sigma_j\Vert\rho)
\ge D\bigl((r_j,1-r_j)\Vert(r,1-r)\bigr)
\ge2(r_j-r)^2.
```

Cauchy–Schwarz therefore yields

```math
D(\sigma\Vert P)\ge2\sum_j(r_j-r)^2
\ge\frac{2}{n}\left(\sum_j(r-r_j)\right)^2
=\frac{2L^2}{n}.
```

This proof includes coherent and correlated outputs. The measurement is a mathematical device for bounding relative entropy; it supplies no measurement record to the protocol.

### Compare the two optimizations

For an actual-work optimizer, $`W_\epsilon(U)\ge0`$ because doing nothing is allowed. Thus

```math
\delta L\ge D(\sigma\Vert P)\ge\frac{2L^2}{n},
\qquad 0\le L\le\frac{n\delta}{2}.
```

Since $`W_0(U)\le W_n(t;2)`$, this proves the upper comparison. For a harmonic optimizer, $`W_0(U)\ge0`$ and

```math
tL=D(\sigma\Vert P)+\beta W_0(U)\ge0.
```

The assumptions $`t>0`$ and $`\epsilon\ge0`$ imply $`W_\epsilon(U)\ge W_0(U)`$, proving the lower comparison. The sign and preparation assumptions are substantive; the statement does not silently include arbitrary negative detuning or population errors.

## 2. Normalize with the actual Hamiltonian

The benchmark is the energy difference between the supplied state and the positive-temperature Gibbs state of its **actual** Hamiltonian having the same entropy. The [uniform expansion](calibration.md#2-uniform-thermodynamic-normalization), valid for $`\alpha`$ in a fixed compact neighborhood of $`2`$, is

```math
w_\infty(\delta;\alpha)
=\frac{R_{\alpha,\beta}}{2\beta}\delta^2+O(\delta^3),\qquad
R_{\alpha,\beta}
=\mathrm{Var}_{\gamma}(K)
-\frac{\mathrm{Cov}_{\gamma}(H_\alpha,K)^2}{\mathrm{Var}_{\gamma}(H_\alpha)}>0.
```

Here $`\gamma=\gamma_{\beta,\alpha}`$. Smoothness follows from the equal-entropy implicit-function equation, whose inverse-temperature derivative is $`-\beta_*\mathrm{Var}(H_\alpha)\ne0`$ in a common neighborhood. It bounds the Taylor remainder uniformly; it does not interchange the infinite-copy and small-mismatch limits.

Put $`x=e^{-\beta}`$, $`Z_0=1+x+x^2`$ and $`\gamma_1=x/Z_0`$. At the harmonic point,

```math
R_2:=R_{2,\beta}=\frac{x^2}{Z_0(1+4x+x^2)},\qquad
c=\frac{R_2}{2\beta}>0.
```

Fix $`\nu>0`$ and take $`\epsilon=\nu\delta^{3/2}`$. For sufficiently small $`\delta`$, $`t>0`$ and

```math
\begin{aligned}
t&=\delta(1-\beta\nu\sqrt\delta),\\
w_\infty(\delta;2+\epsilon)&=c\delta^2+O(\delta^3),\\
w_\infty(t;2)&=ct^2+O(t^3).
\end{aligned}
```

The two benchmarks need not be equal. Their ratio and the additive comparison error satisfy

```math
\frac{w_\infty(t;2)}{w_\infty(\delta;2+\epsilon)}
=1-2\beta\nu\sqrt\delta+O(\delta).
```

```math
\frac{\epsilon\delta}{2w_\infty(\delta;2+\epsilon)}
=\frac{\beta\nu}{R_2}\sqrt\delta+O(\delta^{3/2}).
```

In particular, the benchmark ratio tends to one and the normalized additive error tends to zero **uniformly over every block size**, because $`n`$ cancels exactly. Replacing the actual benchmark by the harmonic one without checking this ratio would leave a missing step.

## 3. The matched path at yield one tenth

**Theorem.** For every fixed $`\beta,\nu>0`$, there are positive constants $`c_*,C_*,\delta_*`$ such that

```math
\boxed{
c_*\delta^{-2}\le
N_{1/10}(\delta;2+\nu\delta^{3/2})
\le C_*\delta^{-2},\qquad 0<\delta<\delta_*.
}
```

**Necessity.** Apply the inherited [Collective-Work-Thresholds converse](https://github.com/GoGoKo699/Collective-Work-Thresholds/blob/b067b8ad3236f722d3aac4789da176c07e26474e/science/passive_clipping.md) only to the **fixed** harmonic Hamiltonian and mismatch $`t`$. As detailed in the [rational reconciliation](converses.md#corollary-4a-the-inherited-sharp-rational-bound), it excludes every integer with $`nt^2\le s_*`$ from recovering a chosen fixed fraction, for a sufficiently small fixed $`s_*>0`$. Choose that fraction as $`1/40`$. Since $`t/\delta\to1`$, a fixed window $`n\delta^2\le c_*`$ lies inside this exclusion window for all small $`\delta`$. The entropy comparison and Section 2 give

```math
\frac{W_n(\delta;2+\epsilon)}{n w_\infty(\delta;2+\epsilon)}
\le
\frac{W_n(t;2)}{n w_\infty(t;2)}
\frac{w_\infty(t;2)}{w_\infty(\delta;2+\epsilon)}
+\frac{\epsilon\delta}{2w_\infty(\delta;2+\epsilon)}<\frac1{10}
```

throughout that window after reducing $`\delta_*`$. This bounds the minimum over all small block sizes, without assuming monotone yield.

**Sufficiency.** The inherited [one-third construction](achievability.md#5-rational-spectra-a-uniform-one-third-fraction) at the fixed harmonic spectrum supplies a block $`n\le C t^{-2}`$ with

```math
W_n(t;2)\ge\frac13 n w_\infty(t;2).
```

The lower entropy comparison and the benchmark ratio tending to one give an actual recovered fraction greater than $`1/10`$ at that block for every sufficiently small $`\delta`$. Also $`t/\delta\to1`$, so its size is $`O(\delta^{-2})`$. This proves the upper bound. A bare one-third guarantee transfers directly to any fixed fraction strictly below one third; the requested one tenth needs no assertion at the endpoint.

The fixed-rational converse is inherited from Collective-Work-Thresholds, and the one-third construction is inherited from Quantum-Work-Activation. Their fixed-rational combination is a corollary, not another discovery of either ingredient. The additional result here is the finite entropy comparison and its correctly normalized consequence for the specified moving spectrum.

## 4. Two copies and the boundary at order delta

For $`0<\epsilon<1`$ and $`0<t<\beta`$, the state is passive on one copy. In two copies, the only inverted energy sectors are $`|11\rangle`$ and $`|02\rangle,|20\rangle`$. Exactly one of the two latter microstates can be exchanged with $`|11\rangle`$. Thus

```math
W_2(\delta;2+\epsilon)
=\epsilon\frac{x^2}{(1+x+x^2e^t)^2}(e^t-1).
```

For $`\epsilon=\lambda\delta`$ with $`0<\beta\lambda<1`$, the inherited [two-copy calculation](calibration.md#5-harmonic-resonance-an-exact-two-copy-boundary), normalized by the actual benchmark, gives

```math
\frac{W_2(\delta;2+\lambda\delta)}{2w_\infty(\delta;2+\lambda\delta)}
\longrightarrow\beta\lambda(1-\beta\lambda)(1+3\gamma_1).
```

At $`\lambda=1/(8\beta)`$ this limit is $`7(1+3\gamma_1)/64>1/10`$, so $`N_{1/10}=2`$ eventually. The normalized entropy-comparison error is then order one; it does not establish a vanishing perturbation of the harmonic yield.

For the present $`\epsilon=\nu\delta^{3/2}`$ path, the same exact formula instead yields

```math
\frac{W_2(\delta;2+\nu\delta^{3/2})}{2w_\infty(\delta;2+\nu\delta^{3/2})}
=\beta\nu(1+3\gamma_1)\sqrt\delta+O(\delta)\longrightarrow0.
```

Consequently first activation is already at **two copies**, while fixed useful mean-work recovery needs order $`\delta^{-2}`$ copies. The two statements answer different questions. These two detuning paths and the comparison inequality do not specify a full crossover law, an optimal constant, or every sign and rate of spectral detuning.

The [finite comparison checks](../verification/README.md#entropy-comparison-and-two-copy-checks) evaluate the sandwich, benchmark ratios and exact two-copy formula. They are numerical consistency checks; the finite entropy argument and inherited theorems establish the result.

[Scientific guide](README.md) · [Calibration](calibration.md) · [Repository overview](../README.md)
