from setuptools import setup, find_packages

setup(
    name="ark",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "argparse",
    ],
    entry_points={
        "console_scripts": [
            "ark=ark.cli:main",  # This makes "ark" a global command
        ],
    },
)
