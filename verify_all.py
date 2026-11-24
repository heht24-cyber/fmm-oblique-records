"""
100% Standalone Exact Characteristic-0 Verifier for All FMM Schemes in This Repository.
Dependencies: Python 3.10+ standard library + numpy (ZERO external code!).

Usage:
    python verify_all.py
    python verify_all.py schemes_classic_le16/9x11x15_m949_dyadic.json.gz
"""
from __future__ import annotations

import gzip
import json
import math
import random
import sys
import time
from fractions import Fraction
from pathlib import Path

import numpy as np

CRT_PRIMES = [
    999_999_937, 999_999_929, 999_999_893, 999_999_883,
    999_999_797, 999_999_761, 999_999_757, 999_999_751,
    999_999_739, 999_999_733, 999_999_667, 999_999_613,
    999_999_599, 999_999_587, 999_999_541, 999_999_527,
]


def _lcm(a: int, b: int) -> int:
    return abs(a * b) // math.gcd(a, b) if a and b else max(abs(a), abs(b), 1)


def parse_frac(v) -> Fraction:
    if isinstance(v, int):
        return Fraction(v)
    s = str(v).strip()
    if "/" in s:
        a, b = s.split("/")
        return Fraction(int(a), int(b))
    return Fraction(s)


def load_scheme(path: Path):
    if path.suffix == ".gz":
        with gzip.open(path, "rt", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = json.loads(path.read_text(encoding="utf-8"))
    m, n, p = [int(x) for x in data["format"]]
    R = int(data["rank"])
    U = [{int(c): parse_frac(v) for c, v in row} for row in data["u_sparse"]]
    V = [{int(c): parse_frac(v) for c, v in row} for row in data["v_sparse"]]
    W = [{int(c): parse_frac(v) for c, v in row} for row in data["w_sparse"]]
    assert len(U) == R and len(V) == R and len(W) == R
    return data, (m, n, p, R), U, V, W


def verify_exact_crt(U, V, W, m: int, n: int, p: int) -> tuple[bool, str]:
    R = len(U)
    L1, L2, L3 = m * n, n * p, m * p

    def clear_d(rows):
        d = 1
        for row in rows:
            for fr in row.values():
                if fr.denominator != 1:
                    d = _lcm(d, fr.denominator)
        scaled = [{c: int(fr.numerator * (d // fr.denominator)) for c, fr in row.items()} for row in rows]
        infs = [max((abs(x) for x in row.values()), default=0) for row in scaled]
        return scaled, d, infs

    Ui, dU, infU = clear_d(U)
    Vi, dV, infV = clear_d(V)
    Wi, dW, infW = clear_d(W)
    D = dU * dV * dW
    B = D + sum(infU[r] * infV[r] * infW[r] for r in range(R))

    primes = []
    prod = 1
    for pr in CRT_PRIMES:
        primes.append(pr)
        prod *= pr
        if prod > 2 * B:
            break
    assert prod > 2 * B, f"Need more primes for bound B={B}"

    # 15-bit split float64 BLAS is mathematically bit-exact when R * 32767^2 < 2^52 (R < 4.19e6)!
    MASK15 = np.int64((1 << 15) - 1)
    assert R * (32767 * 32767) < (1 << 52)
    for pr in primes:
        Ua = np.zeros((R, L1), dtype=np.int64)
        Va = np.zeros((R, L2), dtype=np.int64)
        Wa = np.zeros((R, L3), dtype=np.int64)
        for r in range(R):
            for c, v in Ui[r].items(): Ua[r, c] = v % pr
            for c, v in Vi[r].items(): Va[r, c] = v % pr
            for c, v in Wi[r].items(): Wa[r, c] = v % pr
        D_mod = D % pr
        Wlo_all = (Wa & MASK15).astype(np.float64)
        Whi_all = (Wa >> np.int64(15)).astype(np.float64)
        for i in range(m):
            for j in range(n):
                a = i * n + j
                ua = Ua[:, a]
                nz = np.flatnonzero(ua)
                uv = (ua[nz, None] * Va[nz]) % pr
                uv_lo = (uv & MASK15).astype(np.float64)
                uv_hi = (uv >> np.int64(15)).astype(np.float64)
                Wlo = Wlo_all[nz]
                Whi = Whi_all[nz]
                p0 = np.rint(uv_lo.T @ Wlo).astype(np.int64) % pr
                p1 = (np.rint(uv_lo.T @ Whi).astype(np.int64) + np.rint(uv_hi.T @ Wlo).astype(np.int64)) % pr
                p2 = np.rint(uv_hi.T @ Whi).astype(np.int64) % pr
                sl = (p0 + ((p1 << np.int64(15)) % pr) + ((p2 << np.int64(30)) % pr)) % pr
                for k in range(p):
                    sl[j * p + k, i * p + k] = (sl[j * p + k, i * p + k] - D_mod) % pr
                if np.any(sl != 0):
                    return False, f"Brent equation mismatch at ({i},{j}) mod {pr}"
    return True, f"EXACT Q PROVED ({len(primes)} CRT primes, prod>{2*B:.2e}, D={D})"


def verify_exact_fraction_trials(U, V, W, m: int, n: int, p: int, trials: int = 2) -> bool:
    rng = random.Random(20261124)
    for _ in range(trials):
        A = [Fraction(rng.randint(-40, 40)) for _ in range(m * n)]
        B = [Fraction(rng.randint(-40, 40)) for _ in range(n * p)]
        C = [Fraction(0)] * (m * p)
        for r in range(len(U)):
            sa = sum((v * A[c] for c, v in U[r].items()), Fraction(0))
            if not sa: continue
            sb = sum((v * B[c] for c, v in V[r].items()), Fraction(0))
            if not sb: continue
            pr = sa * sb
            for c, v in W[r].items():
                C[c] += pr * v
        for i in range(m):
            for k in range(p):
                if C[i * p + k] != sum((A[i * n + j] * B[j * p + k] for j in range(n)), Fraction(0)):
                    return False
    return True


def main():
    root = Path(__file__).resolve().parent
    if len(sys.argv) > 1:
        files = [Path(a) for a in sys.argv[1:]]
    else:
        files = sorted(root.glob("schemes_*/*.json.gz"))
    print(f"Verifying {len(files)} exact Characteristic-0 FMM scheme(s)...")
    n_pass = 0
    for fp in files:
        t0 = time.perf_counter()
        data, (m, n, p, R), U, V, W = load_scheme(fp)
        ok_crt, msg = verify_exact_crt(U, V, W, m, n, p)
        ok_fr = verify_exact_fraction_trials(U, V, W, m, n, p, trials=2)
        U_bad = [dict(r) for r in U]
        k0 = next(iter(U_bad[0].keys()))
        U_bad[0][k0] += Fraction(1)
        ok_bad, _ = verify_exact_crt(U_bad, V, W, m, n, p)
        dt = time.perf_counter() - t0
        ok = ok_crt and ok_fr and (not ok_bad)
        if ok:
            n_pass += 1
        print(f"  [{'PASS' if ok else 'FAIL'}] {fp.name:36s} <{m:2d}x{n:2d}x{p:2d}: R={R:5d}> | {msg} ({dt:.2f}s)")
    print(f"\nSUMMARY: {n_pass}/{len(files)} schemes 100% verified over exact Q (Characteristic 0).")
    sys.exit(0 if n_pass == len(files) else 1)


if __name__ == "__main__":
    main()
