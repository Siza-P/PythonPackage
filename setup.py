from gettext import install
import imp
from setuptools import setup, find_packages

setup(
    name="my package",
    version="0.1",
    packages=find_packages(exclude=["tests*"]),
    license="MIT",
    description="DSA python package",
    long_description=open("README.md").read(),
    install_requires=["numpy"],
    #url=
    author="Sizakele Phakathi",
    author_email="sizaphakathi09@gmail.com"

)