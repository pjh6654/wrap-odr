import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wrap-odr-pjh6654",
    version="0.0.1",
    author="Peter Hart",
    author_email="pjh6654@rit.edu",
    description="A simple wrapper for scipy.odr",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pjh6654/wrap-odr",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)