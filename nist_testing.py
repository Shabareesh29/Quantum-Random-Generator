
import os
import math
import pandas as pd

from scipy.special import gammaincc


# ==============================================
# QUANTUM RANDOM NUMBER GENERATOR
# Stage 6: NIST SP 800-22 Statistical Testing
# ==============================================

ALPHA = 0.01


# ----------------------------------------------
# TEST 1: FREQUENCY (MONOBIT) TEST
# ----------------------------------------------

def frequency_test(bits):

    n = len(bits)

    if n < 100:
        return None

    s = sum(2 * bit - 1 for bit in bits)

    p_value = math.erfc(abs(s) / math.sqrt(2 * n))

    return p_value


# ----------------------------------------------
# TEST 2: FREQUENCY WITHIN A BLOCK
# ----------------------------------------------

def block_frequency_test(bits):

    n = len(bits)

    if n < 100:
        return None

    block_size = max(20, int(0.02 * n))

    number_of_blocks = n // block_size

    if number_of_blocks < 1 or number_of_blocks >= 100:
        return None

    chi_square = 0

    for i in range(number_of_blocks):

        block = bits[
            i * block_size:(i + 1) * block_size
        ]

        proportion = sum(block) / block_size

        chi_square += 4 * block_size * (
            proportion - 0.5
        ) ** 2

    p_value = gammaincc(
        number_of_blocks / 2,
        chi_square / 2
    )

    return p_value


# ----------------------------------------------
# TEST 3: RUNS TEST
# ----------------------------------------------

def runs_test(bits):

    n = len(bits)

    if n < 100:
        return None

    proportion = sum(bits) / n

    # NIST precondition
    if abs(proportion - 0.5) >= 2 / math.sqrt(n):
        return None

    runs = 1

    for i in range(1, n):

        if bits[i] != bits[i - 1]:
            runs += 1

    expected_runs = 2 * n * proportion * (
        1 - proportion
    )

    denominator = (
        2 * math.sqrt(2 * n)
        * proportion
        * (1 - proportion)
    )

    p_value = math.erfc(
        abs(runs - expected_runs) / denominator
    )

    return p_value


# ----------------------------------------------
# TEST 4: APPROXIMATE ENTROPY TEST
# ----------------------------------------------

def approximate_entropy_test(bits, m=2):

    n = len(bits)

    if n < 2048:
        return None

    def calculate_phi(pattern_length):

        counts = {}

        extended = bits + bits[:pattern_length - 1]

        for i in range(n):

            pattern = tuple(
                extended[i:i + pattern_length]
            )

            counts[pattern] = counts.get(pattern, 0) + 1

        phi = 0

        for count in counts.values():

            probability = count / n

            phi += probability * math.log(probability)

        return phi

    phi_m = calculate_phi(m)
    phi_m1 = calculate_phi(m + 1)

    approximate_entropy = phi_m - phi_m1

    chi_square = 2 * n * (
        math.log(2) - approximate_entropy
    )

    p_value = gammaincc(
        2 ** (m - 1),
        chi_square / 2
    )

    return p_value


# ----------------------------------------------
# RUN ALL SELECTED TESTS
# ----------------------------------------------

def run_nist_tests(bits, dataset_name):

    tests = {
        "Frequency Test": frequency_test,
        "Block Frequency Test": block_frequency_test,
        "Runs Test": runs_test,
        "Approximate Entropy Test": approximate_entropy_test
    }

    results = []

    print("\n====================================")
    print(dataset_name.upper())
    print("====================================")

    print("Total bits:", len(bits))
    print("Significance level:", ALPHA)

    for test_name, test_function in tests.items():

        try:

            p_value = test_function(bits)

            if p_value is None:

                status = "NOT APPLICABLE"

                print(f"{test_name}: {status}")

            elif math.isfinite(p_value):

                status = (
                    "PASS" if p_value >= ALPHA else "FAIL"
                )

                print(
                    f"{test_name}: {status} "
                    f"(p-value = {p_value:.6f})"
                )

            else:

                p_value = None
                status = "INVALID RESULT"

                print(f"{test_name}: {status}")

        except Exception as error:

            p_value = None
            status = "ERROR"

            print(f"{test_name}: {error}")

        results.append({
            "Dataset": dataset_name,
            "Test": test_name,
            "P_Value": p_value,
            "Significance_Level": ALPHA,
            "Status": status
        })

    return results


# ==============================================
# MAIN EXECUTION
# ==============================================

print("\nQUANTUM RANDOMNESS TESTING")
print("NIST SP 800-22 SELECTED TESTS")

# Load raw dataset
raw_df = pd.read_csv(
    "data/quantum_random_bits.csv"
)

raw_bits = raw_df["Random_Bit"].astype(int).tolist()

# Load debiased dataset
debiased_df = pd.read_csv(
    "data/debiased_random_bits.csv"
)

debiased_bits = (
    debiased_df["Debiased_Bit"]
    .astype(int)
    .tolist()
)

# Run tests on both datasets
all_results = []

all_results.extend(
    run_nist_tests(raw_bits, "Raw Quantum Bits")
)

all_results.extend(
    run_nist_tests(debiased_bits, "Debiased Quantum Bits")
)

# Save test results
os.makedirs("results", exist_ok=True)

results_df = pd.DataFrame(all_results)

results_df.to_csv(
    "results/nist_test_results.csv",
    index=False
)

print("\n====================================")
print("NIST TESTING COMPLETED")
print("====================================")

print("Results saved to:")
print("results/nist_test_results.csv")

print("\nFinal Testing Summary:")

print(
    results_df[
        ["Dataset", "Test", "P_Value", "Status"]
    ].to_string(index=False)
)
