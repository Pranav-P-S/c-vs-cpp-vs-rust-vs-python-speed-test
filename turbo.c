// turbo.c
#include <stdint.h> // For precise integer types

// On Windows, we need dllexport. On Linux, we don't, but this macro handles it.
#ifdef _WIN32
    #define EXPORT __declspec(dllexport)
#else
    #define EXPORT
#endif

// We use 'unsigned long long' to guarantee 64 bits on Windows
EXPORT unsigned long long heavy_computation(unsigned long long n) {
    unsigned long long sum = 0;
    
    for (unsigned long long i = 0; i < n; i++) {
        // In C, unsigned math wraps automatically!
        sum += (i * i) % 2345;
    }
    
    return sum;
}