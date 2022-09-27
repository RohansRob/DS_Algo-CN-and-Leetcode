class ExpenseTracker:
    "this is a class to do expense tracking"

    def __init__(self):
        pass

#   //simple implementation of python class
  obj1 = ExpenseTraker()  
  def __init__(self,date , description,transaction_type , amount):
    self.date = date
    self.description = description
    self.transaction_type = transaction_type
    self.amount = amount



obj2 = ExpenseTracker("12Jan","Dinner","debit","1000")

obj2.amount

obj3 = ExpenseTracker("1jan","salary credited", "credited","500")

obj3.amount