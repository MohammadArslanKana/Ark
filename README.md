# 🛡️ ARK - Cybersecurity Toolkit

**ARK** is a modular, CLI-based cybersecurity toolkit built in Python. It combines utilities for steganography, and secure disk wiping.

> ⚠️ This toolkit is built for ethical use only. Always ensure you have permission before running any of its features.

---
## Features 🚀

### 🖼️ Stego Tool — Image Steganography
- Hide messages inside images securely.
- Encrypt the pixel locations using AES encryption.
- Retrieve hidden messages from stego images.
- Supports custom or randomly generated encryption keys.

### 💣 NukeDisk — Secure Disk Wiper
- A powerful Bash script that **permanently wipes all data** from a disk.
- Ideal for securely erasing hard drives, USBs or NVME before disposal or reuse.
- You can either leave the disk as it is or format it for further usage. 

## Installation 💻
Using this might need some extra work like using break system packages.
Clone the repository and install the package:

```sh
git clone https://github.com/Mady520/ark.git
cd ark
pip install -r requirements.txt 
pip install . 
```
You can use python virtual enivronment if some errors are there

```sh
python3 -m venv myenv  # Create a virtual environment
source myenv/bin/activate  # Activate the environment
git clone https://github.com/Mady520/ark.git
cd ark 
pip install -r requirements.txt
pip install .
deactivate 
```

## Usage : Its very simple to use 
```sh
ark -h # for help it will show all the tools and how to use them 
ark -s # for stego-tool
sudo ark -n # for NukeDisk --> Disk Wiper
```
or
```sh
python -m ark.cli --stego
sudo python -m ark.cli --nuke
```

If the NukeDisk doesn't work through cli use the script directly from the directory scripts using:
```sh
sudo bash Nukedisk.sh
```

📜 License
This project is for educational and ethical use only.
You are responsible for how you use the tools included in ARK.
