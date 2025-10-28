// src/crypto/chacha20.cpp
#include <sodium.h>
#include <vector>

std::vector<uint8_t> chacha20_encrypt(const std::vector<uint8_t>& plaintext,
                                      const std::vector<uint8_t>& key,
                                      const std::vector<uint8_t>& nonce) {
    if (key.size() != crypto_stream_chacha20_KEYBYTES ||
        nonce.size() != crypto_stream_chacha20_NONCEBYTES) {
        throw std::invalid_argument("Invalid key/nonce size");
    }
    std::vector<uint8_t> ciphertext(plaintext.size());
    if (crypto_stream_chacha20_xor(ciphertext.data(), plaintext.data(),
                                   plaintext.size(), nonce.data(), key.data()) != 0) {
        throw std::runtime_error("Encryption failed");
    }
    return ciphertext;
}
