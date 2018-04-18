
from employee_derived_class import Employee

def main():
    employee_class = Employee("John", "Smith")  
    employee_info = employee_class.employee_name()
    print("Full Information: {}".format(employee_info))
    
    employee_class = Employee("John", "Smith", "1099")    
    employee_info = employee_class.employee_name_id()
    print("Full Information: {}".format(employee_info))   

if __name__ == '__main__':
    main()