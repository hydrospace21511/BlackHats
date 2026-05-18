#!/usr/bin/env python3
"""
Cherry-pick specific commits to rebuild the branch without the unwanted commits.
"""
import subprocess
import os

os.chdir(r'C:\Users\Admin\Desktop\BlackHats\main')

# We want to keep these commits (in order)
commits_to_keep = [
    'a5af509',    # test
    'b1fb86a',    # test (merge commit)
    '5a6b6e3',    # Border and Impact Frame fix v.07
]

print("=== Cherry-picking desired commits ===\n")
print(f"Commits to cherry-pick: {commits_to_keep}\n")

# Cherry-pick each commit
for i, sha in enumerate(commits_to_keep, 1):
    print(f"[{i}/{len(commits_to_keep)}] Cherry-picking {sha}...")
    
    # Check if it's a merge commit
    result = subprocess.run(
        ['git', 'rev-list', '--parents', '-n', '1', sha],
        capture_output=True, text=True
    )
    parents = result.stdout.strip().split()
    is_merge = len(parents) > 2
    
    if is_merge:
        print(f"   (detected as merge commit, using -m 1)")
        cp_result = subprocess.run(['git', 'cherry-pick', '-m', '1', sha], capture_output=True, text=True)
    else:
        cp_result = subprocess.run(['git', 'cherry-pick', sha], capture_output=True, text=True)
    
    if cp_result.returncode != 0:
        print(f"   ERROR: {cp_result.stderr}")
        print("   Aborting cherry-pick...")
        subprocess.run(['git', 'cherry-pick', '--abort'], capture_output=True)
        print("   Aborting entire operation...")
        subprocess.run(['git', 'reset', '--hard', '7df2595'], capture_output=True)
        exit(1)
    else:
        print(f"   ✓ OK")

print(f"\n=== Verifying new history ===")
result = subprocess.run(['git', 'log', '--oneline', '-10'], capture_output=True, text=True)
print(result.stdout)

print("\n=== Complete! ===")
print("The three unwanted commits have been deleted.")
print("\nIf you want to push this: git push --force-with-lease")
