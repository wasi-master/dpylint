import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dpylint",
    version="0.1.0",
    author="Wasi Master",
    author_email="arianmollik323@gmail.com",
    description="A package for analyzing Python code using pylint",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wasi-master/dpylint",
    project_urls={
        "Bug Tracker": "https://github.com/wasi-master/dpylint/issues",
    },
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["dpylint", "dpylint.checkers", "dpylint.assets"],
    python_requires=">=3.5.3",
    install_requires=["pylint", "astroid", "discord.py"],
)