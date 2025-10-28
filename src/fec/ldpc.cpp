// src/fec/ldpc.cpp
#include "LdpcCode.h"  // From tavildar/LDPC

class LDPCFEC {
public:
    LdpcCode ldpc;  // Initialize with params (e.g., rate 1/2)

    bool encode(const uint8_t* data, size_t len, std::vector<uint8_t>& parity) {
        std::vector<uint8_t> codeword = ldpc.encode(data, len);
        parity.assign(codeword.begin() + len, codeword.end());
        return true;
    }

    bool decode(uint8_t* data, const uint8_t* parity, size_t len) {
        std::vector<uint8_t> codeword(len + parity->size());
        std::copy(data, data + len, codeword.begin());
        std::copy(parity, parity + parity->size(), codeword.begin() + len);
        return ldpc.decode(codeword.data(), codeword.size()) == 0;  // 0 = success
    }
};
