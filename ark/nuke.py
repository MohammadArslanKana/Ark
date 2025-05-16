import subprocess
import os

def main():
    script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../scripts/NukeDisk.sh"))

    if not os.path.exists(script_path):
        print("❌ NukeDisk.sh not found.")
        return

    print("🚀 Launching NukeDisk.sh script...")
    try:
        subprocess.run(["bash", script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"💥 Script failed with error: {e}")