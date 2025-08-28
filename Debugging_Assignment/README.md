## 🛠 Debug Challenge: Decode & Rotate

Welcome to the Autotronics Research Lab Debugging Mission 🎯
Your task is to debug both the C++ source code and the CMake build system until the program builds and runs successfully.

## ⚡ How to Build

Create a build directory and enter it:

```bash
mkdir build && cd build
```
Configure the project with CMake:

```bash
cmake ..
```
Build the project:
```bash
make
```

# ⚠️ You will see errors — your mission is to fix them in both main.cpp and CMakeLists.txt.

# Extra Notes
## Mission: Decode & Rotate
This task is designed to test your ability to identify and fix bugs in C++ code.  
The file contains **three levels of bugs**, each tied to a specific concept or algorithm:  

- **Level 1 – Compilation & Header Management**  
  Errors such as missing includes, syntax mistakes, or incorrect namespace usage that prevent the program from compiling.  
  *Algorithm / Concept:* **C++ Compilation & Header Management**  

- **Level 2 – String Decoding Logic**  
  Problems in the message decoding function, which lead to incorrect string output.  
  *Algorithm / Concept:* **Character Encoding & String Construction**  
  

- **Level 3 – Rotation Matrix Transformation**  
  Mistakes in implementing a 2D/3D rotation using linear algebra. 
  *Algorithm / Concept:* **Rotation Matrix (Linear Algebra / Eigen Library)**  
  

The purpose of the task is not just to fix the code, but to **understand each bug, document your solution, and explain the reasoning**.  
This ensures you gain both **debugging skills** and a deeper understanding of **C++ programming, algorithms, and libraries like Eigen**.  


## 📦 What to Submit (Required)

### ✅ Corrected Source Files
- `main.cpp` (fixed)  
- `CMakeLists.txt` (fixed)  

### 📑 PDF Report Explaining All Issues and Fixes
- **Name it:** `<your_name>_DebugChallenge_Report.pdf`  
- Your report should include:
  - A **list of all errors/bugs** you found (compile-time, logic, algorithmic).  
  - For each bug: **symptom**, **root cause**, and **your fix** (with a short code snippet if helpful).  
  - **Reasoning/explanation** behind each fix (what concept was involved).  
  - **References/resources** you used (links, docs, articles, etc.).  

*(Optional but appreciated: a short note on how to run your final build and a screenshot or log of successful execution.)*

