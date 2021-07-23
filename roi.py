import time
import sys

# Creates House class that stores object and functions
class House:
    def __init__(self, value, closingCost, downPayment, interestRate, years, PMI = 0, feesHOA = 0, vacRate = 5, capEx = 100, mangRate = 0):
        self.value = value
        self.closingCost = closingCost
        self.downPayment = downPayment
        self.interestRate = interestRate
        self.years = years
        self.PMI = PMI
        self.feesHOA = feesHOA
        self.vacRate = vacRate
        self.capEx = capEx
        self.mangRate = mangRate
        
    # Calculates mortgage from user inputs
    def mortgage(self):        
        moIntRate = (self.interestRate/100)/12
        principal = self.value - self.downPayment
        noPayments = self.years * 12
        monthlyMortgage = (principal * ((1 + moIntRate)**noPayments)*moIntRate)/(((1 + moIntRate)**noPayments)-1)
        return monthlyMortgage

    # Calculates income from user inputs
    def income(self, rent, misc):
        self.rent = rent
        self.misc = misc
        income = rent + misc
        return income

    # Calculates expenses based on user inputs and previously calculated numbers
    def expenses(self, tax, insurance, repairs):
        self.tax = tax
        self.insurance = insurance
        self.repairs = repairs
        self.propManage = self.rent * (self.mangRate / 100)
        vacancy = self.vacRate/100 * self.income(self.rent, self.misc)
        expense = self.mortgage() + tax + insurance + repairs + self.feesHOA + self.PMI + vacancy + self.capEx + self.propManage
        return expense

    # Calculates ROI and returns it as a decimal float
    def returnOnInvestment(self):
        totalInvestment = self.downPayment + self.closingCost
        moIncome = self.income(self.rent, self.misc)
        moExpenses = self.expenses(self.tax, self.insurance, self.repairs)
        return (((moIncome - moExpenses)*12)/totalInvestment)

# Function to test inputs
def is_number(string):
    try:
        if float(string) and string[0] != '-':
            return True
    except ValueError:
        return False

# Parent loop that maintains the program until user quits
while True:
    print('=============================================================================================')
    print('Welcome to the ROI calculator, where we help you evaluate if a property is a good investment.')
    print('=============================================================================================')
    time.sleep(1)
    initial = input('Do you want to calculate a Return On Investment for a potential rental property? (Y/N) ')
    if initial.lower() == 'y':
        # Beginning of user inputs for mortgage calculation
        print('Okay, let me ask you a few questions about your potential rental property.')
        time.sleep(0.5)
        while True:    
            value = input('What would be the purchase price of your rental property? ')
            if is_number(value):
                value = int(value)
                break
            else:
                print('Please enter a valid number.')
        while True:
            closeResp = input('What would be the estimated closing costs of this property? ')
            if is_number(closeResp):
                closingCost = float(closeResp)
                break
            else:
                print('Please enter a valid number.')
        while True:
            dwnPay = input('What percentage would you put down? If none, enter 0: ')
            if is_number(dwnPay):
                downPayment = (float(dwnPay)/100) * value
                break
            else:
                print('Please enter a valid number.')
        while True:
            rate = input('What would your interest rate be? ')
            if is_number(rate):
                interestRate = float(rate)
                break
            else:
                print('Please enter a valid number.')
        while True:
            years = input('How many years would your loan be for? ')
            if years.isnumeric() and years[0] != '-':
                years = int(years)
                break
            else:
                print('Please enter a valid number.')
        rentalProperty = House(value, closingCost, downPayment, interestRate, years)
        print('Calculating your mortgage...')
        time.sleep(1)
        print('...')
        time.sleep(1)
        print('...')
        mortgage_string = "${:,.2f}".format(rentalProperty.mortgage())
        print(f'Your monthly mortgage payment will be {mortgage_string}. This is before taxes and insurance.')
        time.sleep(2)
        print('Now lets estimate your income.')
        # Beginning of inputs to calculate income
        while True:
            incResponse = input('How much do you estimate to charge for rent? ')
            if is_number(incResponse):
                rent = float(incResponse)
                break
            else:
                print('Please enter a valid number.')
        while True:
            miscResponse = input('Do you estimate any other income from this property? (y/n) ')
            if miscResponse.lower() == 'y':
                miscResponse = input('What is your estimated extra income? ')
                if is_number(miscResponse):
                    misc = float(miscResponse)
                    break
                else:
                    print('Please enter a valid number.')
            elif miscResponse.lower() == 'n':
                misc = 0
                break
            else:
                print('Sorry, you must select yes or no.')
        print('Calculating your income...')
        time.sleep(1)
        print('...')
        time.sleep(1)
        print('...')
        income_string = "${:,.2f}".format(rentalProperty.income(rent, misc))
        print(f'Your estimated monthly income is: {income_string}')
        time.sleep(2)
        print('Now lets estimate your expenses.')
        time.sleep(1)
        # Beginning of inputs to calculate expenses
        while True:
            taxResponse = input('What is your estimated annual tax for this property? ')
            if is_number(taxResponse):
                tax = float(taxResponse)/12
                break
            else:
                print('Please enter a valid number.')            
        while True:
            insResponse = input('What is your estimated monthly insurance? ')
            if is_number(insResponse):
                insurance = float(insResponse)
                break
            else:
                print('Please enter a valid number')
        while True:
            repResponse = input('What is your estimated monthly budget for repairs? ')
            if is_number(repResponse):
                    repairs = float(repResponse)
                    break
            else:
                print('Please enter a valid number')
        while True:
            if float(dwnPay) < 20:
                print('You have a down payment of less than 20%, this means you need Private Mortgage Insurance (PMI)\nYour PMI rate is 1%')
                rentalProperty.PMI = ((rentalProperty.value - downPayment) * .01)/12
                break
            elif float(dwnPay) >= 20:
                print('You qualify for a PMI free loan. Congratulations!!')
                break
            else:
                print('Please enter a valid number')
        time.sleep(1)
        print('Just a few more questions, I promise we are almost finished.')
        time.sleep(1)
        while True:
            hoaResponse = input('Will this property incur HOA fees? (y/n) ')
            if hoaResponse.lower() == 'y':
                while True:
                    feeResponse = input('What are the monthly HOA fees for this property? ')
                    if is_number(feeResponse):
                        rentalProperty.feesHOA = float(feeResponse)
                        break
                    else:
                        print('Please enter a valid number')
                break
            elif hoaResponse.lower() == 'n':
                break
            else:
                print('Sorry, you must select yes or no.')
        while True:
            vacYN = input('Industry standard for vacancy rate is 5% of the rent, do you want to change this? (y/n) ')
            if vacYN.lower() == 'y':
                while True:
                    newVacRate = input('What percentage of the estimated rent do you want to budget for vacancy rate? ')
                    if is_number(newVacRate):
                        rentalProperty.vacRate = float(newVacRate)
                        break
                    else:
                        print('Please enter a valid number')
                break
            elif vacYN.lower() == 'n':
                break
            else:
                print('Sorry, you must select yes or no.')
        while True:
            print('Some rental owners budget money for future major repairs. Industry standard is $100.')
            time.sleep(.5)
            capExResponse = input('Do you want to enter a custom amount? (y/n) ')            
            if capExResponse.lower() == 'y':
                while True:
                    newCapEx = input('How much per month do you want to set aside for potential major expense? ')
                    if is_number(newCapEx):
                        rentalProperty.capEx = float(newCapEx)
                        break
                    else:
                        print('Please enter a valid number')
                break
            elif capExResponse.lower() == 'n':
                break
            else:
                print('Sorry, you must select yes or no.')
        while True:
            propManResp = input('Are you using a property management company to manage your property? (y/n) ')
            if propManResp.lower() == 'y':
                while True:
                    newPropMan = input('What percentage of rent does you property management charge? ')
                    if is_number(newPropMan):
                        rentalProperty.mangRate = float(newPropMan)
                        break
                    else:
                        print('Please enter a valid number')
                break
            elif propManResp.lower() == 'n':
                break
            else:
                print('Sorry, you must select yes or no.')
        print('Calculating your expenses...')
        time.sleep(1)
        print('...')
        time.sleep(1)
        print('...')
        expense_string = "${:,.2f}".format(rentalProperty.expenses(tax, insurance, repairs))
        print(f'Your estimated expenses for this property are {expense_string}')
        time.sleep(2)
        # Calculating ROI, derived from previous information.
        print('Now we will calculate your return on investment, and determine if this property is a good investment.')
        print('Calculating your return on investment...')
        time.sleep(1)
        print('...')
        time.sleep(1)
        print('...')
        time.sleep(1)
        print('...')
        time.sleep(1)
        print('...')
        finalROI = rentalProperty.returnOnInvestment()
        roi_string = "{:.2%}".format(finalROI)
        print(f'The estimated return on investment for this property is: {roi_string}')
        time.sleep(1)
        if finalROI * 100 > 12:
            print('A ROI of 12% or higher is a good investment. Congratulations on starting a life of income freedom!')
        elif finalROI * 100 > 8:
            print('A ROI of 8-12% is a decent investment. You may want to look for better opportunities.')
        elif finalROI * 100 >= 0:
            print('A ROI of less than 8% is not a good investment. We suggest looking for another property to purchase.')
        else:
            print("'You would lose money on this property. We strongly suggest not buying this as a rental property. But ultimately\nit's your decision and life and you can do what you want. It is a free country and all and, although money can't buy happiness,\nit can buy freedom from a reliance of cyclical capitalistic oppression designed to keep poor people poor and restrict\nclass movement in order to maintain a select group of elitists and their power structure. But you do what you want.")
            time.sleep(20)
        while True:
            another = input('Do you want to evaluate another property? (y/n) ')
            if another.lower() == 'y':
                break
            elif another.lower() == 'n':
                print('Thank you for using our program. Happy investing!!!')
                sys.exit(0)
            else:
                print('Sorry, you must select yes or no.')
    elif initial.lower() == 'n':
        quit = input('Are you sure you want to quit? (Y/N) ')
        if quit.lower() == 'y':
            print('Thank you for using our program, happy investing!')
            break
    else:
        print('Sorry, you must select yes or no.')
