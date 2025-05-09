import datetime
import os

Tracker = [] # to store expenses

from datetime import date 
d1 = str(date.today())

def add_expense(amount_spent, categary, payment_method, description="", date = d1):
    '''Helpful to add expense'''
    expense = {
        "Id" : len(Tracker) + 1,
        "Amount" : amount_spent,
        "Categary" : categary,
        "Payment" : payment_method,
        "Description" : description,
        "Date" : date,
    }
    Tracker.append(expense)
    print("Expense added Successfully...")  

def view():
    """Veiw the Expenses Being added"""
    for exp in Tracker:
        if len(exp["Description"]) == 0:
            print(f"{exp["Id"]}.For {exp["Categary"]} in Rs.{exp["Amount"]} by {exp["Payment"]} on {exp["Date"]}.")
        else:
            print(f"{exp["Id"]}.For {exp["Categary"]} in Rs.{exp["Amount"]} by {exp["Payment"]} on {exp["Date"]} due to --> {exp["Description"]}.")
    return

def rm_expense(id):
    """Helps to remove the expense"""
    for expense in Tracker:
        if expense["Id"] == id:
            Tracker.remove(expense)
            print(f"Expense Id {id} was removed sucessfully....")
        elif expense["Id"] > id :
            new_id = int(expense["Id"]) - 1
            expense["Id"] = new_id

def edit_expense(id,property,value):
    """Helps to edit Expense details"""
    for exp in Tracker:
        if exp["Id"] == id:
            exp[property] = value
            print("Changed Sucessfuly...")
    return

def generate_report(month,year):
    """help to create a text report."""
    from datetime import datetime
    
    repo_date = datetime.now().strftime('%Y-%m-%d')
    report = f"Expense Report for {month}-{year}\n"
    report += f"Generated on : {repo_date}\n"
    total = 0
    categories = {}
    
    # looping for getting month provided by user
    for expense in Tracker:
        exp_date = datetime.strptime(expense["Date"], "%Y-%m-%d") #converting date formate from str
        if exp_date.month == month and exp_date.year == year:
            total += expense["Amount"] #computing Total monthly expense
            categories[expense["Category"]] = categories.get(expense["Category"], 0) + expense["Amount"]
    report += f"Total Spent: {total}\n"
    for cat, amt in categories.items():
        report += f"{cat}: {amt}\n"
        
    # using the file handling creating report as text file
    with open(f"report_{month}_{year}.txt", "w") as file:
        file.write(report)
        
def visualize_report(month, year):
    from matplotlib import pyplot as plt
    from datetime import datetime
    """For providing graphical representation to user"""
    report = ""
    total = 0
    categories = {}

    for expense in Tracker:
        exp_date = datetime.strptime(expense["Date"], "%Y-%m-%d") #converting date formate from str
        if exp_date.month == month and exp_date.year == year:
            total += expense["Amount"] #computing Total monthly expense
            categories[expense["Category"]] = categories.get(expense["Category"], 0) + expense["Amount"]
    report += f"Total Spent: {total}\n"
    cate = list(categories.keys())
    val = list(categories.values())
    plt.plot(cate,val)
    Graph = plt.show()
    report += Graph
    with open(f"report_{month}_{year}.txt", "w") as file:
        file.write(report)

print('''Hello Dear User,
According to Your Ask choice option from the following.
Also give answer in A, B, C, D, E....
 [A] Add Expense.
 [B] Remove/Delete Expense.
 [C] View Expenses.
 [D] Edit Expense.
 [E] Generate Monthly Report.
 [F] Visualized Report.
 [G] Visualized The Report.''')

next = True
while (next == True):
    User = input("Enter Your Choise :")

    if User == 'A':
        amount = int(input("Enter the amount of expense = "))
        categori = input("Enter the Category of the expense :")
        method = input("Enter the method of payment[eg:UPI,cash...] :")
        Describe = input("Enter the description of expense :") 
        add_expense(amount, categori, method, Describe)

    elif User == 'B':
        print("Note: If you donot know the id then choice [C] ")
        idx = int(input("Enter the expense id :"))
        rm_expense(idx)

    elif User == 'C':
        view()

    elif User == 'D':
        print("Note: If you donot know the id then choice [C] ")
        idx = int(input("Enter the expense id :"))
        prop = input("Enter the property which should be edited : ")
        val = input("Enter new property value : ")
        edit_expense(idx,prop,val)

    elif User == 'E':
        mon = int(input("Enter the month of the report = "))
        years = int(input("Enter the year of the report = "))
        generate_report(mon,years)

    elif User == "F":
        mon = int(input("Enter the month of the report = "))
        years = int(input("Enter the year of the report = "))
        visualize_report(mon,years)
    
    elif User == "G":
        mon = int(input("Enter the month of the report = "))
        years = int(input("Enter the year of the report = "))
        
    else:
        print("Invalid Input")

    print('''Are you want to continue or do work on the expense...
    Yes --> choice = Y
    No --> choice = N''')
    choice = input ("Enter your choice : ")
    if choice == 'Y':
        pass
    elif choice == 'N':
        next = False