import setuptools

VERSION = "0.1.0"
README_FILENAME = "README.md"
KEYWORD = [
    "date to text",
    "date to word",
    "to word",
    "to text",
]

with open(README_FILENAME, "r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

setuptools.setup(
    name="past_date2word",
    version=VERSION,
    author="Awiteb",
    author_email="Awiteb@hotmail.com",
    description="past_date2word is library helps you to convert the past date to text",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TheAwiteb/past_date2word",
    packages=setuptools.find_packages(),
    keywords=KEYWORD,
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
