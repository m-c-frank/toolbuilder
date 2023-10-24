from setuptools import setup, find_packages

setup(
    name="toolbuilder_cli",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    extras_require={
        "git": [
            "treeofthoughts @ git+https://github.com/m-c-frank/tree-of-thoughts",
            "neuralapi @ git+https://github.com/m-c-frank/neuralapi",
        ],
    },
    author="Martin Christoph Frank",
    author_email="martin7.frank7@gmail.com",
    description="CLI tool for the Toolbuilder application.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/m-c-frank/toolbuilder",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GOS License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
    entry_points={
        "console_scripts": [
            "toolbuilder=toolbuilder.__main__:main",
        ],
    },
)
