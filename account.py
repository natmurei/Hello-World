class Account(self):
    def __init__(self,first_name,second_name,balance):
        self. first_name = first_name
        self.second_name = second_name
        self.balance = balance
        # self.amount = amount

    def welcome(self):
        greet = "Hello, {} {} ,welcome to your account.your current balance is KES {}.".format(self.first_name,self.second_name,self.balance)
        return greeting
    
	def deposit(self,n):
		self.balance = self.amount + self.balance + n
		return "Hello {} {},welcome to your account.You have deposited KES {}.".format (self.first_name,self.second_name,n)

    def withdrawal (self,s):
        self.balance = self.balance - s
        return "Hello {} {} ,welcome to your account.You have withdrawn KES {}.".format (self.first_name,self.second_name,s)

    def show_balance (self):
        show_balance = self.balance
        return "Hello {} {},to your account.you current balance is {}.".format (self.first_name,self.second_name,self.balance)

