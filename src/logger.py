from src.logger import logging
import os 
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%n_%d_%Y_%H_%M_%S')}.log"
log_path=os.path.join(os.getcwdb(),"logs",LOG_FILE)
os.makedirs(log_path,exist_ok=True)


LOG_FILE_PATH=os.path.join(log_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    
)

if __name__=="__main":
    logging.info("logging has started")
    
    