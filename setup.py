from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()
setup (

    name="Video Merger",
    version="1.0.0",
    Description="Python appliction that merges and adds music to your videos.",
    long_description=long_description,
    long_description_content_type="Text/markdown",
    author="Totenkopf",
    license="MIT",
    classifiers=[
        "Development Status : 4- Beta",
        "Intended Audience : Developers and Normal Users",
        "LICENSE : OSI Approved : MIT LICENSE"
    ],
    keywords="Video Merger and Music Adding Tool",
    packages=find_packages(),
    install_requires=["requests>=2"],
    python_requires="~=3.5"

)