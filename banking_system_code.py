# """
# Create a Python class called BankAccount which
# represents a bank account, having as attributes: accountNumber (numeric
# type), name (name
# of the account owner as string type), balance.
# Create a constructor with parameters: accountNumber, name, balance.
# Create a Deposit() method which
# manages the Deposit actions.
# Create a Withdrawal() method  which
# manages withdrawals actions.
# Create an bankFees() method to apply
# the bank fees with a percentage of 5% of the balance account.
# Create a Display() method to Display
# account details.
# Give the complete code for
# the  BankAccount class.Output:The output is :
# Account Number :   0000-0000-123

# Account Name :  Your Name

# Account Balance :  Rs. 5000
# """

# # initializing Class Bank


class Bank:
    
    
    # arguments necessary for Bank class
    def __init__(self, accountNumber, name, balance):
        self.balance = balance
        self.name = name
        self.accountNumber = accountNumber.zfill(11)
    
    # deposit amount function
    def Deposit(self, amount):
        self.balance += amount
    
    # withdrawing amount fucntion
    def Withdrawal(self, takeout):
        # if amount of withdrawal is more than current balance it wont withdraw
        if self.balance > takeout:
            self.balance -= takeout
        else:
            print('low balance')
    
    # calculating bankfees
    def Bankfees(self):
        bankfees = self.balance*(0.05)
        print(bankfees)
        
    # display of account information    
    def Display(self):
        print(f'''
              Account Number : {self.accountNumber}
              Account Name : {self.name}
              Account Balance : Rs. {self.balance}
              ''')
         
print('Welcome to SBP. ')

acc_num = input('Enter your account number :')   
acc_name = input('Enter account name : ')
acc_bal = int(input('Enter account balance : '))
         
# creating object of class
bk = Bank(acc_num, acc_name, acc_bal)

# while loop to run the commands until done 
while True:
     
    op = input('(d) Deposit, (w) Withdraw, (b) Check Balance, (f) Bankfees, (c) Close. ').upper()

    if op == 'D':
        amnt = int(input('amount to deposit : '))
        bk.Deposit(amnt)

    elif op == 'W':
        amnt = int(input('amount to deposit : '))
        bk.Withdrawal(amnt)

    elif op == 'B':
        bk.Display()
    
    elif op == 'F':
        bk.Bankfees()

    else:
        print('Thank you for using our bank! ')
        break
