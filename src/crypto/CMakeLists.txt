cmake_minimum_required(VERSION 3.16)
project(BlackHoleV218)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Dependencies (Open Source Libs)
find_package(PkgConfig REQUIRED)
pkg_check_modules(SODIUM REQUIRED libsodium)
pkg_check_modules(BLAKE3 REQUIRED blake3)  # Assume installed

# Submodules (git submodule add URLs)
add_subdirectory(extern/kyber)  # PQClean Kyber
add_subdirectory(extern/schifra)  # RS
add_subdirectory(extern/ldpc)  # tavildar/LDPC
add_subdirectory(extern/openrq)  # Tornado

# Core Lib
add_library(bh_core SHARED
    src/crypto/chacha20.cpp
    src/core/bh_neptunian.cpp
    src/core/bh_quantum_tweak.cpp
    src/fec/reedsolomon.cpp
    src/fec/ldpc.cpp
    src/fec/tornado.cpp
)
target_link_libraries(bh_core sodium blake3 kyber schifra ldpc openrq)

# SYCL GPU (Optional - Intel oneAPI)
find_package(IntelSYCL)  # If installed
if(IntelSYCL_FOUND)
    add_library(bh_gpu SHARED src/gpu/bh_self_healing_gpu.sycl)
    target_link_libraries(bh_gpu sycl)
endif()

# Executable
add_executable(bh_test tests/test_main.cpp)
target_link_libraries(bh_test bh_core)

# Install
install(TARGETS bh_core bh_test DESTINATION lib)
