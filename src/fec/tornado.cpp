// src/fec/tornado.cpp
#include "openrq.h"  // From OpenRQ lib

class TornadoFEC {
public:
    static bool encode(const uint8_t* data, size_t len, std::vector<uint8_t>& parity, int symbols) {
        rq_encoder encoder = rq_encoder_create(len / 1450, symbols);  // Block size
        rq_encoder_add_source_block(encoder, data, len);
        rq_encoder_encode(encoder, parity.data(), symbols * 1450);
        rq_encoder_destroy(encoder);
        return true;
    }

    static bool decode(uint8_t* data, const uint8_t* parity, size_t len, int symbols) {
        rq_decoder decoder = rq_decoder_create(len / 1450, symbols);
        rq_decoder_add_source_block(decoder, data, len);
        rq_decoder_decode(decoder, parity, symbols * 1450);
        rq_decoder_destroy(decoder);
        return true;
    }
};
