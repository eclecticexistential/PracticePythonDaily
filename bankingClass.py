import random

bank_accounts = {}
num_words = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f','g','h','i','j','k','l','m',0,1,2,3,4,5,6,7,8,9,'n','o','p','q','r','s','t','u','v','w','x','y','z',0,1,2,3,4,5,6,7,8,9]
num_only = [0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9]

def get_virtual_ID():
    iter = 11
    accountComp = ""
    while iter > 0:
        digitComp = random.choice(num_words)
        accountComp += str(digitComp)
        iter -= 1

    return accountComp

def get_account():
    iter = 11
    accountHuman = ""
    while iter > 0:
        digitHuman = random.choice(num_only)
        accountHuman += str(digitHuman)
        iter -= 1
    return accountHuman

def create_account(full_name,social,address):
    virtID = get_virtual_ID()
    account_num = get_account()
    issues = 0
    account_info = dict()
    for i in bank_accounts:
        if i == virtID:
            while i == virtID:
                try:
                    virtID = get_virtual_ID()
                finally:
                    if i == virtID:
                        print("Unable to create new Virtual ID. Contact admin.")
                        issues += 1
                        break
        if bank_accounts[i][0] == account_num:
            while bank_accounts[i][0] == account_num:
                try:
                    account_num = get_account()
                finally:
                    if bank_accounts[i][0] == account_num:
                        print("Unable to create new Account Number. Contact Admin.")
                        issues += 1
                        break
    if issues == 0:
        account_info[0] = account_num
        account_info[1] = full_name
        account_info[2] = social
        account_info[3] = address
        bank_accounts[virtID]=account_info
        return bank_accounts

class Person(object):
    def __init__(self,first_name,last_name,social,address):
        self.first_name = first_name
        self.last_name = last_name
        self.social = social
        self.address = address
    def get_account_number(self):
        self.full_name = self.first_name, self.last_name
        self.account_info = create_account(self.full_name, self.social, self.address)
        return self.account_info
    def get_info(self):
        self.get_account_number()


x = Person("Jared","Smith",555009999,"240 W. Main St")
y = Person("Rebecca","Codwell",111223333,"555 E. Market Ave")
z = Person("Harley","Jones",131720369,"500 N. Street Ave")
x.get_info()
y.get_info()
z.get_info()

for i in bank_accounts:
    print("Virtual ID: {} \nAccount Number: {} \nName: {} \nSocial: {} \nAddress: {}\n".format(i,bank_accounts[i][0],' '.join(bank_accounts[i][1]),bank_accounts[i][2],bank_accounts[i][3]))