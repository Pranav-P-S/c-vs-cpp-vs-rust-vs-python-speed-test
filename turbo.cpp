// turbopp.cpp
#include <cstdint>

// 1. extern "C" -> Stops C++ name mangling (keeps it "heavy_computation")
// 2. __declspec(dllexport) -> Exports it from the DLL on Windows
extern "C" __declspec(dllexport) unsigned long long heavy_computation(unsigned long long n) {
    unsigned long long sum = 0;
    
    for (unsigned long long i = 0; i < n; i++) {
        // The logic matches our C and Rust implementations
        sum += (i * i) % 2345;
    }
    
    return sum;
}