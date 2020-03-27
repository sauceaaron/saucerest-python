import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="saucerest",
    version="0.0.1",
    author="Aaron Evans",
    author_email="worcestershire@saucelabs.com",
    description="A python client for the Sauce Labs REST API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sauceaaron/saucerest-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)