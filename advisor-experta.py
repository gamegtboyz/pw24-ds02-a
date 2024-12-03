from experta import *
from random import choice


class Finance(Fact):
    pass


class InvestmentAdvisor(KnowledgeEngine):
    @Rule(Finance(SavingsAdequate=False))
    def savings(self):
        print("savings")


    @Rule(Finance(SavingsAdequate=True, IncomeAdequate=True))
    def stocks(self):
        print("stocks")


    @Rule(Finance(SavingsAdequate=True, IncomeAdequate=False))
    def mixture(self):
        print("mixture")





NoOfDependents = int(input("Please Enter No. of Dependents: ") ) #Z
AmountSaved = 10000
Income = 50000

IncomeSteady= input("Is Income Steady (yes/no)")
print ("IncomeSteady: " + str(IncomeSteady))

if IncomeSteady == "yes":
  IncomeSteady = True
else:
  IncomeSteady = False

ThresholdSavings = NoOfDependents * 3000
ThresholdIncome = 9000 + NoOfDependents * 2500


print ("NoOfDependents: " + str(NoOfDependents))
print ("AmountSaved: " + str(AmountSaved))
print ("Income: " + str(Income))
print ("ThresholdSavings: " + str(ThresholdSavings))
print ("ThresholdIncome: " + str(ThresholdIncome))






if AmountSaved >= ThresholdSavings:
  SavingsAdequate = True
else:
  SavingsAdequate = False

if IncomeSteady==True and Income >= ThresholdIncome:
  IncomeAdequate = True
else:
  IncomeAdequate = False


print ("SavingsAdequate: " + str(SavingsAdequate))
print ("IncomeAdequate: " + str(IncomeAdequate))




advisor = InvestmentAdvisor()
advisor.reset()

advisor.declare(Finance(SavingsAdequate=SavingsAdequate, IncomeAdequate=IncomeAdequate))
advisor.run()





'''
NoOfDependents = int(input("Please Enter No. of Dependents: ") ) #Z
AmountSaved = 100
Income = 50000

IncomeSteady= input("Is Income Steady (yes/no)")
print ("IncomeSteady: " + str(IncomeSteady))

if IncomeSteady == "yes":
  IncomeSteady = True
else:
  IncomeSteady = False

ThresholdSavings = NoOfDependents * 3000
ThresholdIncome = 9000 + NoOfDependents * 2500


print ("NoOfDependents: " + str(NoOfDependents))
print ("AmountSaved: " + str(AmountSaved))
print ("Income: " + str(Income))
print ("ThresholdSavings: " + str(ThresholdSavings))
print ("ThresholdIncome: " + str(ThresholdIncome))






if AmountSaved >= ThresholdSavings:
  SavingsAdequate = True
else:
  SavingsAdequate = False

if IncomeSteady==True and Income >= ThresholdIncome:
  IncomeAdequate = True
else:
  IncomeAdequate = False


print ("SavingsAdequate: " + str(SavingsAdequate))
print ("IncomeAdequate: " + str(IncomeAdequate))







if SavingsAdequate == False:
  recommendation = "Savings"
else:
  if IncomeAdequate == True:
    recommendation = "Stocks"
  else:
    recommendation = "Mixture"

print ("Recommendation: ", recommendation)
'''