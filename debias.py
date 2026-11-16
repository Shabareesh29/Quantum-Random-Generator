
import os
import pandas as pd

# ==========================================
# QUANTUM RANDOM NUMBER GENERATOR
# Stage 5: Von Neumann Debiasing
# ==========================================

# Step 1: Load original quantum random bits
df = pd.read_csv("data/quantum_random_bits.csv")

raw_bits = df["Random_Bit"].tolist()

# Step 2: Calculate original statistics
total_raw = len(raw_bits)
raw_zeros = raw_bits.count(0)
raw_ones = raw_bits.count(1)

# Step 3: Apply Von Neumann debiasing
debiased_bits = []

discarded_pairs = 0
retained_pairs = 0

for i in range(0, total_raw - 1, 2):

    first = raw_bits[i]
    second = raw_bits[i + 1]

    if first == 0 and second == 1:
        debiased_bits.append(0)
        retained_pairs += 1

    elif first == 1 and second == 0:
        debiased_bits.append(1)
        retained_pairs += 1

    else:
        discarded_pairs += 1

# Step 4: Calculate debiased statistics
total_debiased = len(debiased_bits)

debiased_zeros = debiased_bits.count(0)
debiased_ones = debiased_bits.count(1)

if total_debiased > 0:
    zero_percentage = debiased_zeros / total_debiased * 100
    one_percentage = debiased_ones / total_debiased * 100
else:
    zero_percentage = 0
    one_percentage = 0

# Step 5: Calculate efficiency
efficiency = (total_debiased / (total_raw // 2)) * 100

# Step 6: Create output directories
os.makedirs("data", exist_ok=True)
os.makedirs("results", exist_ok=True)

# Step 7: Save debiased bits
output_df = pd.DataFrame({
    "Index": range(1, total_debiased + 1),
    "Debiased_Bit": debiased_bits
})

output_df.to_csv(
    "data/debiased_random_bits.csv",
    index=False
)

# Step 8: Save comparison summary
summary = pd.DataFrame({
    "Metric": [
        "Original Bits",
        "Original Zeros",
        "Original Ones",
        "Retained Pairs",
        "Discarded Pairs",
        "Debiased Bits",
        "Debiased Zeros",
        "Debiased Ones",
        "Zero Percentage",
        "One Percentage",
        "Debiasing Efficiency"
    ],
    "Value": [
        total_raw,
        raw_zeros,
        raw_ones,
        retained_pairs,
        discarded_pairs,
        total_debiased,
        debiased_zeros,
        debiased_ones,
        zero_percentage,
        one_percentage,
        efficiency
    ]
})

summary.to_csv(
    "results/debiasing_summary.csv",
    index=False
)

# Step 9: Display results
print("\n====================================")
print("VON NEUMANN DEBIASING RESULTS")
print("====================================")

print("Original bits:", total_raw)
print("Original zeros:", raw_zeros)
print("Original ones:", raw_ones)

print("\nDebiasing results:")
print("Retained pairs:", retained_pairs)
print("Discarded pairs:", discarded_pairs)

print("\nFinal output:")
print("Debiased bits:", total_debiased)
print("Debiased zeros:", debiased_zeros)
print("Debiased ones:", debiased_ones)

print(f"\nZero percentage: {zero_percentage:.2f}%")
print(f"One percentage: {one_percentage:.2f}%")
print(f"Debiasing efficiency: {efficiency:.2f}%")

print("\nSaved files:")
print("data/debiased_random_bits.csv")
print("results/debiasing_summary.csv")

print("\nSTAGE 5 COMPLETED!")
