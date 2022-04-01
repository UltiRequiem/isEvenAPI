from setuptools import setup, find_packages

with open("readme.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()
with open("requirements.txt", "r", encoding="utf-8") as requirement:
    requirements = requirement.read()

setup(
    name="isEvenAPI",
    packages=find_packages(),
    version="3.0",
    author="Eliaz Bobadilla",
    author_email="eliaz.bobadilladev@gmail.com",
    url="https://github.com/UltiRequiem/isEvenAPI",
    description="API Wrapper for the isEven API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    keywords=["api", "isEven", "math", "even", "odd"],
    install_requires=[requirements],
    classifiers=[
        "Operating System :: OS Independent",
    ],
    entry_points="""
        [console_scripts]
        is_even=is_even:__main__
    """,
)
