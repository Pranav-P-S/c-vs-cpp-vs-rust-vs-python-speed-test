import ctypes
import time
import os

# Configuration
N = 100_000_000  # 100 Million
print(f"--- 🏁 THE ULTIMATE RACE: Counting to {N:,} 🏁 ---")

def load_lib(name, path):
    """Helper to safely load a DLL and configure arguments"""
    full_path = os.path.join(os.getcwd(), path)
    try:
        lib = ctypes.CDLL(full_path)
        # Configure arguments for 64-bit Unsigned Int (unsigned long long / u64)
        lib.heavy_computation.argtypes = [ctypes.c_ulonglong]
        lib.heavy_computation.restype = ctypes.c_ulonglong
        return lib
    except OSError:
        return None

# --- LOAD CONTENDERS ---
c_lib    = load_lib("C", "turbo.dll")
cpp_lib  = load_lib("C++", "turbopp.dll")
# Adjust this path if your rust build is elsewhere
rust_lib = load_lib("Rust", os.path.join("rust_turbo", "target", "release", "rust_turbo.dll"))

results = {}

# --- 1. PYTHON (The Baseline) ---
print("Running Python...", end="", flush=True)
start = time.perf_counter()
py_sum = 0
for i in range(N):
    py_sum += (i * i) % 2345
py_time = time.perf_counter() - start
results['Python'] = (py_time, py_sum)
print(f"\r🐍 Python Time: {py_time:.4f} sec | Result: {py_sum}")

# --- 2. C ---
if c_lib:
    print("Running C...", end="", flush=True)
    start = time.perf_counter()
    c_sum = c_lib.heavy_computation(N)
    c_time = time.perf_counter() - start
    results['C'] = (c_time, c_sum)
    speedup = py_time / c_time
    print(f"\r🔵 C Time:      {c_time:.4f} sec | Result: {c_sum} | {speedup:.1f}x faster")
else:
    print("\n🔵 C: Skipped (turbo.dll not found)")

# --- 3. C++ ---
if cpp_lib:
    print("Running C++...", end="", flush=True)
    start = time.perf_counter()
    cpp_sum = cpp_lib.heavy_computation(N)
    cpp_time = time.perf_counter() - start
    results['C++'] = (cpp_time, cpp_sum)
    speedup = py_time / cpp_time
    print(f"\r🟣 C++ Time:    {cpp_time:.4f} sec | Result: {cpp_sum} | {speedup:.1f}x faster")
else:
    print("\n🟣 C++: Skipped (turbopp.dll not found)")

# --- 4. RUST ---
if rust_lib:
    print("Running Rust...", end="", flush=True)
    start = time.perf_counter()
    rust_sum = rust_lib.heavy_computation(N)
    rust_time = time.perf_counter() - start
    results['Rust'] = (rust_time, rust_sum)
    speedup = py_time / rust_time
    print(f"\r🦀 Rust Time:   {rust_time:.4f} sec | Result: {rust_sum} | {speedup:.1f}x faster")
else:
    print("\n🦀 Rust: Skipped (rust_turbo.dll not found)")

# --- VERIFICATION ---
print("\n--- 🔍 Integrity Check ---")
reference = results['Python'][1]
all_match = True
for lang, (t, res) in results.items():
    if res != reference:
        print(f"❌ {lang} Result MISMATCH! Expected {reference}, got {res}")
        all_match = False
    
if all_match:
    print("✅ All calculations match perfectly!")