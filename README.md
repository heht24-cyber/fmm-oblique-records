# Oblique Hyperplane Projection Deletion for Fast Matrix Multiplication

**58 New Independently Verified Exact Characteristic-0 Matrix Multiplication Rank Records** (saving **1,461 multiplications** in total relative to the monotone-closed 2026-11-24 state of the art combining [Sedoglavic's Lille Catalogue](https://github.com/sedoglavic/fmm_digest) [`2daba01`, 2026-11-23], [Greg Sidebottom's `mat_mul`](https://github.com/gsidebottom/mat_mul) [`2026-11-22`], [Quantavane](https://github.com/arhancanli/quantavane-fmm-records) [`2026-11-14`], [Andrew Perminov's `FastMatrixMultiplication`](https://github.com/dronperminov/FastMatrixMultiplication) [`2026-11-16`], and [LITA](https://github.com/khoruzhii/lita) [`2026`]).

## Highlights

- **58 undominated world records** (0 dominated under monotonicity closure), every single scheme canonically oriented to sorted format $m \le n \le p$ and independently proved exact over $\mathbb{Q}$ (Characteristic 0).
- **10 classic formats with $\max(m, n, p) \le 16$** (`schemes_classic_le16/`):
  - $\langle 9\times 11\times 11 : \mathbf{702}\rangle$ — **pure dyadic $\mathbb{Z}[1/2]$**, beating Sidebottom's `705` ($-3$) and Quantavane's `708` ($-6$).
  - $\langle 9\times 11\times 15 : \mathbf{949}\rangle$ — **pure dyadic $\mathbb{Z}[1/2]$**, beating Sidebottom's `953` ($-4$) while simultaneously strengthening the coefficient ring from $\mathbb{Z}[1/6]$ to $\mathbb{Z}[1/2]$.
  - $\langle 11\times 11\times 16 : \mathbf{1224}\rangle$ — **pure dyadic $\mathbb{Z}[1/2]$**, beating `1230` ($-6$).
  - $\langle 12\times 13\times 13 : \mathbf{1270}\rangle$ ($-4$), $\langle 13\times 14\times 15 : \mathbf{1644}\rangle$ ($-1$), $\langle 14\times 14\times 15 : \mathbf{1709}\rangle$ ($-6$), $\langle 14\times 15\times 15 : \mathbf{1836}\rangle$ ($-6$), $\langle 14\times 16\times 16 : \mathbf{2110}\rangle$ ($-18$), $\langle 15\times 15\times 16 : \mathbf{2105}\rangle$ (**$-27$**), and $\langle 15\times 16\times 16 : \mathbf{2173}\rangle$ (**$-20$** vs Sidebottom `2193`; **$-27$** vs `fmm_digest@2daba01` `2200`).
- **14 pure dyadic ($\mathbb{Z}[1/2]$) records** (valid over every ring in which $2$ is invertible, including $\mathbb{F}_3, \mathbb{F}_5, \dots$), featuring Kronecker oblique deletions up to **$-63$** ($\langle 9\times 17\times 30 : \mathbf{2648}\rangle$, $\langle 15\times 17\times 18 : \mathbf{2648}\rangle$ [$-57$], $\langle 12\times 17\times 17 : \mathbf{2058}\rangle$ [$-56$], $\langle 11\times 18\times 21 : \mathbf{2443}\rangle$ [$-56$], $\langle 9\times 17\times 24 : \mathbf{2097}\rangle$ [$-54$], $\langle 12\times 17\times 18 : \mathbf{2106}\rangle$ [$-42$]).
- **48 large formats ($17 \le \max \le 23$)** (`schemes_large/`), with single-format savings up to **$-90$** ($\langle 20\times 21\times 22 : \mathbf{4897}\rangle$ vs `4987`, $\langle 19\times 22\times 22 : \mathbf{4905}\rangle$ vs `4994`, $\langle 20\times 23\times 23 : \mathbf{5495}\rangle$ vs `5554`, $\langle 18\times 21\times 21 : \mathbf{4274}\rangle$ vs `4327`).

See [RESULTS_TABLE.md](RESULTS_TABLE.md) for the complete 58-row table and [paper.tex](paper.tex) for the mathematical proof and structural analysis.

## Method Summary: Oblique Hyperplane Projection Deletion

Given any exact bilinear scheme $\sum_{r=1}^R \langle U_r, A\rangle \langle V_r, B\rangle W_r = AB$ for $\langle m\times n\times p\rangle$ over a field $K$ and any nonzero vectors $\alpha, \beta \in K^d$ satisfying $\alpha^T \beta \ne 0$:

1. Let $k$ be any index with $\alpha_k \ne 0$ and $J = \lbrace 0,\dots,d-1\rbrace \setminus \lbrace k\rbrace$.
2. Define $E \in K^{d\times(d-1)}$ by $E_J = I_{d-1}$ and $E_{k,j} = -\alpha_j / \alpha_k$ (so $\alpha^T E = 0$), and define $\Pi = R_J (I_d - \frac{\beta\alpha^T}{\alpha^T\beta}) \in K^{(d-1)\times d}$ (so $\Pi E = I_{d-1}$ and $\Pi \beta = 0$).
3. Replacing $(U, V, W)$ by $(E^T U, V, \Pi W)$ (axis $0$), $(U \Pi^T, E^T V, W)$ (axis $1$), or $(U, V E, W \Pi^T)$ (axis $2$) yields an **exact** bilinear scheme for the reduced format, annihilating every term whose corresponding factor lies in $\mathrm{span}(\alpha)$ or $\mathrm{span}(\beta)$.
4. We follow each oblique deletion by **Optimal Pivot-Exchange 2-Reduction** on the left nullspaces of the Khatri--Rao products ($U\odot V$, $U\odot W$, $V\odot W$), selecting free-row pivot bases that maximize simultaneous complementary-row cancellations, and replay the entire chain in exact rational arithmetic (`fractions.Fraction`).

Whereas standard coordinate deletion ($\alpha = \beta = e_k$) kills $0$ terms directly on even LITA squares ($14^3, 16^3, 18^3, 20^3, 22^3, \dots$) and misses the internal dual vectors on odd LITA squares ($13^3, 15^3, 17^3, 19^3, 21^3, 23^3, \dots$), symmetric oblique projection along LITA's half-period eigenvectors ($e_i \pm e_{i+m}$) and internal dual vectors unlocks massive direct annihilations and cascaded 2-reductions.

## Independent Exact Verification

Every scheme in `schemes_classic_le16/` and `schemes_large/` is stored in compressed sparse exact rational JSON (`.json.gz`). You can independently verify any or all 58 schemes using only Python 3.10+ and NumPy (zero other dependencies):

```bash
# Verify a single scheme (takes ~0.1s - 2s)
python verify_all.py schemes_classic_le16/9x11x11_m702_dyadic.json.gz

# Verify all 10 classic <=16 schemes (~15s)
python verify_all.py schemes_classic_le16/*.json.gz

# Verify ALL 58 schemes (full deterministic CRT proof over all (mn)(np)(mp) Brent equations)
python verify_all.py
```

For each scheme, `verify_all.py`:
1. Parses every rational coefficient via exact `fractions.Fraction` and clears exact LCM denominators $(d_U, d_V, d_W)$, setting $D = d_U d_V d_W$.
2. Computes the rigorous infinity-norm bound $B = D + \sum_{r=1}^R \lVert U_r\rVert_\infty \lVert V_r\rVert_\infty \lVert W_r\rVert_\infty$ and selects deterministic 30-bit primes $P_1, \dots, P_k$ with $\prod_i P_i > 2B$.
3. Checks **all $(mn)(np)(mp)$ Brent tensor equations** modulo every $P_i$ using exact 15-bit split arithmetic (asserting $R \cdot 32767^2 < 2^{52}$ for bit-exact zero-rounding evaluation). By the Chinese Remainder Theorem, passing proves exact equality over $\mathbb{Z}$ and $\mathbb{Q}$ with **zero probability of error**.
4. Additionally runs exact Python `Fraction` random matrix multiplication trials and a negative corruption check (perturbing a single entry must be rejected).

## Repository Layout

- `schemes_classic_le16/` — 10 compressed exact schemes with $\max(m, n, p) \le 16$.
- `schemes_large/` — 48 compressed exact schemes with $17 \le \max(m, n, p) \le 23$.
- `verify_all.py` — Standalone zero-dependency deterministic CRT exact verifier.
- `RESULTS_TABLE.md` & `results_summary.json` — Full verified comparison tables.
- `paper.tex` — Formal technical manuscript detailing the theorem, structural analysis, and results.
- `LICENSE` — MIT License.

## Author & Acknowledgments

**Haotian He** (2026). All search, exact rational replay, and deterministic CRT certification were developed with AI assistance. We gratefully acknowledge the open schemes and benchmark catalogues maintained by Alexandre Sedoglavic (`fmm_digest`), Andrew I. Perminov (`FastMatrixMultiplication`), Greg Sidebottom (`mat_mul`), Jean-Guillaume Dumas / Clément Pernet (`<3x3x6:40>`), and Kirill Khoruzhii (`lita`).
