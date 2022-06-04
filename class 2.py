#: part of oop
class employee():
    def __init__(self):
        self.__employee_name = ""
        self.__employee_ID = ""
        self.__ammount_paid = 0.0

    def setEmployeeName (self, n):
        self.__employee_name = n

    def setEmployeeID (self , ID):
        self.__employee_ID = ID

    def setammountpaid (self , ammount_paid):
        self.__ammount_paid = ammount_paid

    def getemployeename (self):
        return self.__employee_name

    def getemployeeID (self):
        return self.__employee_ID

    def getammountpaid (self):
        return self.__ammount_paid

    def getdetails (self):
         print(self.__employee_name , "with ID" , self.__employee_ID , "has paid ammount :" , self.__ammount_paid )


employeepayment = employee()
employeepayment.setEmployeeName("bing boy bitch")
employeepayment.setEmployeeID("4567")
employeepayment.setammountpaid(0.1)
print(employeepayment.getdetails())


