# benchmarks/benchmark_core.py
import time
import secrets
import matplotlib.pyplot as plt
from python.blackhole_real import singularity_encrypt
import numpy as np

def benchmark_encrypt(size_mb):
    data = secrets.token_bytes(size_mb * 1024 * 1024)
    start = time.time()
    ct, nonce = singularity_encrypt(data)
    end = time.time()
    speed = size_mb / (end - start)
    print(f"{size_mb} MB → {speed:.2f} GB/s")
    return speed

sizes = [1, 10, 50, 100, 500, 1000]
speeds = [benchmark_encrypt(s) for s in sizes]

# Plot
plt.plot(sizes, speeds, 'o-')
plt.xlabel("Data Size (MB)")
plt.ylabel("Throughput (GB/s)")
plt.title("Black Hole Encryption Benchmark")
plt.grid(True)
plt.savefig("results/benchmark_plot.png")
print("Plot saved: results/benchmark_plot.png")
