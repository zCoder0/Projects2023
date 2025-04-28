import os
from pathlib import Path

project_dir="src"

files_path=[
    f"{project_dir}\__init__.py",
    
    
    f"{project_dir}\components\__init__.py",
    f"{project_dir}\components\data_integtion.py",
    f"{project_dir}\components\data_preprocessing.py",
    f"{project_dir}\components\Feature_engineering.py",
    f"{project_dir}\components\model.py",
    
    f"{project_dir}\dataset\__init__.py",
    
    f"{project_dir}\models\__init__.py",
    
    f"{project_dir}\logs\__init__.py",
    f"{project_dir}\logs\log_config.py",
    
    f"{project_dir}\exception\__init__.py",
    f"{project_dir}\exception\exception_base.py",
    
    
]

for path in files_path:
    file = Path(path)
    
    filedir,file_name = os.path.split(path)
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
    
    if (not os.path.exists(file) or os.path.getsize(file)==0 ):
        with open(file,"w") as f:
            pass