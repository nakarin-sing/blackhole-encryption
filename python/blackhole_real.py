# python/blackhole_real.py
import ctypes
import secrets
from typing import Tuple

lib = ctypes.CDLL('./libbh_core.so')
lib.parallel_encrypt.argtypes = [ctypes.POINTER(ctypes.c_uint8), ctypes.c_size_t, ctypes.POINTER(ctypes.c_uint8),
                                 ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_uint8)]

def singularity_encrypt(data: bytes) -> Tuple[bytes, bytes]:
    key = secrets.token_bytes(32)
    nonce = secrets.token_bytes(12)
    out = (ctypes.c_uint8 * len(data)).from_buffer_copy(data)
    lib.parallel_encrypt(out, len(data), out, key, nonce)
    return bytes(out), nonce

if __name__ == "__main__":
    data = b"Hello, Open Source World!"
    ct, nonce = singularity_encrypt(data)
    print(f"Encrypted: {ct.hex()}")
