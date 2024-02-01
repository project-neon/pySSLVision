from setuptools import find_packages, setup

setup(
    name="pySSLVision",
    packages=find_packages() + find_packages(where="./protocols"),
    version="1.0.0",
    description="Creates a network socket to communicate with the SSL Vision",
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    author="Project-Neon",
    author_email="projectneon@gmail.com",
    license="GNU",
    install_requires=['protobuf==3.6.1'],
)