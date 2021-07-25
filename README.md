# roi_calculator

## Project:
The ROI Calculator is designed to take in user inputs and caluculate, and evaluate, the return on investement for a potential rental property.

## Functionality:
This program starts by accepting aspects of the initial purchase of the property and returns the expected monthly mortgage payment. 
It then collects information for both income and expenses and calculates the ROI. Finally, it returns a suggestion based on industry
standards.

## Program:
The program operates with a series of questions for the customer about the potential property. All of these inputs are checked for validity
and type match before commiting to a variable.

#### Mortgage
The program calculates the monthly mortgage payment based on loan amount, interest rate and length of loan. It does not add in PMI, insurance or property taxes.

#### Income
The income for the rental property is calulated with rent, and any other miscellaneous income.

#### Expenses
Monthly expenses for the property, including tax, insurance, repair budget, any HOA fees, Private Mortgage Insurance, vacancy budget, capital expenses and property management fees.
More information provided in Assumptions.

#### Return On Investment
ROI takes the annual cash flow (monthly income - monthly expenses, mulitplied by twelve) and divides that by the initial investment. The initial investment
is the downpayment and closing costs.

## Assumptions
This program makes several assumptions.
Mortage: Does not roll closing costs, insurance or tax into calculation. The user is informed of this.
PMI: PMI rate is assumed to be 1%, it is automatically added if the downpayment is less than 20% of the value of the house.
HOA Fees: Assumed to be zero unless user provides another amount.
Vacancy budget: Assumed to be 5% of the rent unless otherwise specified by the user.
Capital Expense: A budget for major repairs, the program assumes $100 unless otherwise specified by the user.
Property Management: The management rate is assumed to be 0%, user can change this.
Final Evaluations: The evaluation is split up in four tiers, according to normal industry suggestion. It provides advice for each potential property.

## Test Cases
Two test cases were used. The first one used the numbers provided by the video accompanying this assignment. The mortgage numbers are used to simulate the mortgage
payment he had in the video. It will be an extra sixty something cents but it will suffice for this.
The second case is one that attmepts to utilize all aspects of the program, and each input will be the opposite of the first test case. Any default number in the first
case will be a custom number in this case, and vice verse.

## Test Case #1:
House Value: $200,000<br/>
Closing Costs: $3000<br/>
Down Payment: 20% (input 20, not 0.2)<br/>
Interest Rate: 5.02<br/>
Loan Length: 30 years<br/>

Mortgage: $860.87

Income:
Rent: 2,000<br/>
Misc: none<br/>

Income: $2,000

Expenses:
Annual Tax: 1,800<br/>
Monthly Insurance: 100<br/>
Repairs: 100<br/>
PMI: automatically declined due to 20% down payment<br/>
HOA Fees: none<br/>
Vacancy Rate: default (5%)<br/>
Capital Expense: defualt ($100)<br/>
Property Mangement: 10<br/>

Expense: $1,610.87

Return on Investment: 10.86%, ok but may want to look for other opportunities.

## Test Case #2:
House Value: $400,000<br/>
Closing Costs: $3000<br/>
Down Payment: 15% (input 15, not 0.15)<br/>
Interest Rate: 2.96<br/>
Loan Length: 30 years<br/>

Mortgage: $1,426.13

Income:
Rent: 2,550<br/>
Misc: 120<br/>

Income: $2,670

Expenses:
Annual Tax: 2,400<br/>
Monthly Insurance: 66<br/>
Repairs: 100<br/>
PMI: automatically caluclated as 1% of the rent = $283.33<br/>
HOA Fees: 125<br/>
Vacancy Rate: 7.5%<br/>
Capital Expense: 120<br/>
Property Mangement: none<br/>

Expense: $2,511.71

Return on Investment: %3.01, not suggested to buy

## Lessons Learned
This project emphasized the importance of planning appropriately. The nature of the project is difficult to manage based on the number of user inputs required.
I think this project would've worked much better with a form in a gui, but it functions well as it is. The main portion of the program is pretty heavy, and although
the calculations are all done in functions of the House class, the major lifting is done in the main portion.<br/>

What I think this program does well is that the user has to supply the least amount of information. The user only has to provide the raw information and the program
does most of the math. While it does require handling more inputs, it is technically more user friendly because they don't have to do any other calculations beforehand.
I think this program also provides a certain amount of charm and character. It isn't really needed but I think it makes it a little more fun for this kind of project.


