
import os
import pandas as pd

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator


# ==========================================
# QUANTUM RANDOM NUMBER GENERATOR
# Stage 3: Generate 10,000 Random Bits
# ==========================================

TOTAL_BITS = 10000

# Step 1: Create a one-qubit circuit
qc = QuantumCircuit(1, 1)

# Step 2: Apply Hadamard gate
qc.h(0)

# Step 3: Measure qubit into classical bit
qc.measure(0, 0)

# Step 4: Initialize simulator
simulator = AerSimulator()

# Step 5: Compile the circuit
compiled_circuit = transpile(qc, simulator)

# Step 6: Execute 10,000 shots
job = simulator.run(
    compiled_circuit,
    shots=TOTAL_BITS,
    memory=True
)

# Step 7: Retrieve individual measurement results
result = job.result()
random_bits = result.get_memory()

# Step 8: Convert results into integers
bit_sequence = [int(bit) for bit in random_bits]

# Step 9: Calculate statistics
zeros = bit_sequence.count(0)
ones = bit_sequence.count(1)

zero_percentage = (zeros / TOTAL_BITS) * 100
one_percentage = (ones / TOTAL_BITS) * 100

# Step 10: Create data directory
os.makedirs("data", exist_ok=True)

# Step 11: Save bits into CSV
df = pd.DataFrame({
    "Index": range(1, TOTAL_BITS + 1),
    "Random_Bit": bit_sequence
})

df.to_csv("data/quantum_random_bits.csv", index=False)

# Step 12: Display results
print("\n====================================")
print("QUANTUM RANDOM NUMBER GENERATOR")
print("====================================")

print("Total bits generated:", TOTAL_BITS)
print("Number of zeros:", zeros)
print("Number of ones:", ones)

print(f"Zero percentage: {zero_percentage:.2f}%")
print(f"One percentage: {one_percentage:.2f}%")

print("\nFirst 50 random bits:")
print("".join(map(str, bit_sequence[:50])))

print("\nCSV file saved successfully!")
print("Location: data/quantum_random_bits.csv")

print("\n====================================")
print("STAGE 3 EXECUTION COMPLETED")
print("====================================")

