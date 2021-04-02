import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fundb",
    version="0.0.5",
    author="Madhava",
    author_email="alformint@gmail.com",
    description="Simple database for Python user",
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
