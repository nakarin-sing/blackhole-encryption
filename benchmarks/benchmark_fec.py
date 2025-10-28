# benchmarks/benchmark_fec.py
import random
from python.blackhole_real import singularity_encrypt, singularity_decrypt_with_fec

def inject_errors(data, error_rate):
    data = bytearray(data)
    for i in range(len(data)):
        if random.random() < error_rate:
            data[i] = random.randint(0, 255)
    return bytes(data)

def benchmark_recovery(error_rates=[0.1, 0.2, 0.3, 0.4]):
    data = b"A" * (223 * 100)  # 100 RS blocks
    ct, nonce, key, parity = singularity_encrypt_with_fec(data)
    
    results = []
    for rate in error_rates:
        corrupted = inject_errors(ct, rate)
        try:
            recovered = singularity_decrypt_with_fec(corrupted, nonce, key, parity)
            success = recovered == data
            results.append((rate, success))
            print(f"Error {rate*100:.1f}% → Recovery: {'SUCCESS' if success else 'FAIL'}")
        except:
            results.append((rate, False))
            print(f"Error {rate*100:.1f}% → FAIL (crash)")
    
    return results

benchmark_recovery()
