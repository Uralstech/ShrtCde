from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding='utf-8') as fh:
    long_description = '\n' + fh.read()

VERSION = '0.4.4'
DESCRIPTION = 'Helps shorten the amount of code you write'

# Setting up
setup(
    name="ShrtCde",
    version=VERSION,
    author="Uralstech (Udayshankar Ravikumar)",
    author_email="<info@uralstech.in>",
    url="https://github.com/Uralstech/ShrtCde",
    license="Apache License 2.0",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'shrt', 'short', 'cde', 'code', 'shortcode', 'shrtcde', 'ui', 'sort', 'file', 'io', 'library'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows"
    ]
)