from setuptools import setup,find_packages
from typing import List 

def get_requirements() -> List[str]:
    
    requirement_list:List[str]=[]
    
    with open('requirements.txt', 'r') as f:
        lines = f.readlines()
        
        for line in lines:
            
            if line and line != '-e .':
                requirement_list.append(line.strip())
        
    
    return requirement_list

setup(
    name='Weather Prediction',
    version='1.0',
    packages=find_packages(),
    install_requires=get_requirements(),
    author='Prem Raj',
    author_email='rajp37590@gmail.com',
)