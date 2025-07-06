from datamanage import DataManager
data_manager = DataManager()
fistName = input("Enter your first name : ").title()
lastName = input("Enter your last name : ").title()
email = input("Enter your email : ").title()
data_manager.add_entry(fistName,lastName,email)