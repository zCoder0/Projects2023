import logging
import os 
from datetime import datetime 

LOG_FILES = f"{datetime.now().strftime('%d_%m_%Y_%H')}.log"

LOG_FILES_PATH = os.path.join(os.getcwd(),'logs',LOG_FILES)

os.makedirs(LOG_FILES_PATH,exist_ok=True)

LOG_FILES_PATH =os.path.join(LOG_FILES_PATH ,LOG_FILES)

logging.basicConfig(
    level=logging.INFO, 
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
   
    filename=LOG_FILES_PATH
)