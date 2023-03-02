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
income_types = ["Rental","Laundry","Storage","Other Income"]
expense_types = ["Tax","Insurance","Electric","Water","Sewer","Garbage","Gas","HOA Fees","Lawn/Snow","Vacancy Fund",\
                 "Average Repairs","CapEx","Property Management","Mortgage","Other"]
investment_types = ["Down Payment","Closing Costs", "Rehab Budget", "Other Investments"]

print("INCOME SOURCES:")
for income in income_types:
    while True:
        try:
            roi_calculator.addIncome(income, float(input(f"Enter {income} Income: $")))
            break
        except:
            print('Enter Valid Amount!')

print("\nMONTHLY EXPENSES:")
for expense in expense_types:
    while True:
        try:
            roi_calculator.addExpense(expense, float(input(f"Enter {expense} Expense: $")))
            break
        except:
            print('Enter Valid Amount!')
print("\nINITIAL INVESTMENTS:")
for investment in investment_types:
    while True:
        try:
            roi_calculator.addInvestment(investment, float(input(f"Enter {investment} Amount: $")))
            break
        except:
            print('Enter Valid Amount!')

roi_calculator.printAll()
print('')
print(f"Monthly Cash flow: ${roi_calculator.calculateCashFlow()}")
print(f"Return On Investing: {roi_calculator.calculateROI()}%")