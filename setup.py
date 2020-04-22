from setuptools import find_packages, setup

requires = ['configparser', 'pymysql']

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="shutils",
    version="0.0.9",
    author="山南",
    author_email="zhangpeichaook@163.com",
    url="https://github.com/shannan1989/py-shutils",
    description="Tools for python development.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=find_packages(exclude=["tests"]),
    install_requires=requires,
    entry_points={
        "console_scripts": []
    }
)
