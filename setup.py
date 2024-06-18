from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT = "-e ."
def get_requirments(file_path:str)->List[str]:

    '''
    this function will return the list of the requirements (packages)
    '''
    requirements=[]
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.strip() for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements

setup(
    name="InsightForge",
    version="0.0.1",
    author="Shresth",
    author_email="shresthskaterquad7@gmail.com",
    packages=find_packages(),
    install_requires=get_requirments("requirements.txt")
)