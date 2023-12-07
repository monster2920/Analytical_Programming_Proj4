from setuptools import setup, find_packages

setup(
    name="my_package",  
    version="0.1.0",  
    author="Sandeep Varma Uppalapati",  
    author_email="u.s.varma2920@gmail.com",  
    description="A package for extracting and analyzing web data",  
    url="https://github.com/monster2920/Analytical-Programming-Project/tree/main/Project%202",  
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.1",
        "pandas>=1.2.0",
        "beautifulsoup4>=4.9.3",
        
    ],
    classifiers=[
        # Full list: https://pypi.org/classifiers/
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6", # version of the package
)
