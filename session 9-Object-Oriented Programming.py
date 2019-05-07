#Session_9
#Bank_account_claases

class Person:
    '''to handle person's details'''
    def __init__(self, fn, ln):
        self.first_name = fn
        self.last_name = ln
        self.address = None #addresses stored by strings
    def set_address(self, adr):
        self.address = adr #strings

class IndividualBankAccount:
    '''to handle individual bank account data'''
    def __init__(self, sort_code, account_number, owner):
        '''TD implement this; creates a bank account
        with sort code as string, account number as string,
        and owner as Person'''
        self.sort_code=sort_code
        self.account_number=account_number
        self.Person=owner
    def set_sort_code(self, sort_code):
        '''TD implement this; updates sort code'''
        self.sort_code=sort_code
    def get_sort_code(self):
        '''TD implement this; returns sort code'''
        return self.sort_code
    def set_account_number(self, account_number):
        '''TD implement this; updates account number'''
        self.account_number=account_number
    def get_account_number(self):
        '''TD implement this; returns account number'''
        return self.account_number
    def get_account_data(self):
        '''TD implement this; returns string "FN LN SC AN"
        where FN and LN are owner's first and last names,
        SC is sort code, AN is account number'''
        s=str(self.Person.first_name)+" "+str(self.Person.last_name)+" "+str(self.sort_code)+" "+str(self.account_number)
        return s

class SharedBankAccount:
    '''to handle data of an account that has several owners'''
    def __init__(self, sort_code, account_number, owners):
        '''TD implement this; creates a bank account
        with sort code as string, account number as string,
        and owners as a list of Persons'''
        self.sort_code=sort_code
        self.account_number=account_number
        self.Person=owners
    def set_sort_code(self, sort_code):
        '''TD implement this; updates sort code'''
        self.sort_code=sort_code
    def get_sort_code(self):
        '''TD implement this; returns sort code'''
        return sort_code
    def set_account_number(self, account_number):
        '''TD implement this; updates account number'''
        self.account_number=account_number
    def get_account_number(self):
        '''TD implement this; returns account number'''
        return self.account_number
    def get_account_data(self):
        '''TD implement this; returns string
        "FN1 LN1, FN2 LN2, ..., FNM LNM, SC AN"
        where FNi LNi is the i-th owner first and last names,
        SC is sort code, AN is account number'''
        lst=[]
        for i in self.Person:
            lst.append(i.first_name)
            lst.append(i.last_name)
        s=str(lst[0])+" "+str(lst[1])+", "+str(lst[2])+" "+str(lst[3])+", "+str(self.sort_code)+" "+str(self.account_number)
        return s

#NO modifications below this line
import sys
complete_input = sys.stdin.readlines()
for line in complete_input: exec(line)

#Bank_account_classes_with_inheritance

class Person:
    '''to handle person's details'''
    def __init__(self, fn, ln):
        self.first_name = fn
        self.last_name = ln
        self.address = None #addresses stored by strings
    def set_address(self, adr):
        self.address = adr #strings

class BankAccount:
    def __init__(self, sort_code, account_number):
        '''TD implement this; creates a bank account
        with sort code as string and account number as string'''
        self.sort_code=sort_code
        self.account_number=account_number
    def set_sort_code(self, sort_code):
        '''TD implement this; updates sort code'''
        self.sort_code=sort_code
    def get_sort_code(self):
        '''TD implement this; returns sort code'''
        return self.sort_code
    def set_account_number(self, account_number):
        '''TD implement this; updates account number'''
        self.account_number=account_number
    def get_account_number(self):
        '''TD implement this; returns account number'''
        return self.account_number
    def get_account_data(self):
        '''TD implement this; returns string "SC AN"
        where SC is sort code, AN is account number'''
        s=str(self.sort_code)+" "+str(self.account_number)
        return s

class IndividualBankAccount(BankAccount):
    def __init__(self, sort_code, account_number, owner):
        super().__init__(sort_code, account_number)
        '''line above sets up sc and number
        TD implement setting up an owner as Person'''
        self.Person=owner
    def get_account_data(self):
        '''TD implement this; returns string "FN LN SC AN"
        where FN and LN are owner's first and last names,
        SC is sort code, AN is account number'''
        s=str(self.Person.first_name)+" "+str(self.Person.last_name)+" "+str(self.sort_code)+" "+str(self.account_number)
        return s

class SharedBankAccount(BankAccount):
    def __init__(self, sort_code, account_number, owners):
        super().__init__(sort_code, account_number)
        '''line above sets up sc and number
        TD implement setting up an owners as a list of Persons'''
        self.Persons=owners
    def get_account_data(self):
        '''TD implement this; returns string
        "FN1 LN1, FN2 LN2, ..., FNM LNM, SC AN"
        where FNi LNi is the i-th owner first and last names,
        SC is sort code, AN is account number'''
        lst=[]
        for i in self.Persons:
            lst.append(i.first_name)
            lst.append(i.last_name)
        s=str(lst[0])+" "+str(lst[1])+", "+str(lst[2])+" "+str(lst[3])+", "+str(self.sort_code)+" "+str(self.account_number)
        return s

#NO modifications below this line
import sys
complete_input = sys.stdin.readlines()
for line in complete_input: exec(line)
