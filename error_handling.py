
# Handling Exceptions
# https://wiki.python.org/moin/HandlingExceptions

# Professional Error Handling With Python - Gigi Sayfan
# https://code.tutsplus.com/tutorials/professional-error-handling-with-python--cms-25950

import sys
# import os
import utility_functions

# no_error_handling
def no_error_handling():
    (x,y) = (5,0)
    z = x / y
    print(z)
    
# Now If we print the tuple the values will be this.
# exc_tuple[0] value will be "ZeroDivisionError"
# exc_tuple[1] value will be "integer division or modulo by zero" (String passed as parameter to the exception class)
# exc_tuple[2] value will be "trackback object at (some memory address)"
    
# handling all exceptions - new code
def error_handling_new_code():    
    try:
        (x,y) = (5,0)
        z = x / y
        print(z)
    except:
        exception_message = sys.exc_info()[0]
        print("An error occurred. {}".format(exception_message))
        exception_message = utility_functions. get_exception_message()
        utility_functions.print_exception_message()      
               
#         path = os.path.abspath(__file__)
#         dir_path = os.path.dirname(path)
#         file = "error.log"
#         full_file = os.path.join(dir_path, file)
#         write_log_file(full_file, "error", exception_message)
        
    finally:
        pass
    
# handling all exceptions - old code
def error_handling_old_code():    
    try:
        (x,y) = (5,0)
        z = x / y
        print(z)
    except Exception as e:        
        print("An error occurred. {}".format(str(e)))
    finally:
        pass
    
def write_log_to_file(log_file_name, logevent_level, log_message):
    utility_functions.write_log_file(log_file_name, logevent_level, log_message)
    
if __name__ == '__main__':
#     no_error_handling()
    error_handling_new_code()
#     error_handling_old_code()

#     path = os.path.abspath(__file__)
#     dir_path = os.path.dirname(path)
#     file = "error1.log"
#     full_file = os.path.join(dir_path, file)
#     write_log_to_file(full_file, "info", "the message example")
    
