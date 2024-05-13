   class bank_account:
       def __init__(self, username, password):
           self.username = username
           self.password = password
           self.balance = 0
    
       def login(self, username, password):
          if self.username == username and self.password ==password:
              return True
          else: 
              return False
         
       def  deposit(self, amount):
           if amount >=0:
              self.balance += amount
              print("Amount of", {amount}, "deposited in your Account")
              print("your current Balance : ", {self.balance})
           else:
               print("invalid Amount")
       
       def withdrawal(self, amount):
            if amount >0 and amount <= self.balance:
                self.balance -= amount
                print("An amount of ", amount, "withdrawn from your account")
                print("your remaining Balance is :", {self.balance})
            else:
               print("you don't have sufficient balance in your account")
               
   if __name__== "__main__":
        username = input("Enter Username: ")
        password = input("Enter Password :")
    
        account = bank_account(username, password)
        
        if account.login(username, password):
            print("Login successful")
            while True:
                print("\nOptions")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Exit")
                
                choice = input("Enter your choice :")
                
                if choice == '1':
                   amount = float(input("Enter an amount to deposit :"))
                   account.deposit(amount)
                elif choice == '2':
                    amount = float(input("Enter an amount to withdraw :"))
                    account.withdrawal(amount)
                elif choice == '3':
                    print("Exit program.")
                    break
                else:
                    print("invalid Username and Password")
                    
                 
                
                
    
                
