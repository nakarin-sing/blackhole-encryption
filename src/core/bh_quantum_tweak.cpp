// src/core/bh_quantum_tweak.cpp
#include <blake3.h>
#include "kyber/kyber.h"  // PQClean

void generate_tweak(const uint8_t* seed, uint8_t* out) {
    blake3_hasher hasher;
    blake3_hasher_init_keyed(&hasher, seed, 32);  // Kyber seed
    blake3_hasher_update(&hasher, seed, 32);
    blake3_hasher_finalize(&hasher, out, 32);
}
