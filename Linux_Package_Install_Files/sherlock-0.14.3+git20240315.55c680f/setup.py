import setuptools
import re

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open('sherlock/sherlock.py', 'rt', encoding='utf8') as f:
    version = re.findall('__version__ = "(.*)"', f.read())[0]

setuptools.setup(
    name="sherlock",
    version=version,
    author="Sherlock Project",
    description="Hunt down social media accounts by username across social networks",
    url="https://github.com/sherlock-project/sherlock",
    packages=setuptools.find_packages(exclude=['sherlock.tests']),
    package_data={"": ["resources/data.json"]},
    include_package_data=True,
    python_requires=">=3.0",
    install_requires=requirements,
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python ::3",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points={
        "console_scripts": ["sherlock=sherlock.sherlock:main"],
    },
)
