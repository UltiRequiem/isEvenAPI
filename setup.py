from setuptools import setup

setup(
    name="isEvenAPI",
    packages=["is_even"],
    version="2.2.1",
    license="MIT",
    description="API Wrapper for the isEven api.",
    author="Eliaz Bobadilla",
    url="https://github.com/UltiRequiem/isEven.py",
    keywords=["api", "isEven"],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=["requests==2.25.1", "retry==0.9.2"],
)
