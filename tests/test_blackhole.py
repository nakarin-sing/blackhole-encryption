# tests/test_blackhole.py
import pytest
import secrets
from blackhole_v23 import BlackHoleV23

@pytest.fixture
def bh():
    return BlackHoleV23()

def test_round_trip_small(bh):
    data = b"Hello, Black Hole!"
    ct, nonce, key, tag, parity = bh.encrypt(data)
    recovered = bh.decrypt(ct, nonce, key, tag, parity)
    assert recovered == data

def test_round_trip_large(bh):
    data = secrets.token_bytes(10 * 1024 * 1024)  # 10 MB
    ct, nonce, key, tag, parity = bh.encrypt(data)
    recovered = bh.decrypt(ct, nonce, key, tag, parity)
    assert recovered == data

def test_corruption_detection(bh):
    data = b"Secret Message"
    ct, nonce, key, tag, parity = bh.encrypt(data)
    
    # Corrupt ciphertext
    corrupted = bytearray(ct)
    corrupted[0] ^= 0xFF
    corrupted = bytes(corrupted)
    
    recovered = bh.decrypt(corrupted, nonce, key, tag, parity)
    assert recovered != data  # Should fail or recover

def test_invalid_tag(bh):
    data = b"Test"
    ct, nonce, key, tag, parity = bh.encrypt(data)
    bad_tag = bytearray(tag)
    bad_tag[0] ^= 0xFF
    with pytest.raises(ValueError):
        bh.decrypt(ct, nonce, key, bytes(bad_tag), parity)
