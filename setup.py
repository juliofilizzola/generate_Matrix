from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name='datamatrix_lib',
    version='0.1',
    author='Julio Filizzola',
    packages=find_packages(),
    description='Lib de geração de qrcode datamatrix',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    package=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=requirements
)
