# tests/test_fec.py
import pytest
from ctypes import *

# Assume libbh_core.so loaded
def test_rs_recovery():
    data = b"A" * 223
    # Simulate encode/decode via lib
    # ... (call encode/decode)
    assert recovered == data  # Placeholder for real call

pytest.main()
