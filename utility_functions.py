import sys
import traceback
import datetime
import logging
import configparser
import time
import os


def get_exception_message():      
    """
    get full exception message
    :return None
    """     
    try:     
        exc_type, exc_value, exc_tb = sys.exc_info()               
        file_name, line_number, procedure_name, line_code = traceback.extract_tb(exc_tb)[-1]           
        exception_message = ''.join('[Time Stamp]: ' + str(time.strftime('%Y-%m-%d %I:%M:%S %p')) + ' '
                            + '[File Name]: ' + str(file_name) + ' '
                            + '[Procedure Name]: ' + str(procedure_name) + ' '
                            + '[Error Message]: ' + str(exc_value) + ' '  
                            + '[Error Type]: ' + str(exc_type) + ' '                                                                                                                                
                            + '[Line Number]: ' + str(line_number) + ' '
                            + '[Line Code]: ' + str(line_code))               
    except Exception:
        pass   
    return exception_message   
       
def print_exception_message(message_orientation = "horizontal"):
    """
    print full exception message
    :param message_orientation: horizontal or vertical
    :return None
    """
    try:
        exc_type, exc_value, exc_tb = sys.exc_info()           
        file_name, line_number, procedure_name, line_code = traceback.extract_tb(exc_tb)[-1]      
#         time_stamp = '[Time Stamp]: ' + str(time.strftime("%Y-%m-%d %H:%M:%S"))
        time_stamp = " [Time Stamp]: " + str(time.strftime("%Y-%m-%d %I:%M:%S %p"))
        file_name = " [File Name]: " + str(file_name)
        procedure_name = " [Procedure Name]: " + str(procedure_name)
        error_message = " [Error Message]: " + str(exc_value)       
        error_type = " [Error Type]: " + str(exc_type)                   
        line_number = " [Line Number]: " + str(line_number)               
        line_code = " [Line Code]: " + str(line_code)
        if (message_orientation == "horizontal"):
            print( "An error occurred:{};{};{};{};{};{};{}".format(time_stamp, file_name, procedure_name, error_message, error_type, line_number, line_code))
        elif (message_orientation == "vertical"):
            print( "An error occurred:\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(time_stamp, file_name, procedure_name, error_message, error_type, line_number, line_code))
        else:
            pass                   
    except Exception:
        pass
       
def write_log_file(log_file_name, event_level, message):
    """
     write to a log file
    :param log_file_name - log file name
    :param event_level - even level name (CRITICAL, DEBUG, ERROR, INFO and WARNING)
    :param message: message to be wrtten 
    :return None
    """       
    try:
        if event_level == "CRITICAL".lower():
            logging.basicConfig(format=message, filename=log_file_name, level=logging.CRITICAL)      
            logging.critical(message)        
        elif event_level == "DEBUG".lower():
            logging.basicConfig(format=message, filename=log_file_name, level=logging.DEBUG)      
            logging.debug(message)
        elif event_level == "ERROR".lower():
            logging.basicConfig(format=message, filename=log_file_name, level=logging.ERROR)      
            logging.error(message)
        elif event_level == "INFO".lower():
            logging.basicConfig(format=message, filename=log_file_name, level=logging.INFO)      
            logging.info(message)
        elif event_level == "WARNING".lower():
            logging.basicConfig(format=message, filename=log_file_name, level=logging.WARNING)      
            logging.warning(message)               
    except Exception:
        print_exception_message()      