# Quantum Random Number Generator (QRNG)

### Quantum-Based Random Bit Generation, Debiasing and Statistical Randomness Evaluation

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Qiskit](https://img.shields.io/badge/Qiskit-Quantum%20Computing-purple)
![Status](https://img.shields.io/badge/Project-Completed-success)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 1. Project Overview

The **Quantum Random Number Generator (QRNG)** is a Python-based project that demonstrates quantum circuit-based random bit generation using Qiskit.

Unlike conventional pseudo-random number generators, which rely on deterministic mathematical algorithms, this project uses quantum measurement outcomes to generate binary sequences.

A Hadamard gate is applied to a qubit initialized in the zero state, creating an equal superposition of the computational basis states. Measuring the qubit produces either 0 or 1 with an ideal probability of 50% each.

The generated binary sequence is processed using the Von Neumann debiasing algorithm to reduce simple statistical bias. The raw and debiased datasets are subsequently evaluated using four selected statistical tests based on the NIST SP 800-22 framework.

The project also includes data visualization, comparative analysis and an interactive HTML dashboard.

**Note:** The current implementation uses the Qiskit Aer quantum simulator. It does not collect measurement data from physical quantum hardware.

---

## 2. Problem Statement

Traditional pseudo-random number generators produce sequences using deterministic algorithms. Although they are widely used, their outputs are not fundamentally random.

Quantum mechanics provides an alternative approach through the probabilistic nature of quantum measurement.

The objective of this project is to develop a quantum circuit-based random number generation system that generates binary sequences, applies statistical debiasing, evaluates randomness properties and presents the results through an interactive visualization dashboard.

---

## 3. Project Objectives

The main objectives are:

1. Understand and implement quantum superposition using Qiskit.
2. Generate 10,000 binary measurement outcomes using a Hadamard gate.
3. Store generated random bits in CSV format.
4. Analyse the distribution of zeros and ones.
5. Implement Von Neumann debiasing to reduce simple probability bias.
6. Perform selected statistical randomness tests based on NIST SP 800-22.
7. Compare raw and debiased random bit sequences.
8. Generate graphical representations of statistical results.
9. Develop an interactive dashboard for result analysis.
10. Automate the complete project execution using a master Python script.

---

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Qiskit | Quantum circuit creation |
| Qiskit Aer | Quantum circuit simulation |
| NumPy | Numerical computations |
| Pandas | Dataset processing |
| Matplotlib | Static data visualization |
| SciPy | Statistical calculations |
| Plotly | Interactive visualizations |
| VS Code | Development environment |

---

## 5. System Architecture

The project follows a modular processing architecture.

```text
             START
               |
               v
      Quantum Circuit Creation
               |
               v
       Initialize One Qubit
               |
               v
        Apply Hadamard Gate
               |
               v
         Qubit Measurement
               |
               v
       Generate 10,000 Bits
               |
               v
       Save Raw Bit Dataset
               |
               v
       Data Visualization
               |
               v
       Von Neumann Debiasing
               |
               v
      Save Debiased Dataset
               |
               v
      NIST Statistical Testing
               |
               v
      Raw vs Debiased Analysis
               |
               v
       Interactive Dashboard
               |
               v
              END
```

---

## 6. Quantum Computing Concepts

### 6.1 Qubit

A qubit is the fundamental unit of quantum information.

A general single-qubit state can be represented as:

\[
|\psi\rangle=\alpha|0\rangle+\beta|1\rangle
\]

Where:

- \(|0\rangle\) represents the zero state.
- \(|1\rangle\) represents the one state.
- \(\alpha\) and \(\beta\) represent probability amplitudes.

The normalization condition is:

\[
|\alpha|^2+|\beta|^2=1
\]

### 6.2 Superposition

Superposition allows a qubit to exist in a combination of quantum states.

The project uses superposition to obtain measurement outcomes with equal theoretical probabilities.

### 6.3 Hadamard Gate

The Hadamard gate is applied to the initial zero state.

Its mathematical representation is:

\[
H=\frac{1}{\sqrt{2}}
\begin{bmatrix}
1&1\\
1&-1
\end{bmatrix}
\]

Applying the gate:

\[
H|0\rangle=
\frac{|0\rangle+|1\rangle}{\sqrt{2}}
\]

Therefore:

\[
P(0)=0.5
\]

\[
P(1)=0.5
\]

Measurement produces one binary outcome for each execution.

---

## 7. Algorithms Implemented

### 7.1 Quantum Random Bit Generation

The generator performs the following operations:

1. Initialize a quantum circuit with one qubit and one classical bit.
2. Apply a Hadamard gate to the qubit.
3. Measure the qubit.
4. Execute the circuit for 10,000 shots.
5. Retrieve individual measurement outcomes.
6. Convert measurement results into binary values.
7. Store the generated bits in a CSV file.

Output:

`data/quantum_random_bits.csv`

### 7.2 Von Neumann Debiasing

The Von Neumann algorithm processes binary values in pairs.

| Input Pair | Operation | Output |
|---|---|---|
| 00 | Discard | None |
| 11 | Discard | None |
| 01 | Retain | 0 |
| 10 | Retain | 1 |

The algorithm helps remove simple probability bias when input bits are independent and identically distributed.

The resulting sequence is saved as:

`data/debiased_random_bits.csv`

### 7.3 Statistical Randomness Testing

Four selected statistical tests based on NIST SP 800-22 are implemented.

**1. Frequency (Monobit) Test**

Evaluates whether the proportion of zeros and ones is approximately balanced.

**2. Block Frequency Test**

Examines the proportion of ones within fixed-size blocks of the sequence.

**3. Runs Test**

Evaluates the number of consecutive runs of identical bits.

**4. Approximate Entropy Test**

Examines the frequency of overlapping binary patterns to assess sequence regularity.

The significance level used is:

\[
\alpha=0.01
\]

Decision rule:

- PASS: p-value ≥ 0.01
- FAIL: p-value < 0.01

A passing result means the test does not find sufficient evidence against the tested randomness property. It does not prove true randomness or cryptographic security.

These are four selected tests, not a complete implementation of all 15 tests in the NIST SP 800-22 suite.

---

## 8. Data Visualization

The project generates three visualization graphs.

### Graph 1: Bit Distribution

Displays the frequency of zeros and ones in the generated dataset.

File:

`results/bit_distribution.png`

### Graph 2: Probability Convergence

Shows how the cumulative probability of obtaining a one changes as the number of measurements increases.

File:

`results/probability_convergence.png`

### Graph 3: Random Bit Sequence

Displays the first 200 generated bits as a binary visualization.

File:

`results/random_bit_sequence.png`

---

## 9. Interactive Dashboard

An interactive HTML dashboard is generated using Plotly.

The dashboard includes:

- Total number of raw bits.
- Number of debiased bits.
- Debiasing efficiency.
- NIST test pass summary.
- Raw versus debiased bit distribution.
- Statistical p-value comparison.
- Cumulative probability visualization.
- NIST pass/fail summary.

Dashboard location:

`results/dashboard.html`

Open this file in a web browser to view the analysis.

---

## 10. Project Folder Structure

```text
Quantum-Random-Generator/
│
├── main.py
│
├── visualize.py
│
├── debias.py
│
├── nist_testing.py
│
├── dashboard.py
│
├── run_all.py
│
├── requirements.txt
│
├── README.md
│
├── data/
│   ├── quantum_random_bits.csv
│   └── debiased_random_bits.csv
│
└── results/
    ├── bit_distribution.png
    ├── probability_convergence.png
    ├── random_bit_sequence.png
    ├── analysis_summary.csv
    ├── debiasing_summary.csv
    ├── nist_test_results.csv
    └── dashboard.html
```

---

## 11. Installation and Setup

### Prerequisites

- Python 3.x
- Visual Studio Code
- pip package manager

### Step 1: Clone the Repository

```bash
git clone https://github.com/Shabareesh29/Quantum-Random-Generator.git
```

Navigate to the project folder:

```bash
cd Quantum-Random-Generator
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Execute the Project

Run the master execution file:

```bash
python run_all.py
```

The master script automatically executes:

1. Quantum random bit generation.
2. Data visualization.
3. Von Neumann debiasing.
4. NIST statistical testing.
5. Dashboard generation.

### Step 4: Open the Dashboard

After successful execution, open:

```text
results/dashboard.html
```

---

## 12. Experimental Results

The following results represent one successful execution of the project.

### Raw Quantum Bit Generation

| Metric | Result |
|---|---:|
| Total bits generated | 10,000 |
| Zeros | 4,960 |
| Ones | 5,040 |
| Zero percentage | 49.60% |
| One percentage | 50.40% |

### Von Neumann Debiasing Results

| Metric | Result |
|---|---:|
| Original bits | 10,000 |
| Retained pairs | 2,440 |
| Discarded pairs | 2,560 |
| Debiased bits | 2,440 |
| Debiased zeros | 1,242 |
| Debiased ones | 1,198 |
| Zero percentage | 50.90% |
| One percentage | 49.10% |
| Debiasing efficiency | 48.80% |

### NIST Statistical Testing Results

The following results were obtained from the same execution.

| Statistical Test | Raw Data | Debiased Data |
|---|---|---|
| Frequency Test | PASS | PASS |
| Block Frequency Test | PASS | PASS |
| Runs Test | PASS | PASS |
| Approximate Entropy Test | PASS | PASS |

Significance level: 0.01

All eight test evaluations passed during this execution.

The results indicate that the tested datasets did not show statistically significant deviations under the four implemented tests.

**Note:** These results are specific to one simulator execution. New executions can produce different measurement counts and p-values.

---

## 13. Advantages

- Demonstrates quantum circuit-based random bit generation.
- Provides practical experience with Qiskit.
- Implements a simple debiasing technique.
- Evaluates multiple statistical properties of binary sequences.
- Provides automated data processing.
- Includes interactive visualization.
- Uses a modular and reusable Python architecture.

---

## 14. Limitations

1. The current implementation uses a quantum simulator rather than physical quantum hardware.
2. Only four selected NIST-style statistical tests are implemented.
3. The generated sequences contain a limited number of bits.
4. Von Neumann debiasing reduces simple probability bias but does not eliminate every possible correlation.
5. Passing statistical tests does not establish cryptographic security.
6. The current implementation is an experimental demonstration rather than a certified quantum entropy source.

---

## 15. Future Scope

The project can be extended through:

- Integration with real IBM Quantum hardware.
- Generation of larger quantum random bit sequences.
- Implementation of the complete NIST SP 800-22 test suite.
- Evaluation of additional debiasing techniques.
- Comparison of quantum and classical random number generators.
- Hardware noise and measurement error analysis.
- Integration with cryptographic applications.
- Development of a web-based monitoring application.

---

## 16. Conclusion

The Quantum Random Number Generator demonstrates how quantum circuit operations can be used to generate binary measurement outcomes through superposition and measurement.

The project successfully integrates quantum bit generation, Von Neumann debiasing, statistical randomness evaluation and interactive data visualization into a unified Python pipeline.

The implementation provides an experimental foundation for understanding quantum randomness and evaluating the statistical properties of generated binary sequences.

---

## 17. References

1. NIST Special Publication 800-22 Rev. 1a, *A Statistical Test Suite for Random and Pseudorandom Number Generators for Cryptographic Applications*.

   https://csrc.nist.gov/pubs/sp/800/22/r1/upd1/final

2. Qiskit Documentation.

   https://docs.quantum.ibm.com/

3. Qiskit Aer Documentation.

   https://qiskit.github.io/qiskit-aer/

4. Von Neumann, J. (1951). Various techniques used in connection with random digits. In *Monte Carlo Method*, National Bureau of Standards Applied Mathematics Series.

5. Python Documentation.

   https://docs.python.org/3/

---

## 18. Author and Project Information

**Project Title:** Quantum Random Number Generator

**Domain:** Quantum Computing

**Programming Language:** Python

**Framework:** Qiskit

**Project Type:** Academic Research and Implementation

**Execution:** Automated Python Pipeline

**Visualization:** Interactive HTML Dashboard

---
