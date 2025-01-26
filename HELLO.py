import sys
import os

def print_activation_command():
    venv_path = os.path.abspath('.venv')
    if sys.platform == "win32":
        cmd_command = f"{venv_path}\\Scripts\\activate.bat"
        ps_command = f"{venv_path}\\Scripts\\Activate.ps1"
        print("For Command Prompt, run:")
        print(cmd_command)
        print("\nFor PowerShell, run:")
        print(ps_command)
    else:
        bash_command = f"source {venv_path}/bin/activate"
        print("For Bash-like shells, run:")
        print(bash_command)

if __name__ == "__main__":
    print_activation_command()