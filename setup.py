import setuptools
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='reple',
     version='0.1.0.1',
     scripts=['reple/reple'] ,
     author="Benjamin Brock",
     author_email="brock@cs.berkeley.edu",
     description="\"replay-based\" REPL for compiled languages",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/BenBrock/reple",
     install_requires=['prompt_toolkit', 'pygments'],
     packages=['reple'],
     include_package_data=True,
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: BSD License",
         "Operating System :: OS Independent",
     ],
)
