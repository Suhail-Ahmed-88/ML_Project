import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
    
__version__ = "0.0.1"

REPO_NAME = "ML_Project"
AUTHOR_USER_NAME = "Suhail Ahmed"
SRC_REPO = "ML_Project"
AUTHOR_EMAIL = "rajpar.suhail.ahmed@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A simple machine learning project",
    url=f"https://github.com/Suhail-Ahmed-88/ML_Project",
    packages=setuptools.find_packages(),
)
