from src.logs import log_config
import sys
import os

class ProjectException(Exception):
    
    def __init__(self,error_message,error_details:sys):
        
        self.error_message = error_message
        
        _,_,exc_tb = error_details.exc_info()
        
        self.lineno = exc_tb.tb_lineno
        self.filename = exc_tb.tb_frame.f_code.co_filename
        
        log_config.logging.info(self.__str__())
        
    def __str__(self):
        return f"Error occured in python script name at {self.filename} on line number {self.lineno} error messgae {self.error_message}"
    