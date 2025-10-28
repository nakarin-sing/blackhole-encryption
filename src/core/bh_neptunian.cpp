// src/core/bh_neptunian.cpp
#include <thread>
#include <vector>
#include "crypto/chacha20.cpp"  // Include

void parallel_encrypt(const uint8_t* in, size_t len, uint8_t* out,
                      const uint8_t* key, const uint8_t* nonce) {
    size_t num_threads = std::thread::hardware_concurrency();
    size_t chunk = len / num_threads;
    std::vector<std::thread> threads;
    for (size_t t = 0; t < num_threads; ++t) {
        size_t offset = t * chunk;
        threads.emplace_back([in, out, key, nonce, offset, chunk]() {
            uint8_t local_nonce[12];
            std::memcpy(local_nonce, nonce, 12);
            local_nonce[11] ^= t;  // Per-thread nonce
            chacha20_encrypt(in + offset, std::min(chunk, len - offset), out + offset, key, local_nonce);
        });
    }
    for (auto& th : threads) th.join();
}
