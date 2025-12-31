# 🏎️ The FFI Speed Race: Python vs C vs C++ vs Rust

A high-performance benchmark comparing the execution speed of Python against compiled languages (C, C++, and Rust) using Foreign Function Interfaces (FFI).

This project demonstrates how to optimize slow Python loops by offloading heavy computations to shared libraries (`.dll` / `.so`) written in system-level languages.

## 🧪 The Experiment
We calculate the sum of a mathematical sequence for **100 Million iterations**:

$$\sum_{i=0}^{99,999,999} ((i \times i) \pmod{2345})$$

* **Logic:** The modulo operator `% 2345` is used to prevent compiler optimizations (like loop deletion) and force the CPU to perform the actual work.
* **Data Types:** All implementations use **64-bit Unsigned Integers** (`unsigned long long` / `u64`) to handle large numbers and wrapping behavior.

---

## 📊 Benchmark Results

Running on a standard Windows x64 machine (MSYS2 environment):

| Language | Type | Execution Time | Speedup |
| :--- | :--- | :--- | :--- |
| **Python** | Interpreted | ~9.50 sec | 1x (Baseline) |
| **C** | Compiled (GCC) | ~0.09 sec | **~102x** |
| **C++** | Compiled (G++) | ~0.09 sec | **~104x** |
| **Rust** | Compiled (LLVM) | ~0.09 sec | **~100x** |

**Conclusion:** Native compiled languages are approximately **100x faster** than Python for raw mathematical loops.

---

## 📂 Project Structure

```text
├── race.py           # The "Master" driver script (Python)
├── turbo.c           # C implementation (Exports turbo.dll)
├── turbopp.cpp       # C++ implementation (Exports turbopp.dll)
├── rust_turbo/       # Rust Cargo project
│   └── src/lib.rs    # Rust implementation (Exports rust_turbo.dll)
└── README.md         # Documentation
