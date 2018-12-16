import setuptools
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='reple',
     version='0.1',
     scripts=['reple.py'] ,
     data_files=[('config/reple', ['configs/' + x for x in os.listdir('configs')])],
     author="Benjamin Brock",
     author_email="brock@cs.berkeley.edu",
     description="\"replay-based\" REPL for compiled languages",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/BenBrock/reple",
     install_requires=['prompt_toolkit', 'pygments'],
     packages=setuptools.find_packages(),

     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: BSD License",
         "Operating System :: OS Independent",
     ],
)
