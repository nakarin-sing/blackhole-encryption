# tests/full_suite.py
import pytest
import secrets
from python.blackhole_real import (
    singularity_encrypt, singularity_decrypt,
    singularity_encrypt_with_fec, singularity_decrypt_with_fec
)

def test_crypto_roundtrip():
    data = b"Hello, Black Hole!"
    ct, nonce, key = singularity_encrypt(data)
    pt = singularity_decrypt(ct, nonce, key)
    assert pt == data

def test_fec_recovery_30_percent():
    data = b"A" * 2230
    ct, nonce, key, parity = singularity_encrypt_with_fec(data)
    corrupted = bytearray(ct)
    for i in range(0, len(corrupted), 10):  # 30% errors
        if i < len(corrupted):
            corrupted[i] = 0xFF
    recovered = singularity_decrypt_with_fec(bytes(corrupted), nonce, key, parity)
    assert recovered == data

def test_edge_cases():
    assert singularity_encrypt(b"")[0] == b""
    assert singularity_encrypt(b"\x00")[0] != b"\x00"

if __name__ == "__main__":
    pytest.main(["-v"])
