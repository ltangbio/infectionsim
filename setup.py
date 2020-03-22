"""
A package that models the spread of infection.
"""
import setuptools

with open("README.rst", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="infectionsim",
    version="0.0.1",
    author="Laura Tang",
    author_email="laura.tang@mail.utoronto.ca",
    description="A package that models the spread of infection",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    packages=["infectionsim"]
)
