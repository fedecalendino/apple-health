from os import path

from setuptools import setup

this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="apple-health",
    version="1.1.1",
    url="https://github.com/fedecalendino/apple-health",
    license="MIT",
    description="Library to extract information from Apple Health exports",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Fede Calendino",
    author_email="fede@calendino.com",
    packages=[
        "apple_health",
        "apple_health.classes",
        "apple_health.constants",
    ],
    keywords=["apple health"],
    install_requires=[
        "python-dateutil",
        "xmltodict",
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
