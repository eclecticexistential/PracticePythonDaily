import random

bank_accounts = []
num_words = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f','g','h','i','j','k','l','m',0,1,2,3,4,5,6,7,8,9,'n','o','p','q','r','s','t','u','v','w','x','y','z',0,1,2,3,4,5,6,7,8,9]
num_only = [0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9]

def get_account():
    iter = 11
    accountComp = ""
    accountHuman = ""
    accountDict = dict()
    while iter > 0:
        digitComp = random.choice(num_words)
        digitHuman = random.choice(num_only)
        accountComp += str(digitComp)
        accountHuman += str(digitHuman)
        iter -= 1

    accountDict[0] = accountComp
    accountDict[1] = accountHuman
    return accountDict

class Person(object):
    def __init__(self):
        self.first_name = input("First Name? ")
        self.last_name = input("Last Name? ")
    def account_number(self):
        self.account_number = get_account()
        return self.account_number
    def add_account(self):
        self.info = [self.first_name,self.last_name,self.account_number]
        bank_accounts.append(self.info)
    def get_info(self):
        x.account_number()
        x.add_account()
        return "Virtual ID: {} \nAccount Number: {} \nName: {} {}".format(bank_accounts[0][2][0],
                                                             bank_accounts[0][2][1],bank_accounts[0][0], bank_accounts[0][1])


x = Person()

print(x.get_info())