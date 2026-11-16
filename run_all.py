
import subprocess
import sys
import os
import time

# ==========================================
# QUANTUM RANDOM NUMBER GENERATOR
# MASTER EXECUTION PIPELINE
# ==========================================

PROJECT_STAGES = [
    ("Quantum Random Bit Generation", "main.py"),
    ("Data Visualization", "visualize.py"),
    ("Von Neumann Debiasing", "debias.py"),
    ("NIST Statistical Testing", "nist_testing.py"),
    ("Dashboard Generation", "dashboard.py")
]


def execute_stage(stage_name, script_name):

    print("\n" + "=" * 55)
    print(f"STARTING: {stage_name}")
    print("=" * 55)

    start_time = time.time()

    try:

        subprocess.run(
            [sys.executable, script_name],
            check=True
        )

        elapsed = time.time() - start_time

        print(f"\n[SUCCESS] {stage_name}")
        print(f"Execution time: {elapsed:.2f} seconds")

        return True

    except subprocess.CalledProcessError as error:

        print(f"\n[FAILED] {stage_name}")
        print("Exit code:", error.returncode)

        return False

    except FileNotFoundError:

        print(f"\n[ERROR] Missing file: {script_name}")

        return False


def main():

    print("\n")
    print("*" * 55)
    print(" QUANTUM RANDOM NUMBER GENERATOR ")
    print(" COMPLETE PROJECT EXECUTION ")
    print("*" * 55)

    start_time = time.time()

    successful_stages = 0

    for stage_name, script_name in PROJECT_STAGES:

        success = execute_stage(
            stage_name,
            script_name
        )

        if not success:

            print("\nPIPELINE STOPPED!")
            print("Please fix the error and execute again.")

            return

        successful_stages += 1

    total_time = time.time() - start_time

    print("\n" + "*" * 55)
    print(" PROJECT EXECUTION COMPLETED ")
    print("*" * 55)

    print(
        f"Successful stages: "
        f"{successful_stages}/{len(PROJECT_STAGES)}"
    )

    print(f"Total execution time: {total_time:.2f} seconds")

    print("\nGenerated folders:")

    for folder in ["data", "results"]:

        if os.path.exists(folder):
            print(f"[OK] {folder}/")

    print("\nFinal dashboard:")
    print("results/dashboard.html")

    print("\nOpen dashboard.html in your browser.")


if __name__ == "__main__":
    main()
