from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="python-template",
    version="0.0.1",
    author="Daniel Flanigan",
    author_email="daniel.isaiah.flanigan@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/danielflanigan/python-template",
    packages=['package'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['numpy'],
)
