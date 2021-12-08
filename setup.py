import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Covid-data-dashboard-pkg-luishidalgogt2003",
    version="0.0.1",
    author="Luis Hidalgo Gutierrez De Tovar ",
    author_email="luigihg592@gmail.com",
    description="A Covid Data Dashbord with the latest data updates",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lhidalgogt2003/Covid-data-dashboard",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)