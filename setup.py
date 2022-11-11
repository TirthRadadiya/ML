from setuptools import setup,find_packages
from typing import List




#declaring variable for setpu function
PROJECT_NAME = "Housing_predictor"
VERSION = "0.0.1"
AUTHOR  = "Tirth Radadiya"
DESCRIPTION = "This is the first project based on real-world practice"
# PACKAGES = ["housing"] 
REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirements_list()->List(str):
    """
    Description: This function is going to return list of requirement
    mention in requirements.txt file
    return This function is going to return a list which contain name
    of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list()
)

"""
find_packages() will iterate every __init__ file in our project and install necccessary packages
if we want to "-e ." we need to have setup.py file
"-e ." does the same work as find_packages()
.egg-info contains all the information about our local project and "-e ." creates .egg-info folder 
"""