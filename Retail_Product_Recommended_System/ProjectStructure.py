import os
from pathlib import Path

dir_name = "src"

file_path=[
    
    f"{dir_name}/__init__.py",
    f"{dir_name}/components/__init__.py",
    
    f"{dir_name}/components/dataset/__init__.py",    
    f"{dir_name}/components/model/__init__.py",
    
    f"{dir_name}/exception/__init__.py",
    f"{dir_name}/exception/ExceptionBase.py",
    
    f"{dir_name}/logg/__init__.py",
    f"{dir_name}/logg/Logger.py",
    
]

for path in file_path:
    file = Path(path)
    
    filedir,file_name = os.path.split(path)
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
    
    if (not os.path.exists(file) or os.path.getsize(file)==0 ):
        with open(file,"w") as f:
            pass
