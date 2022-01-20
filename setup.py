import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fundb",
    version="0.0.6",
    author="Madhava-mng",
    author_email="alformint@gmail.com",
    description="Simple dictionary database for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Madhava-mng/FunDB",
    use2to3 = True,
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = ["milkycow"]
)
