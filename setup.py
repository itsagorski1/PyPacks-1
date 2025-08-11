from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pypacks",
    version="1.1.0",
    description="A Minecraft pack generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Block120",
    packages=find_packages(),
    install_requires=[],
    python_requires=">=3.6",
)