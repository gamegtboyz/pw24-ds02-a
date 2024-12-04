# import ALL modules from experta library, and import choice from random library too.
from experta import *
from random import choice

# initiate the class called 'Finance', which is inherited their own propoerties from experta's 'Fact' class.
class Finance(Fact):
    pass

# create the class called 'InvestmentAdvisor', which is inherited their own properties from 'KnowledgeEngine' module.
# this class is placed to make the decision based on the defined income.
class InvestmentAdvisor(KnowledgeEngine):
    @Rule(Finance(SavingsAdequate = False))
    def savings(self):
        print('Please save some money.')

    @Rule(Finance(SavingsAdequate = True, IncomeAdequate = True))
    def stocks(self):
        print('Go with the stocks.')

    @Rule(Finance(SavingsAdequate = True, IncomeAdequate = False))
    def stocks(self):
        print('Just mix it. It\'s fine.')

# define the input, then calculate the output.
# this to gather the input
NoOfDependents = int(input("Please specify the number of your dependencies: "))
AmountSaved = 10000
Income = 5000
IncomeSteady = input("Is your income steady? (yes/no): ")
if IncomeSteady == 'yes':
    IncomeSteady = True
else:
    IncomeSteady = False

# calculate the threshold from entries
ThresholdSavings = NoOfDependents * 3000
ThresholdIncome = 9000 + (NoOfDependents * 2500)

if AmountSaved >= ThresholdSavings:
    SavingsAdequate = True
else:
    SavingsAdequate = False

# evaluate the adequecies of savings and income
if IncomeSteady == True and Income >= ThresholdIncome:
    IncomeAdequate = True
else:
    IncomeAdequate = False

# create the instance of InvestmentAdvisor class
advisor = InvestmentAdvisor()

# since 'InvestmentAdvisor' class is inherited from 'KnowledgeEngine' class, we need to cleared the previously-stored output in KnowledgeEngine class to ensure that the instance is cleaned and free from previuosly-stored data.
advisor.reset()

# we take the input onto the 'Fact' class, use them to calculate the defined outcome.
advisor.declare(Finance(SavingsAdequate=SavingsAdequate, IncomeAdequate=IncomeAdequate))

# run the expert system as defined.
advisor.run()