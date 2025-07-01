# To automate terminal commands with python we will use subprocess library.
# It connects python with the CLI
# Here we will be using check_call function

import subprocess

for i in range(5):
    subprocess.check_call(["python", "example.py"])