#!/bin/bash
set -e

echo "BLACK HOLE ENCRYPTION — FULL TEST & BENCHMARK"
echo "============================================"

# Build
echo "[1] Building..."
./scripts/build.sh

# Unit Tests
echo "[2] Running Tests..."
python3 -m pytest tests/full_suite.py -v

# Benchmark Crypto
echo "[3] Benchmarking Crypto..."
python bất benchmarks/benchmark_core.py

# Benchmark FEC
echo "[4] Benchmarking FEC Recovery..."
python3 benchmarks/benchmark_fec.py

# GPU (if SYCL)
if command -v sycl-ls &> /dev/null; then
    echo "[5] Running GPU Kernel..."
    ./build/bh_gpu_test
fi

echo "ALL TESTS & BENCHMARKS PASSED!"
echo "Results saved in: results/"
