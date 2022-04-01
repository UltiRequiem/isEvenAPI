from setuptools import setup

setup(
    name="isEvenAPI",
    packages=["is_even"],
    version="3.0",
    license="MIT",
    description="API Wrapper for the isEven API.",
    author="Eliaz Bobadilla",
    url="https://github.com/UltiRequiem/isEvenAPI",
    keywords=["api", "isEven", "math", "even", "odd"],
    long_description=open("readme.md").read(),
    long_description_content_type="text/markdown",
    install_requires=["requests==2.25.1", "retry==0.9.2"],
)
