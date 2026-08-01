expense={}

def add_expense():
     while True:
          print("\n---^_^ADD EXPENSE^_^---")
          category=input("ENTER EXPENSE CATEGORY:")
          amount=float(input("ENTER AMOUNT{₹}:"))
          expense={
               "category":category,
               "amount":amount
          }
          expenses.append(expense)
          print("expense added successfully")
          more=input("do you want add another expense?(yes/no):").lower()
          if more != "yes":
              break
def view_expenses():
     if not expenses:
          print("\nNo expenses recorded.")
          return
     print("\n---Your Expenses---")
     for index,expense in enumerate(expense,start=1):
          print(f"{index}. Category: {expense['category']}, Amount: ₹{expense['amount']:.2f}") 

def delete_expense():
     if not expenses:
          print("\nNo expenses to delete.")
          return
     view_expenses()
     try:
         number=int(input("Enter the number of the expense to delete:"))
         
