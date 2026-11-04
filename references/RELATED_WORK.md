# Related work and the specific question studied here

The question is how large a jointly controlled block must be to recover a fixed fraction of the available **average** work from known passive states approaching thermal equilibrium. The model is a fixed qutrit Hamiltonian $`H_\alpha=\operatorname{diag}(0,1,\alpha)`$, the input family $`\rho_\delta\propto\exp(-\beta H_\alpha+\delta K)`$, and unrestricted cyclic unitary control on $`n`$ copies. There is no bath, catalyst, or measurement record in the extraction model. The charged resource is the maximum number of copies jointly controlled. It is not total specimen count for reliable work, implementation time, or gate complexity.

<a id="ergotropy"></a>
<a id="asymptotic-work"></a>
<a id="virtual-temperatures"></a>

## Ergotropy, complete passivity, and the asymptotic benchmark

The finite-system work optimization and its solution by spectral rearrangement are the established notion of ergotropy [1]. Alicki and Fannes proved that collective extraction from many copies reaches the energy of the Gibbs state with the same entropy [2]. Thus the benchmark

```math
w_\infty(\rho,H)=\operatorname{tr}[H(\rho-\gamma_{\beta_*})],
\qquad S(\rho)=S(\gamma_{\beta_*}),
```
and the limit $`W_n/n\to w_\infty`$ are inherited results.

The virtual-temperature proof of Skrzypczyk, Silva, and Brunner explains why a full-rank passive state that is not Gibbs eventually becomes active under collective processing [3]. Constructing one inverted pair from unequal virtual temperatures belongs to that established mechanism. The present question concerns the weight of extractable transitions: a first inverted pair can have negligible probability and recover a vanishing fraction of $`n w_\infty`$.

## Fixed-fraction collective extraction and work concentration

Perarnau-Llobet and Uzdin already study extracting a prescribed fraction of the asymptotic ergotropy collectively [4]. In their arXiv v3, Eqs. (19)–(20) use the equal-entropy Gibbs benchmark and a typical-occupation transport. Equation (12) bounds failure probability by a term of the form $`d\exp(-N\gamma^2c^2)`$. Equation (18) and the discussion after Eq. (20) specify the leading coefficient and acknowledge finite-size corrections. The appendix around Eq. (30) simplifies integer rounding. Fixed-fraction extraction and matching typical multiplicities are therefore not new here.

For the present family, expanding their leading coefficient gives $`c=\Theta(\delta)`$: its relative-entropy numerator is quadratic in $`\delta`$, while its log-population-ratio denominator is linear. This is our substitution into their expression, not a uniform joint-limit theorem quoted from that paper. It points to an $`N\delta^2`$ concentration scale for reliable work. The present $`\delta^{-1}`$ result concerns mean-work **control-block size**, and does not assert a corresponding reduction in specimens needed for reliable positive output.

## Lattice versus nonlattice finite-size work

Tajima and Hayashi analyze finite heat engines using strong large deviations and explicit permutations of two IID Gibbs baths [5]. Their achieving protocol need not use a working body or catalyst. Proposition 4 and Theorem 3 of arXiv v3, particularly Eqs. (45)–(53), distinguish lattice and nonlattice bath spectra. At fixed bath parameters and prescribed heat $`Q_n=o(n)`$, their efficiency expansions have different finite-size remainders. Appendix F analyzes the sorted product spectra. Spectral arithmetic in finite-size work extraction and the spectral-sorting approach are therefore established context.

Those results do not state a bound uniform as the input approaches one Gibbs state. Applying their fixed-parameter expansion in such a joint limit would require additional remainder control. They also do not provide the present single-qutrit input family, a Diophantine classification, or an all-unitary lower bound on the block required for a fixed fraction of its vanishing ergotropy. The comparison here is with their stated theorem; it does not assume their methods cannot be extended.

## Quantitative passivity and other resource models

Salvia and Giovannetti bound the excess energy of states that remain exactly $`N`$-passive, first under structural stability and then under weaker hypotheses at sufficiently large $`N`$ [6]. This is a quantitative connection between finite-copy passivity and the equal-entropy Gibbs state. The present block-size question continues beyond first activation and asks when the recovered fraction is bounded away from zero.

Koukoulekidis, Alexander, Hebdige, and Jennings formulate passivity geometrically and relate a geometric athermality measure to ergotropy [7]. That framework explains the energy/probability ordering structure used here. The new scale question additionally combines ordering with the probability mass of typical occupation types.

Sparaciari, Jennings, and Oppenheim show that a cyclic machine can activate a single nonthermal passive system [8]. Their auxiliary machine changes the allowed resources; it is absent from the present model. Salvia and Giovannetti study zero-fluctuation and narrowly bounded work under a two-point-measurement task, including rational spectral assumptions [9]. These results further establish that arithmetic can matter, while addressing a fluctuation constraint different from average ergotropy.

Second-order thermal-operation interconversion theory gives precise finite-size corrections for source/target conversion with an infidelity criterion [10]. Such results are relevant statistical background, but their fixed-state asymptotics are not automatically uniform when the source, target, and thermodynamic signal converge together. Bath-assisted state conversion also has a different free-operation set.

## Contribution after these comparisons

The result is a joint-limit law for every fixed recovered mean-work fraction up to one third within one controlled block. For $`\delta\to0^+`$, the available work per copy satisfies $`w_\infty=\Theta(\delta^2)`$ for all the fixed spectra considered. Nevertheless, the logarithmic exponent of the required block size is two for fixed rational $`\alpha`$ and one for fixed irrational $`\alpha`$ of irrationality exponent two. The latter includes almost every fixed real $`\alpha`$. Badly approximable spectra admit stronger bounds up to one logarithm.

The achievability argument must choose a useful energy gap, not merely an unusually small gap, and move a nonvanishing amount of typical probability. The converse controls arbitrary unitaries by approximating the input spectrum with a passive one. These ingredients separate the amount of useful mean work from the existence of activation. The calibrated extension is uniform in an explicitly specified order-$`\delta`$ neighborhood of a fixed generic irrational spectrum, with preparation matched to the actual Hamiltonian. A detuning family around a harmonic spectrum gives a contrasting exact two-copy boundary. Spectral instability itself is established context [6]; the statements here quantify the recovered mean-work fraction, the uncertainty window and its order of limits.

The numerical calculations in [numerical report](../verification/report.md) evaluate full spectral rearrangement and check these mechanisms. They are not an independent proof of the exponents. The comparison above does not claim the first activation theorem, the first fixed-fraction protocol, the first use of typical occupations, or the first arithmetic effect in thermodynamic work.

## Primary references

1. A. E. Allahverdyan, R. Balian, and Th. M. Nieuwenhuizen, **Maximal work extraction from finite quantum systems**, *Europhysics Letters* **67**, 565–571 (2004). [DOI](https://doi.org/10.1209/epl/i2004-10101-2); [arXiv:cond-mat/0401574v1](https://arxiv.org/abs/cond-mat/0401574v1), whose preprint title omits *finite*.

2. R. Alicki and M. Fannes, **Entanglement boost for extractable work from ensembles of quantum batteries**, *Physical Review E* **87**, 042123 (2013). [DOI](https://doi.org/10.1103/PhysRevE.87.042123); [arXiv:1211.1209v2](https://arxiv.org/abs/1211.1209v2), whose preprint title is *Extractable work from ensembles of quantum batteries. Entanglement helps*.

3. P. Skrzypczyk, R. Silva, and N. Brunner, **Passivity, complete passivity, and virtual temperatures**, *Physical Review E* **91**, 052133 (2015). [DOI](https://doi.org/10.1103/PhysRevE.91.052133); [arXiv:1412.5485v2](https://arxiv.org/abs/1412.5485v2).

4. M. Perarnau-Llobet and R. Uzdin, **Collective operations can extremely reduce work fluctuations**, *New Journal of Physics* **21**, 083023 (2019). [DOI](https://doi.org/10.1088/1367-2630/ab36a9); [arXiv:1810.02237v3](https://arxiv.org/abs/1810.02237v3), revised 14 August 2019. Relevant locations: Eqs. (12), (18)–(20), and the appendix beginning with Eq. (30).

5. H. Tajima and M. Hayashi, **Finite-size effect on optimal efficiency of heat engines**, *Physical Review E* **96**, 012128 (2017). [DOI](https://doi.org/10.1103/PhysRevE.96.012128); [arXiv:1405.6457v3](https://arxiv.org/abs/1405.6457v3), revised 31 August 2016, with preprint title *Optimal Efficiency of Heat Engines with Finite-Size Heat Baths*. The equation and theorem numbers above refer to this preprint version.

6. R. Salvia and V. Giovannetti, **Energy upper bound for structurally stable N-passive states**, *Quantum* **4**, 274 (2020). [Publisher](https://quantum-journal.org/papers/q-2020-05-28-274/); [arXiv:1912.02099v4](https://arxiv.org/abs/1912.02099v4), revised 27 May 2020.

7. N. Koukoulekidis, R. Alexander, T. Hebdige, and D. Jennings, **The geometry of passivity for quantum systems and a novel elementary derivation of the Gibbs state**, *Quantum* **5**, 411 (2021). [Publisher](https://quantum-journal.org/papers/q-2021-03-15-411/); [arXiv:1912.07968v3](https://arxiv.org/abs/1912.07968v3).

8. C. Sparaciari, D. Jennings, and J. Oppenheim, **Energetic instability of passive states in thermodynamics**, *Nature Communications* **8**, 1895 (2017). [DOI](https://doi.org/10.1038/s41467-017-01505-4); [arXiv:1701.01703v1](https://arxiv.org/abs/1701.01703v1); [open article](https://pmc.ncbi.nlm.nih.gov/articles/PMC5711874/).

9. R. Salvia and V. Giovannetti, **Zero-fluctuation quantum work extraction**, *Physical Review A* **110**, 012213 (2024). [DOI](https://doi.org/10.1103/PhysRevA.110.012213); [arXiv:2402.16964v1](https://arxiv.org/abs/2402.16964v1).

10. C. T. Chubb, M. Tomamichel, and K. Korzekwa, **Beyond the thermodynamic limit: finite-size corrections to state interconversion rates**, *Quantum* **2**, 108 (2018). [Publisher](https://quantum-journal.org/papers/q-2018-11-27-108/); [arXiv:1711.01193v5](https://arxiv.org/abs/1711.01193v5).

Structured entries are available in [references.bib](references.bib). The comparison concerns the identified primary results and their stated assumptions; it does not establish exhaustive priority.
