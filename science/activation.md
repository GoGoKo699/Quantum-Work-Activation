# First activation and finite work fractions

The earliest block with positive work need not recover an appreciable fraction of the asymptotic work. The distinction can be made explicit for the same qutrit family.

The population-inversion criterion is a direct instance of the [virtual-temperature activation framework](../references/RELATED_WORK.md#virtual-temperatures). The criterion itself is inherited; its comparison with the finite-fraction theorem explains which resource that theorem measures.

## 1. Exact first-inversion criterion

A microstate with occupation counts $`k=(k_0,k_1,k_2)`$ has energy and probability

```math
E(k)=k_1+\alpha k_2,\qquad
P(k)=Z_{\delta,\alpha}^{-n}
\exp[-\beta E(k)+\delta k_2].
```
An inversion between two distinct energies requires a positive difference $`q`$ in the level-2 count. Writing the difference in level-1 count as $`-p`$, the occupation shift is

```math
\Delta=(p-q,-p,q).
```
Its energy and log-probability differences are

```math
h=\alpha q-p,\qquad s=\delta q-\beta h.
```
The more energetic type is also more probable per microstate precisely when $`h>0`$ and $`s>0`$. For sufficiently small $`\delta`$, these inequalities force $`p>q>0`$, and become

```math
\alpha-\frac{\delta}{\beta}<\frac pq<\alpha.
```
The positive and negative parts of $`\Delta`$ each contain $`p`$ occupations. Therefore the smallest block that can realize this difference has $`n=p`$. At that size, the two types are $`(0,p,0)`$ and $`(p-q,0,q)`$. It follows that

```math
N_{\mathrm{act}}(\delta;\alpha)
=\min\left\{p:
\exists q\ge1,\quad
\alpha-\frac{\delta}{\beta}<\frac pq<\alpha
\right\}.
```
The inequalities are strict: equal energies or equal populations give zero work. Once an inverted pair exists, swapping its two eigenstates gives positive mean work. If no pair exists, the full product state is passive, so every unitary gives nonpositive extracted work.

## 2. Activation scales

For a reduced rational $`\alpha=a/b`$, every positive many-copy energy difference is at least $`1/b`$. Thus an inversion needs $`\delta q>\beta/b`$, giving a lower bound proportional to $`\delta^{-1}`$. Choosing $`q`$ in the progression $`aq=1\pmod b`$, immediately above $`\beta/(b\delta)`$, gives the matching upper bound:

```math
N_{\mathrm{act}}(\delta;\alpha)=\Theta_{\alpha,\beta}(\delta^{-1}).
```
For a badly approximable $`\alpha`$, the lower gap bound $`h\ge\kappa/q`$ requires $`q^2>\beta\kappa/\delta`$. The useful-approximation lemma in the [construction](achievability.md) gives the matching upper bound. Hence

```math
N_{\mathrm{act}}(\delta;\alpha)=\Theta_{\alpha,\beta}(\delta^{-1/2}).
```
More generally, the same Diophantine lower bound with an arbitrary exponent slack, together with the Farey construction, gives logarithmic activation exponent $`1/2`$ for every irrationality-exponent-two $`\alpha`$.

## 3. Why first activation does not set the mean-work block scale

At the first inversion, the two selected microstates can have exponentially small probabilities. Their swap proves positivity but gives no fixed fraction of $`n w_\infty`$.

The [finite-fraction construction](achievability.md) places a displacement of size $`q`$ among occupation fluctuations of size $`\sqrt n`$. Taking $`n`$ proportional to $`q^2`$ makes a nonvanishing amount of probability available for compatible swaps. Conversely, the [all-unitary bounds](converses.md) show that at every polynomially smaller block size the total mean work remains a vanishing fraction of the benchmark.

| Fixed spectrum | First-positive-work exponent | Fixed-fraction block exponent |
|---|---:|---:|
| Rational | $`1`$ | $`2`$ |
| Irrationality exponent two | $`1/2`$ | $`1`$ |

Each exponent is the limit of $`\log N/\log(1/\delta)`$. The second column concerns any positive work; the third concerns every fixed fraction $`0\lt f\le1/3`$.

[Scientific guide](README.md) · [Repository overview](../README.md)
