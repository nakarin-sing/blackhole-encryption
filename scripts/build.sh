#!/bin/bash
set -e

# Install Deps (Ubuntu/macOS)
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    sudo apt-get install libsodium-dev libblake3-dev cmake g++ clang
elif [[ "$OSTYPE" == "darwin"* ]]; then
    brew install libsodium cmake
fi

# Submodules
git submodule update --init --recursive  # For kyber, schifra, etc.

# Build
mkdir build && cd build
cmake ..
make -j$(nproc)

# Python
cd ../python && python3 setup.py build_ext --inplace

echo "Build complete! Run: python3 python/blackhole_real.py"
