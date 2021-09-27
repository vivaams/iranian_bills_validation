import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="iranian_bills_validation",
    version="1.1",
    author="Amin Morakabi Sabet",
    author_email="vivaams@yahoo.com",
    description="This module checks and validates your bills and returns the required information",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vivaams/iranian_bills_validation",
    project_urls={
        "Bug Tracker": "https://github.com/vivaams/iranian_bills_validation/issues",
    },
    install_requires=[
          'jdatetime',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3",
)
