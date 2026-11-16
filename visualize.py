
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ==========================================
# QUANTUM RANDOM NUMBER GENERATOR
# Stage 4: Visualization and Analysis
# ==========================================

print("\n===================================")
print("QUANTUM RANDOMNESS ANALYSIS")
print("===================================")

# Step 1: Load generated dataset
df = pd.read_csv("data/quantum_random_bits.csv")

bits = df["Random_Bit"].to_numpy()

# Step 2: Calculate statistics
total_bits = len(bits)

if total_bits == 0:
    raise ValueError("The quantum random dataset is empty.")

if not np.isin(bits, [0, 1]).all():
    raise ValueError("Dataset must contain only binary values 0 and 1.")

zeros = np.sum(bits == 0)
ones = np.sum(bits == 1)

zero_percentage = (zeros / total_bits) * 100
one_percentage = (ones / total_bits) * 100

print("Total bits:", total_bits)
print("Number of zeros:", zeros)
print("Number of ones:", ones)

print(f"Zero percentage: {zero_percentage:.2f}%")
print(f"One percentage: {one_percentage:.2f}%")

# Step 3: Create results directory
os.makedirs("results", exist_ok=True)


# ==========================================
# GRAPH 1: BIT DISTRIBUTION
# ==========================================

plt.figure(figsize=(8, 5))

labels = ["Zeros (0)", "Ones (1)"]
counts = [zeros, ones]

plt.bar(labels, counts)

plt.axhline(
    total_bits / 2,
    linestyle="--",
    label="Expected count (50%)"
)

plt.title("Quantum Random Bit Distribution")
plt.xlabel("Bit Value")
plt.ylabel("Frequency")

plt.legend()
plt.grid(axis="y", alpha=0.3)

plt.tight_layout()

plt.savefig(
    "results/bit_distribution.png",
    dpi=300
)

plt.close()


# ==========================================
# GRAPH 2: PROBABILITY CONVERGENCE
# ==========================================

running_probability = (
    np.cumsum(bits) /
    np.arange(1, total_bits + 1)
)

plt.figure(figsize=(10, 5))

plt.plot(
    np.arange(1, total_bits + 1),
    running_probability,
    label="Observed probability of 1"
)

plt.axhline(
    0.5,
    linestyle="--",
    label="Theoretical probability (0.5)"
)

plt.title("Quantum Randomness: Probability Convergence")
plt.xlabel("Number of Measurements")
plt.ylabel("Cumulative Probability of 1")

plt.legend()
plt.grid(alpha=0.3)

plt.tight_layout()

plt.savefig(
    "results/probability_convergence.png",
    dpi=300
)

plt.close()


# ==========================================
# GRAPH 3: RANDOM BIT SEQUENCE
# ==========================================

sample_size = min(200, total_bits)

plt.figure(figsize=(12, 4))

plt.imshow(
    bits[:sample_size].reshape(1, -1),
    aspect="auto",
    cmap="binary",
    interpolation="nearest"
)

plt.title(
    f"Quantum Random Bit Sequence "
    f"(First {sample_size} Bits)"
)

plt.xlabel("Bit Position")
plt.yticks([])

plt.tight_layout()

plt.savefig(
    "results/random_bit_sequence.png",
    dpi=300
)

plt.close()


# ==========================================
# SAVE ANALYSIS SUMMARY
# ==========================================

summary = pd.DataFrame({
    "Metric": [
        "Total Bits",
        "Zeros",
        "Ones",
        "Zero Percentage",
        "One Percentage"
    ],

    "Value": [
        total_bits,
        zeros,
        ones,
        zero_percentage,
        one_percentage
    ]
})

summary.to_csv(
    "results/analysis_summary.csv",
    index=False
)


# ==========================================
# FINAL OUTPUT
# ==========================================

print("\n===================================")
print("VISUALIZATION COMPLETED")
print("===================================")

print("Generated graphs:")

print("1. results/bit_distribution.png")
print("2. results/probability_convergence.png")
print("3. results/random_bit_sequence.png")

print("\nGenerated summary:")
print("4. results/analysis_summary.csv")

print("\nStage 4 analysis completed successfully!")
