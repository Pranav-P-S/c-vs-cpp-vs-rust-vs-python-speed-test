import ctypes
import time
import os

# Path to the Rust DLL inside the target/release folder
# Note: On Windows it's .dll, on Linux it's .so, on Mac it's .dylib
dll_path = os.path.join(os.getcwd(), "target", "release", "rust_turbo.dll")

print(f"Loading: {dll_path}")
rust_library = ctypes.CDLL(dll_path)

# Configure the function types (i64 in Rust = c_longlong in Python)
rust_library.heavy_computation.argtypes = [ctypes.c_longlong]
rust_library.heavy_computation.restype = ctypes.c_longlong

n = 100000000
print(f"--- The Race: Counting to {n} ---")

# --- CONTENDER 1: PYTHON ---
# Use perf_counter() instead of time()
start_py = time.perf_counter() 
py_sum = 0
for i in range(n):
    py_sum += i
end_py = time.perf_counter()
py_time = end_py - start_py
print(f"Python Time: {py_time:.6f} seconds")

# --- CONTENDER 2: RUST ---
start_rust = time.perf_counter()
rust_sum = rust_library.heavy_computation(n)
end_rust = time.perf_counter()
rust_time = end_rust - start_rust

# Prevent division by zero if it's STILL too fast
if rust_time < 1e-9: 
    rust_time = 1e-9 # Set to 1 nanosecond minimum

print(f"Rust Time:   {rust_time:.6f} seconds")

# Verify results
print(f"\nResults Match? {py_sum == rust_sum}")
speedup = py_time / rust_time
print(f"Speedup: {speedup:.0f}x faster!")