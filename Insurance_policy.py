#age, incom, educate
#y=0.042*x1+0.008*x2+0.2*x3-1.53   equation 3:1
#income=integer 10<1000

import numpy as np
 
print("Welcome_to_the_Insurance_Policy_Prediction_System\n")
def predict(age, income, edu):
    z = 0.042 * age + 0.008 * income + 0.2 * edu - 1.53
    y = sigmoid(z)
    return y

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

#Age
age = int(input("Please_enter_your_Age:"))
if age < 18 or age > 100:
    print("Age must be between 18 and 100.")
    exit()

#Income
income = int(input("Please_enter_your_Income_from_range_between_10<=1000:"))
if income < 10 or income > 1000:
    print("Income_must_be_between_10_and_1000.")
    exit()

#education
edu = input("have_you_completed_your_education? (yes/no): ")
if edu == "yes" or "y" or "Yes":
    edu = 1
elif edu == "no" or "n" or "No":
    edu = 0
else:
    print("please_enter_valid_input")
    exit()

#Prediction
prediction = predict(age, income, edu)

if prediction >= 0.5:
    print("Congratulations!_You_are_eligible_for_the_insurance_policy.")
else:
    print("Sorry!_You_are_not_eligible_for_the_insurance_policy.")

#completed 3:1 system