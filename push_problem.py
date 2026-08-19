import sys
import subprocess
import os

def run_cmd(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error executing: {cmd}")
        print(result.stderr)
        return False
    print(result.stdout)
    return True

def main():
    if len(sys.argv) > 1:
        folder = sys.argv[1]
    else:
        folder = input("Enter problem folder name (e.g., 0155-min-stack): ").strip()

    if not os.path.exists(folder):
        print(f"Directory '{folder}' does not exist!")
        return

    if len(sys.argv) >= 6:
        time_ms = sys.argv[2]
        time_pct = sys.argv[3]
        space_mb = sys.argv[4]
        space_pct = sys.argv[5]
    else:
        time_ms = input("Runtime in ms (e.g., 101): ").strip()
        time_pct = input("Runtime percentile (e.g., 48.02%): ").strip().replace("%", "")
        space_mb = input("Memory in MB (e.g., 32.3): ").strip()
        space_pct = input("Memory percentile (e.g., 20.49%): ").strip().replace("%", "")

    commit_msg = f"Time: {time_ms} ms ({time_pct}%), Space: {space_mb} MB ({space_pct}%) - LeetHub"

    print(f"\nStaging folder: {folder}")
    if not run_cmd(f'git add "{folder}"'):
        return

    print(f"Committing with message: '{commit_msg}'")
    if not run_cmd(f'git commit -m "{commit_msg}"'):
        return

    print("Pushing to remote repository...")
    run_cmd("git push")

if __name__ == "__main__":
    main()
