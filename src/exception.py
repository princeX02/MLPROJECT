import sys
import logging

# Setup logging (if not already configured elsewhere)
logging.basicConfig(
    format="%(asctime)s [%(lineno)d] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

def error_message_detail(error, error_detail: sys):
    _, _, exec_tb = error_detail.exc_info()
    file_name = exec_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script: [{0}] at line [{1}] with message: [{2}]".format(
        file_name, exec_tb.tb_lineno, str(error)
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message



