# !/bin/bash
# =================================================
# Script Name: NukeDisk
# Version    : 1.0
# Author - Mohammad Arslan Kana ,Mudasir Samad
# =================================================

echo "🚨 Welcome to NukeDisk — Secure Drive Data Nuker 🚨"
echo "---------------------------------------------------"
echo "This script will PERMANENTLY erase all data on a disk."
echo "Use with extreme caution."
echo

echo "Listing All Drives connected and their partions"
lsblk
echo

#this takes user drive name and changes to path to get executed further
read -p "Enter the disk you want to clean wipe data out of:" disk_name
disk="/dev/$disk_name"

#echo ${disk}

if [ ! -b "$disk" ]; then
    echo "Error: Device [$disk] not found"
    exit 1
fi

#warning 
echo ""
echo "WARNING"
echo "This disk:[${disk}] will be have all its data deleted and non-retreivable"
read -p "Do you want to continue:y/n " choice

if [ "$choice" = "n" ]; then
    echo "exited"
    exit 2
fi

#echo "choice was y"

#default size for random data writing=10M or user defined
echo
echo "🔧 Block Size (bs) Recommendations for dd:"
echo "--------------------------------------------"
echo "  1M   -> Very safe, compatible everywhere (slow)"
echo "  4M   -> Balanced, safe and slightly faster"
echo "  10M  -> Fast, good performance (recommended)"
echo "  50M  -> Very fast, use if you have 8GB+ RAM"
echo "  100M -> High speed, risk of memory error if low on RAM"
echo "--------------------------------------------"
echo "💡 Tip: If unsure, just press Enter for default (10M)"
echo
read -p "Enter block size for dd (e.g., 1M, 10M, 50M): " block_size
block_size=${block_size:-10M}
echo "Using Block size = $block_size"

#process starts:
echo 
echo "Unmounting all partions of device:${disk}"
unmount ${disk}?* &>/dev/null
echo "Unmountion partion successfull"

#drive duplication and making data non recoverable
echo
echo "Starting Drive data distruction"
for i in {1..3}; do
    echo "Pass $i : writing random data to drive $disk"
    dd if=/dev/urandom of="$disk" bs=$block_size status=progress
    sync
done

echo "Final pass: writing zeros..."
dd if=/dev/zero of="$disk" bs=$block_size status=progress
dd if=/dev/urandom of="$disk" bs=$block_size status=progress
sync

echo "[✔] Wipe complete. Data in $disk is now unrecoverable."
