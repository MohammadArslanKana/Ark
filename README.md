# ARK - small security toolkit  🔒

ARK is a command-line steganography tool that allows you to hide and retrieve secret messages within images using AES encryption.

## Features 🚀
- Hide messages inside images securely.
- Encrypt the pixel locations using AES encryption.
- Retrieve hidden messages from stego images.
- Supports custom or randomly generated encryption keys.

## Installation 💻
Using this might need some extra work like using break system packages.
Clone the repository and install the package:

~~~sh
git clone https://github.com/MohammadArslanKana/ark.git
cd ark
pip install -r requirements.txt 
pip install . 
~~~
You can use python virtual enivronment if some errors are there

~~~sh
python3 -m venv myenv  # Create a virtual environment
source myenv/bin/activate  # Activate the environment
git clone https://github.com/MohammadArslanKana/ark.git
cd ark 
pip install -r requirements.txt
pip install .
deactivate 
~~~
