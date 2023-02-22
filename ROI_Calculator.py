class ROICalculator():
    def __init__(self):
        self.incomes = {}
        self.expenses = {}
        self.investment = {}
        self.cash_flow_calculated = False
        self.roi_calculated = False
        self.roi = 0
        self.cash_flow = 0
    
    def addIncome(self, type, amount):
        self.incomes[type] = amount
        self.cash_flow_calculated = False
        self.roi_calculated = False

    def addExpense(self, type, amount):
        self.expenses[type] = amount
        self.cash_flow_calculated = False
        self.roi_calculated = False
    
    def addInvestment(self, type, amount):
        self.investment[type] = amount
        self.cash_flow_calculated = False
        self.roi_calculated = False

    def printIncomes(self):
        print('')
        print("Monthly Income:")
        if len(self.incomes) > 0:
            for key, value in self.incomes.items():
                print(f"{key}: ${value}")
        else:
            print("No Income Sources Provided")

    def printExpenses(self):
        print('')
        print("Monthly Expenses:")
        if len(self.expenses) > 0:
            for key, value in self.expenses.items():
                print(f"{key}: ${value}")
        else:
            print("No Expenses Provided")

    def printInvestments(self):
        print('')
        print("Investments:")
        if len(self.investment) > 0:
            for key, value in self.investment.items():
                print(f"{key}: ${value}")
        else:
            print("No Investments Provided")

    def printAll(self):
        self.printIncomes()
        self.printExpenses()
        self.printInvestments() 

    def calculateCashFlow(self):
        # check to see if cash flow has been calculated
        if not self.cash_flow_calculated:
            income_total = 0
            expense_total = 0
            for value in self.incomes.values():
                income_total += value
            for value in self.expenses.values():
                expense_total += value
            self.cash_flow = income_total - expense_total
            self.cash_flow_calculated = True
        return self.cash_flow

    def calculateROI(self):
        # check to see if ROI has been calculated
        if not self.roi_calculated:
            annual_cash_flow = self.calculateCashFlow() * 12
            investment_total = 0
            # roi is undefined if investments are zero
            try:
                for value in self.investment.values():
                    investment_total += value
                self.roi = (annual_cash_flow / investment_total) * 10000
                # formatting
                self.roi //= 1
                self.roi /= 100 
            except:
                self.roi = 'Undefined'
            self.roi_calculated = True
        return self.roi
    
roi_calculator = ROICalculator()
while True:
    try:
        action = int(input("=====ROI Calculator=====\n[1]Update Income\n[2]Update Expenses\n[3]Update Investments\n[4]Show Info\n"))

        # Update
        if action > 0 and action < 4:
            while True:
                if action == 1:
                    list_name = "Monthly Income"
                    roi_calculator.printIncomes()
                if action == 2:
                    list_name = "Monthly Expense"
                    roi_calculator.printExpenses()
                if action == 3:
                    list_name = "Initial Investment"
                    roi_calculator.printInvestments()              
                update = input(f"\nUpdate {list_name} List? Y/N ")
                if update.upper() == 'Y':
                    type = input(f"\nInput {list_name} Type ")
                    try:
                        amount = float(input(f"Input {type.title()} Amount $"))
                        if action == 1:
                            roi_calculator.addIncome(type.title(), amount)
                        if action == 2:
                            roi_calculator.addExpense(type.title(), amount)
                        if action == 3:
                            roi_calculator.addInvestment(type.title(), amount)
                    except:
                        print("Invalid Input!")
                else:
                    break
        
        # Show Info
        elif action == 4:
            roi_calculator.printAll()
            print('')
            print(f"Monthly Cash flow: ${roi_calculator.calculateCashFlow()}")
            print(f"Return On Investing: {roi_calculator.calculateROI()}%")
            print('')
            finished = input("Finished? Y/N ")
            if finished.upper() == 'Y':
                break

        else:
            print("Please input valid response")

    except:
        print("Please input valid response")
        

