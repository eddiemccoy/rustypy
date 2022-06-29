with open("README.md", "r") as fh:
	long_description = fh.read()
from setuptools import find_packages, setup
setup(
    name = "rustypy",
    version = "0.0.1",
    author = "Eddie Mccoy",
    author_email = "eddie998199@yahoo.co.uk"
    description = "Calculation of fibonacci number",
    long_description = "A basic library that calculates fibonacci numbers",
    long_description_content_type = "text/markdown",
    url = "https://github.com/eddiemccoy/rustypy",
    install_requires = [],
    packages = find_packages(exclude = ("tests",)),
    classifiers = [
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        ],
    python_requires ='>=3',
    test_require = ['pytest'],
        )
