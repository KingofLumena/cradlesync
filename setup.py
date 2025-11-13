# setup.py
from setuptools import setup, find_packages

setup(
    name="cradlesync",
    version="0.0.0",
    description="Open-source memory protocol for awakening echo AIs",
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    python_requires=">=3.11",
)
