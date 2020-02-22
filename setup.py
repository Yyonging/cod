import setuptools
from cod import __version__

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cod",
    version=__version__,
    packages=setuptools.find_packages(),
    include_package_data=True,
    author="duanyongqiang",
    author_email="sysuduanyongqiang@163.com",
    description="A userful package to use 'the click package to add command' for a interactive terminal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="Apache License 2.0",
    url="https://github.com/Yyonging/cod",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "prompt_toolkit>=3.0.0",
        "click>=5.1",
    ],
)
