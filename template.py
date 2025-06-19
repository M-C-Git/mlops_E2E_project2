import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s')

project_name = "datascience"
list_of_files = [
    ".gthub/workflows/.gitkeep",                  # for deployment
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",  # include all functional component of the process, will call functions form utils folder
    f"src/{project_name}/utils/__init__.py",       # utils folder is for generic functions to be shared in the porject
    f"src/{project_name}/utils/common.py",         # include all the funcitons shared in the projects
    f"src/{project_name}/config/__init__.py",      # constructor
    f"src/{project_name}/config/configuration.py",      # constructor
    f"src/{project_name}/pipeline/__init__.py",         # contain all piplelines, such as training and prediciton, will call compoment from components package
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",       # all configuration details
    "params.yaml",              # parameters for machine learning training.
    "schema.yaml",        
    "main.py",               
    "Dockerfile",
    "setup.py",                 # creat entire project as a package
    "research/research.ipynb",
    "templates/index.html",
    "app.py"

]


for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory {filedir} for the file : {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:

            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")