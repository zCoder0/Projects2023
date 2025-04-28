from setuptools import setup,find_packages
from typing import List
from src.exception.ExceptionBase import ProjectException
import sys
def get_requirement() -> List[str]:
    
    requiremets_list : List[str]=[]
    
    try:
        with open('requirements.txt', 'r') as f:
            lines = f.readlines()
            
            for line in lines:
                requirement=line.strip()
                
                if requirement and requirement != "-e .":
                    requiremets_list.append(requirement)
    except Exception as e:
        print(f"An error occurred: {e}")
        ProjectException(e,sys)

    return requiremets_list

setup(
    name='RetailProductRecommendedSystem',
    author="Prem Raj",
    author_email="rajp37590@gmail.com",
    version="1.0",
    packages=find_packages(),
    install_requires =get_requirement()
)