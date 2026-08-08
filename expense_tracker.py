expenses=[]

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
     for index, expense in enumerate(expenses, start=1):
          print(f"{index}. Category: {expense['category']}, Amount: ₹{expense['amount']:.2f}")

def delete_expense():
     if not expenses:
          print("\nNo expenses to delete.")
          return
     view_expenses()
     try:
         number=int(input("Enter the number of the expense to delete:"))
         if 1 <= number <= len(expenses):
                deleted_expense=expenses.pop(number-1)
                print(f"Deleted expense: Category: {deleted_expense['category']}, Amount: ₹{deleted_expense['amount']:.2f}")
         else:
               print("Invalid expense number.")
     except ValueError:
          print("Please enter a valid number.")
def total_expense():
     total=sum(expense['amount'] for expense in expenses)
     print(f"\nTotal Expense: ₹{total:.2f}")

def main():
     while True:
          print("\n---^_^EXPENSE TRACKER^_^---")
          print("1. Add Expense")
          print("2. View Expenses")
          print("3. Delete Expense")
          print("4. Total Expense")
          print("5. Exit")
          choice=input("Enter your choice(1-5):")
          if choice=="1":
               add_expense()
          elif choice=="2":
               view_expenses()
          elif choice=="3":
               delete_expense()
          elif choice=="4":
               total_expense()
          elif choice=="5":
               print("Exiting the program.")
               break
          else:
               print("Invalid choice. Please try again.")
print("❤(❁´◡`❁)THANK YOU FOR USING THE EXPENSE TRACKER!(❁´◡`❁)❤")
main()
                       