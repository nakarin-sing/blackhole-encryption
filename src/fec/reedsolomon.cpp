// src/fec/reedsolomon.cpp (Integrate Schifra header)
#include "schifra_reed_solomon_encoder.hpp"
#include "schifra_reed_solomon_decoder.hpp"

class ReedSolomonFEC {
public:
    static bool encode(const uint8_t* data, size_t len, std::vector<uint8_t>& parity) {
        schifra::reed_solomon::encoder<255, 223, 8, 0x11d> rs_encoder(8);
        std::vector<uint8_t> block(255, 0);
        std::copy(data, data + std::min(len, size_t(223)), block.begin());
        rs_encoder.encode(block.data(), block.size());
        parity.assign(block.begin() + 223, block.end());
        return true;
    }

    static bool decode(uint8_t* data, const uint8_t* parity, size_t len) {
        schifra::reed_solomon::decoder<255, 223, 8, 0x11d> rs_decoder(8);
        std::vector<uint8_t> block(255);
        std::copy(data, data + len, block.begin());
        std::copy(parity, parity + 32, block.begin() + 223);
        return rs_decoder.decode(block.data());
    }
};
