// src/lib.rs

#[unsafe(no_mangle)]
pub extern "C" fn heavy_computation(n: u64) -> u64 {
    let mut sum: u64 = 0;
    
    for i in 0..n {
        // 1. i.wrapping_mul(i) -> Handles overflow if i*i > 2^64
        // 2. % 2345 -> Reduces the number
        // 3. sum.wrapping_add(...) -> Adds to sum, wrapping if it overflows
        sum = sum.wrapping_add(i.wrapping_mul(i) % 2345);
    }
    
    sum
}