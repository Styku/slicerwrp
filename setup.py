import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="slicerwrp",
    version="0.0.1",
    author="Bartlomiej Styczen",
    description="A small wrapper for Prusa Slic3r",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Styku/slicerwrp",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha"
    ],
    python_requires='>=3.6',
)