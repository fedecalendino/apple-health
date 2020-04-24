from os import path

from setuptools import setup

this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, "readme.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="apple-health",
    version="0.3",
    url="https://github.com/federicocalendino/apple-health",
    license="MIT",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Federico Calendino",
    author_email="federicocalendino@gmail.com",
    packages=[
        "apple_health",
    ],
    keywords=[],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
