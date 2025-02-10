import argparse
import sys
from ark import stego  # Import your tools

def main():
    parser = argparse.ArgumentParser(description="ARK - Cybersecurity Toolkit")
    
    parser.add_argument("-s", "--stego", action="store_true", help="Run the steganography tool")
   
    args = parser.parse_args()

    if args.stego:
        stego.main()  # Call your stego script
    
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
