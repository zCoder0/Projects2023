from setuptools import find_packages, setup
from typing import List

def get_requirements() ->List[str]:
    
    requirements_list : List[str]=[]
    
    try:
        with open('requirements.txt','r') as f:
            
            lines = f.readlines() 
            
            for line in lines:
                requirement =line.strip()
                
                if requirement and requirement != "-e .":
                    requirements_list.append(requirement)
    except Exception as e:
        print(f"An error occured : {e} ")
        
    return requirements_list

setup(
    name="Face Recognition App",
    author = "Prem Raj",
    author_email="rajp37590@gmail.com",
    version="1.0",
    packages=find_packages(),
    install_requires =get_requirements()
)