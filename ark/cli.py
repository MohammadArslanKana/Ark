import argparse
import sys
from ark import stego, nuke # Import your tools

def main():
    parser = argparse.ArgumentParser(description="ARK - Cybersecurity Toolkit")
    
    parser.add_argument("-s", "--stego", action="store_true", help="Run the steganography tool")
    parser.add_argument("-n", "--nuke", action="store_true", help="Run the disk wiping tool") 

    args = parser.parse_args()

    if args.stego:
        stego.main()  # Call your stego script
    elif args.nuke:
        nuke.main()

    else:
        parser.print_help()

if __name__ == "__main__":
    main()