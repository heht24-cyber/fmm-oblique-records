# Verified Exact Characteristic-0 Fast Matrix Multiplication World Records

- **Total Undominated Certified World Records**: **58** (all strictly below the monotone-closed 2026-11-24 Master SOTA combining Sedoglavic `fmm_sota.json` [2026-11-23], Sidebottom `gsidebottom/mat_mul` [2026-11-22], Quantavane [2026-11-14], Perminov [2026-11-16], and LITA [2026]).
- **Classic Formats (`max(m, n, p) <= 16`)**: **10** records.
- **Pure Dyadic ($\mathbb{Z}[1/2]$) / Integer Records**: **14** records.
- **Total Cumulative Multiplications Saved**: **-1461**.
- **Certification**: Every single `.json.gz` file has been oriented to canonical sorted shape `m <= n <= p` and proved 100% exact over $\mathbb{Q}$ (Characteristic 0) via Deterministic Chinese Remainder Theorem over all $(mn)(np)(mp)$ Brent equations + exact Python `Fraction` trials + negative corruption check.

| Format | New Rank | Prev SOTA (2026-11-24) | Gain | $\omega_{\text{new}}$ ($\omega_{\text{prev}}$) | Coefficient Ring | Source Parent | File |
|---|---:|---:|---:|---|---|---|---|
| $\langle 9\times 11\times 11\rangle$ | **702** | 705 (Sedoglavic_2026-11-23) | **-3** | 2.81163 (2.81346) | `Z[1/2]` | `schemes/results/Q/9x11x12_m738_Q.json` | `schemes_classic_le16/9x11x11_m702_dyadic.json.gz` |
| $\langle 9\times 11\times 15\rangle$ | **949** | 953 (Sidebottom_2026-11-22:schemes) | **-4** | 2.81607 (2.81780) | `Z[1/2]` | `schemes/9x11x16_987_dyadic/9x11x16_m987_Q.json.gz` | `schemes_classic_le16/9x11x15_m949_dyadic.json.gz` |
| $\langle 9\times 17\times 24\rangle$ | **2097** | 2151 (Sedoglavic_2026-11-23) | **-54** | 2.79525 (2.80454) | `Z[1/2]` | `DPS40xS346_9x18x24` | `schemes_large/9x17x24_m2097_dyadic.json.gz` |
| $\langle 9\times 17\times 30\rangle$ | **2648** | 2711 (Sedoglavic_2026-11-23) | **-63** | 2.80428 (2.81265) | `Z[1/2]` | `DPS40xS356_9x18x30` | `schemes_large/9x17x30_m2648_dyadic.json.gz` |
| $\langle 9\times 18\times 23\rangle$ | **2133** | 2140 (Sedoglavic_2026-11-23) | **-7** | 2.79650 (2.79769) | `Z[1/2]` | `DPS40xS346_9x18x24` | `schemes_large/9x18x23_m2133_dyadic.json.gz` |
| $\langle 9\times 18\times 29\rangle$ | **2690** | 2700 (Sedoglavic_2026-11-23) | **-10** | 2.80215 (2.80347) | `Z[1/2]` | `DPS40xS356_9x18x30` | `schemes_large/9x18x29_m2690_dyadic.json.gz` |
| $\langle 11\times 11\times 16\rangle$ | **1224** | 1230 (Sedoglavic_2026-11-23) | **-6** | 2.81826 (2.82020) | `Z[1/2]` | `schemes/results/Q/11x12x16_m1278_Q.json` | `schemes_classic_le16/11x11x16_m1224_dyadic.json.gz` |
| $\langle 11\times 17\times 18\rangle$ | **2043** | 2059 (Sedoglavic_2026-11-23) | **-16** | 2.81556 (2.81844) | `Z[1/2]` | `DPS40xS346_12x18x18` | `schemes_large/11x17x18_m2043_dyadic.json.gz` |
| $\langle 11\times 18\times 21\rangle$ | **2443** | 2499 (Sedoglavic_2026-11-23) | **-56** | 2.80854 (2.81670) | `Z[1/2]` | `DPS40xS347_12x21x18` | `schemes_large/11x18x21_m2443_dyadic.json.gz` |
| $\langle 12\times 13\times 13\rangle$ | **1270** | 1274 (Sedoglavic_2026-11-23) | **-4** | 2.81561 (2.81685) | `Z[1/2,1/3,1/13]` | `13x13x13_r1379.npz` | `schemes_classic_le16/12x13x13_m1270_Q.json.gz` |
| $\langle 12\times 17\times 17\rangle$ | **2058** | 2114 (Sedoglavic_2026-11-23) | **-56** | 2.80794 (2.81782) | `Z[1/2]` | `DPS40xS346_12x18x18` | `schemes_large/12x17x17_m2058_dyadic.json.gz` |
| $\langle 12\times 17\times 18\rangle$ | **2106** | 2148 (Sedoglavic_2026-11-23) | **-42** | 2.79682 (2.80403) | `Z[1/2]` | `DPS40xS346_12x18x18` | `schemes_large/12x17x18_m2106_dyadic.json.gz` |
| $\langle 13\times 14\times 15\rangle$ | **1644** | 1645 (Sidebottom_2026-11-22:schemes) | **-1** | 2.80770 (2.80793) | `Z[1/2,1/5,1/17]` | `15x15x15_r1977.npz` | `schemes_classic_le16/13x14x15_m1644_Q.json.gz` |
| $\langle 13\times 17\times 17\rangle$ | **2306** | 2320 (Sedoglavic_2026-11-23) | **-14** | 2.82211 (2.82431) | `Z[1/2,1/3,1/5,1/7]` | `17x17x17_r2723.npz` | `schemes_large/13x17x17_m2306_Q.json.gz` |
| $\langle 14\times 14\times 15\rangle$ | **1709** | 1715 (Sedoglavic_2026-11-23) | **-6** | 2.79621 (2.79753) | `Z[1/2,1/5,1/17]` | `15x15x15_r1977.npz` | `schemes_classic_le16/14x14x15_m1709_Q.json.gz` |
| $\langle 14\times 15\times 15\rangle$ | **1836** | 1842 (Sedoglavic_2026-11-23) | **-6** | 2.79896 (2.80017) | `Z[1/2,1/5,1/17]` | `15x15x15_r1977.npz` | `schemes_classic_le16/14x15x15_m1836_Q.json.gz` |
| $\langle 14\times 16\times 16\rangle$ | **2110** | 2128 (Sedoglavic_2026-11-23) | **-18** | 2.80580 (2.80891) | `Z[1/2,1/3,1/5,1/7]` | `16x16x16_r2236.npz` | `schemes_classic_le16/14x16x16_m2110_Q.json.gz` |
| $\langle 14\times 16\times 17\rangle$ | **2246** | 2278 (Sidebottom_2026-11-22:large) | **-32** | 2.80790 (2.81304) | `Z[1/2,1/3,1/5,1/7]` | `17x17x17_r2723.npz` | `schemes_large/14x16x17_m2246_Q.json.gz` |
| $\langle 14\times 17\times 17\rangle$ | **2400** | 2435 (Sidebottom_2026-11-22:large) | **-35** | 2.81136 (2.81659) | `Z[1/2,1/3,1/5,1/7]` | `17x17x17_r2723.npz` | `schemes_large/14x17x17_m2400_Q.json.gz` |
| $\langle 14\times 17\times 18\rangle$ | **2558** | 2596 (Sedoglavic_2026-11-23) | **-38** | 2.81501 (2.82030) | `Z[1/2]` | `DPS40xS356_15x18x18` | `schemes_large/14x17x18_m2558_dyadic.json.gz` |
| $\langle 14\times 18\times 18\rangle$ | **2630** | 2655 (Sedoglavic_2026-11-23) | **-25** | 2.80579 (2.80916) | `Z[1/2]` | `DPS40xS356_15x18x18` | `schemes_large/14x18x18_m2630_dyadic.json.gz` |
| $\langle 15\times 15\times 16\rangle$ | **2105** | 2132 (Sedoglavic_2026-11-23) | **-27** | 2.80341 (2.80807) | `Z[1/2,1/3,1/5,1/7]` | `17x17x17_r2723.npz` | `schemes_classic_le16/15x15x16_m2105_Q.json.gz` |
| $\langle 15\times 15\times 17\rangle$ | **2248** | 2286 (Sidebottom_2026-11-22:large) | **-38** | 2.80670 (2.81280) | `Z[1/2,1/3,1/5,1/7]` | `17x17x17_r2723.npz` | `schemes_large/15x15x17_m2248_Q.json.gz` |
| $\langle 15\times 16\times 16\rangle$ | **2173** | 2193 (Sidebottom_2026-11-22:large) | **-20** | 2.79304 (2.79637) | `Z[1/2,1/3,1/5,1/7]` | `17x17x17_r2723.npz` | `schemes_classic_le16/15x16x16_m2173_Q.json.gz` |
| $\langle 15\times 16\times 17\rangle$ | **2310** | 2334 (Sidebottom_2026-11-22:large) | **-24** | 2.79473 (2.79846) | `Z[1/2,1/3,1/5,1/7]` | `17x17x17_r2723.npz` | `schemes_large/15x16x17_m2310_Q.json.gz` |
| $\langle 15\times 17\times 17\rangle$ | **2463** | 2490 (Sidebottom_2026-11-22:large) | **-27** | 2.79748 (2.80138) | `Z[1/2,1/3,1/5,1/7]` | `17x17x17_r2723.npz` | `schemes_large/15x17x17_m2463_Q.json.gz` |
| $\langle 15\times 17\times 18\rangle$ | **2648** | 2705 (Sedoglavic_2026-11-23) | **-57** | 2.80428 (2.81186) | `Z[1/2]` | `DPS40xS356_15x18x18` | `schemes_large/15x17x18_m2648_dyadic.json.gz` |
| $\langle 16\times 16\times 17\rangle$ | **2385** | 2392 (Sidebottom_2026-11-22:large) | **-7** | 2.78465 (2.78570) | `Z[1/2,1/3,1/5,1/7]` | `17x17x17_r2723.npz` | `schemes_large/16x16x17_m2385_Q.json.gz` |
| $\langle 16\times 17\times 17\rangle$ | **2546** | 2553 (Sidebottom_2026-11-22:large) | **-7** | 2.78787 (2.78884) | `Z[1/2,1/3,1/5,1/7]` | `17x17x17_r2723.npz` | `schemes_large/16x17x17_m2546_Q.json.gz` |
| $\langle 16\times 17\times 18\rangle$ | **2830** | 2864 (Sidebottom_2026-11-22:large) | **-34** | 2.80645 (2.81067) | `Z[1/2,1/3,1/5,1/7]` | `18x18x18_r3031.npz` | `schemes_large/16x17x18_m2830_Q.json.gz` |
| $\langle 16\times 18\times 18\rangle$ | **2891** | 2916 (Sedoglavic_2026-11-23) | **-25** | 2.79518 (2.79820) | `Z[1/2,1/3,1/5,1/7]` | `18x18x18_r3031.npz` | `schemes_large/16x18x18_m2891_Q.json.gz` |
| $\langle 16\times 19\times 19\rangle$ | **3256** | 3293 (Sidebottom_2026-11-22:large) | **-37** | 2.80146 (2.80538) | `Z[1/2,1/3,1/5,1/7]` | `19x19x19_r3633.npz` | `schemes_large/16x19x19_m3256_Q.json.gz` |
| $\langle 17\times 17\times 18\rangle$ | **2905** | 2923 (Sidebottom_2026-11-22:large) | **-18** | 2.79574 (2.79790) | `Z[1/2,1/3,1/5,1/7]` | `18x18x18_r3031.npz` | `schemes_large/17x17x18_m2905_Q.json.gz` |
| $\langle 17\times 18\times 18\rangle$ | **2963** | 2982 (Sidebottom_2026-11-22:large) | **-19** | 2.78407 (2.78630) | `Z[1/2,1/3,1/5,1/7]` | `18x18x18_r3031.npz` | `schemes_large/17x18x18_m2963_Q.json.gz` |
| $\langle 17\times 18\times 19\rangle$ | **3133** | 3160 (Sidebottom_2026-11-22:large) | **-27** | 2.78601 (2.78898) | `Z[1/2,1/3,1/5,1/7]` | `19x19x19_r3633.npz` | `schemes_large/17x18x19_m3133_Q.json.gz` |
| $\langle 17\times 19\times 19\rangle$ | **3323** | 3354 (Sidebottom_2026-11-22:large) | **-31** | 2.78900 (2.79219) | `Z[1/2,1/3,1/5,1/7]` | `19x19x19_r3633.npz` | `schemes_large/17x19x19_m3323_Q.json.gz` |
| $\langle 17\times 20\times 20\rangle$ | **3779** | 3796 (Sidebottom_2026-11-22:large) | **-17** | 2.80029 (2.80181) | `Z[1/2,1/7,1/29]` | `20x20x20_r3994.npz` | `schemes_large/17x20x20_m3779_Q.json.gz` |
| $\langle 18\times 18\times 19\rangle$ | **3217** | 3225 (Sidebottom_2026-11-22:large) | **-8** | 2.77686 (2.77771) | `Z[1/2,1/3,1/5,1/7]` | `19x19x19_r3633.npz` | `schemes_large/18x18x19_m3217_Q.json.gz` |
| $\langle 18\times 19\times 19\rangle$ | **3416** | 3424 (Sidebottom_2026-11-22:large) | **-8** | 2.78027 (2.78107) | `Z[1/2,1/3,1/5,1/7]` | `19x19x19_r3633.npz` | `schemes_large/18x19x19_m3416_Q.json.gz` |
| $\langle 18\times 19\times 20\rangle$ | **3772** | 3784 (Sidebottom_2026-11-22:large) | **-12** | 2.79780 (2.79888) | `Z[1/2,1/7,1/29]` | `20x20x20_r3994.npz` | `schemes_large/18x19x20_m3772_Q.json.gz` |
| $\langle 18\times 20\times 20\rangle$ | **3838** | 3865 (Sidebottom_2026-11-22:large) | **-27** | 2.78750 (2.78987) | `Z[1/2,1/7,1/29]` | `20x20x20_r3994.npz` | `schemes_large/18x20x20_m3838_Q.json.gz` |
| $\langle 18\times 21\times 21\rangle$ | **4274** | 4327 (Sidebottom_2026-11-22:large) | **-53** | 2.79316 (2.79727) | `Z[1/2,1/7,1/29]` | `21x21x21_r4723.npz` | `schemes_large/18x21x21_m4274_Q.json.gz` |
| $\langle 19\times 19\times 20\rangle$ | **3854** | 3868 (Sidebottom_2026-11-22:large) | **-14** | 2.78803 (2.78926) | `Z[1/2,1/7,1/29]` | `20x20x20_r3994.npz` | `schemes_large/19x19x20_m3854_Q.json.gz` |
| $\langle 19\times 20\times 20\rangle$ | **3918** | 3935 (Sidebottom_2026-11-22:large) | **-17** | 2.77756 (2.77901) | `Z[1/2,1/7,1/29]` | `20x20x20_r3994.npz` | `schemes_large/19x20x20_m3918_Q.json.gz` |
| $\langle 19\times 20\times 21\rangle$ | **4141** | 4154 (Sidebottom_2026-11-22:large) | **-13** | 2.78096 (2.78201) | `Z[1/2,1/7,1/29]` | `21x21x21_r4723.npz` | `schemes_large/19x20x21_m4141_Q.json.gz` |
| $\langle 19\times 21\times 21\rangle$ | **4378** | 4394 (Sidebottom_2026-11-22:large) | **-16** | 2.78442 (2.78563) | `Z[1/2,1/7,1/29]` | `21x21x21_r4723.npz` | `schemes_large/19x21x21_m4378_Q.json.gz` |
| $\langle 19\times 22\times 22\rangle$ | **4905** | 4994 (Sidebottom_2026-11-22:large) | **-89** | 2.79340 (2.79931) | `Z[1/2,1/3,1/11]` | `22x22x22_r5141.npz` | `schemes_large/19x22x22_m4905_Q.json.gz` |
| $\langle 20\times 20\times 21\rangle$ | **4221** | 4230 (Sidebottom_2026-11-22:large) | **-9** | 2.77153 (2.77223) | `Z[1/2,1/7,1/29]` | `21x21x21_r4723.npz` | `schemes_large/20x20x21_m4221_Q.json.gz` |
| $\langle 20\times 21\times 21\rangle$ | **4462** | 4471 (Sidebottom_2026-11-22:large) | **-9** | 2.77498 (2.77564) | `Z[1/2,1/7,1/29]` | `21x21x21_r4723.npz` | `schemes_large/20x21x21_m4462_Q.json.gz` |
| $\langle 20\times 21\times 22\rangle$ | **4897** | 4987 (Sidebottom_2026-11-22:large) | **-90** | 2.79140 (2.79739) | `Z[1/2,1/3,1/11]` | `22x22x22_r5141.npz` | `schemes_large/20x21x22_m4897_Q.json.gz` |
| $\langle 20\times 22\times 22\rangle$ | **4970** | 5005 (Sidebottom_2026-11-22:large) | **-35** | 2.78209 (2.78439) | `Z[1/2,1/3,1/11]` | `22x22x22_r5141.npz` | `schemes_large/20x22x22_m4970_Q.json.gz` |
| $\langle 20\times 23\times 23\rangle$ | **5495** | 5554 (Sidebottom_2026-11-22:large) | **-59** | 2.78791 (2.79137) | `Z[1/2,1/3,1/11]` | `23x23x23_r6009.npz` | `schemes_large/20x23x23_m5495_Q.json.gz` |
| $\langle 21\times 21\times 22\rangle$ | **4991** | 5009 (Sidebottom_2026-11-22:large) | **-18** | 2.78278 (2.78396) | `Z[1/2,1/3,1/11]` | `22x22x22_r5141.npz` | `schemes_large/21x21x22_m4991_Q.json.gz` |
| $\langle 21\times 22\times 22\rangle$ | **5060** | 5082 (Sidebottom_2026-11-22:large) | **-22** | 2.77321 (2.77463) | `Z[1/2,1/3,1/11]` | `22x22x22_r5141.npz` | `schemes_large/21x22x22_m5060_Q.json.gz` |
| $\langle 21\times 22\times 23\rangle$ | **5333** | 5344 (Sidebottom_2026-11-22:large) | **-11** | 2.77692 (2.77759) | `Z[1/2,1/3,1/11]` | `23x23x23_r6009.npz` | `schemes_large/21x22x23_m5333_Q.json.gz` |
| $\langle 21\times 23\times 23\rangle$ | **5608** | 5628 (Sidebottom_2026-11-22:large) | **-20** | 2.77986 (2.78101) | `Z[1/2,1/3,1/11]` | `23x23x23_r6009.npz` | `schemes_large/21x23x23_m5608_Q.json.gz` |
| $\langle 22\times 22\times 23\rangle$ | **5413** | 5423 (Sidebottom_2026-11-22:large) | **-10** | 2.76785 (2.76845) | `Z[1/2,1/3,1/11]` | `23x23x23_r6009.npz` | `schemes_large/22x22x23_m5413_Q.json.gz` |
| $\langle 22\times 23\times 23\rangle$ | **5700** | 5710 (Sidebottom_2026-11-22:large) | **-10** | 2.77126 (2.77183) | `Z[1/2,1/3,1/11]` | `23x23x23_r6009.npz` | `schemes_large/22x23x23_m5700_Q.json.gz` |
