import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cod",
    version="0.0.1",
    packages=['cod'],
    author="duanyongqiang",
    author_email="sysuduanyongqiang@163.com",
    description="A userful package to use 'the click package to add command' for a interactive terminal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Yyonging/cod",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
)
