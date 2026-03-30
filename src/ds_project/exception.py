import sys
from src.ds_project.logger import logging


def error_msg_detail(error,error_details:sys):
    _,_,exc_tb=error_details.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_msg="errr occured in python scripts name [{0}] line number [{1}] error msg".format(
      file_name,exc_tb.tb_lineno,str(error)  
    )




class customexp(Exception):
    def __init__(self,error_msg,error_details:sys):
        super().__init__(error_msg)
        self.error_msg=error_msg_detail(error_msg,error_details)

    def __str__(self):
        return self.error_msg
    


