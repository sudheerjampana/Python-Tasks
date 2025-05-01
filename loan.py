username=str(input("Please enter your name: "))
gender=str(input("enter your gender: "))
age=int(input("enter your age: "))
if age>=18 and age<=58:
    print(" your eligible for loan by considering age:",age)
else:
    print("below 18 years old are not eligible for loan")
    exit()
annual_income=int(input("please enter your annual income: "))
if annual_income>=350000:
    print("your eligible for nxt process of personal loan: ")
else:
    print("you are not eligible for personal loan due to your annual income is less than 3,50,000rs.")
    exit()
CIBIL_score=int(input("please enter your CIBIL Score: "))
if CIBIL_score>=300 and CIBIL_score<=900 :
    print("you are eligible for personal loan. See loan offers as per your credintials")
else:
    print("Sorry,you are not eligible for personal loan ")
    print("you must having cibil score between 300-900")
    exit()
if ((age>=18 and age<=45) and (annual_income>=350000 and annual_income<=800000) and (CIBIL_score>=300 and CIBIL_score<=650)):
    loan_range40=((40/100)*annual_income)
    loan_range90=((90/100)*annual_income)
    print("you are eligible for getting loan range from",loan_range40,loan_range90)
elif (CIBIL_score>650)and(annual_income>=350000 and annual_income<=800000):
    loan_range40_1=((40/100)*annual_income)
    loan_range120=((120/100)*annual_income)
    print("you are eligible for getting loan range from",loan_range40_1,loan_range120)
elif(annual_income>800000 and annual_income<=1500000) and (CIBIL_score>=300 and CIBIL_score<=650):
    loan_range40_2=((40/100)*annual_income)
    loan_range80=((80/100)*annual_income)
    print("you are eligible for getting loan range from",loan_range40_2,loan_range80)
elif((CIBIL_score>650)and(annual_income>800000 and annual_income<=1500000)):
    loan_range40_3=((40/100)*annual_income)
    loan_range90_1=((90/100)*annual_income)
    print("you are eligible for getting loan range from",loan_range40_3,loan_range90_1)
elif(annual_income>1500000)and(CIBIL_score>=300 and CIBIL_score<=650):
    loan_range40_4=((40/100)*annual_income)
    loan_range90_2=((90/100)*annual_income)
    print("you are eligible for getting loan range from",loan_range40_4,loan_range90_2)
elif(CIBIL_score>650)and(annual_income>1500000)and(age>=18 and age<=45):
    loan_range40_5=((40/100)*annual_income) 
    loan_range=((100/100)*annual_income)
    print("you are eligible for getting loan range from",loan_range40_5,loan_range)
else:
    print("**you belongs to second category**")

if((age>=46 and age<=58)and(annual_income>=350000 and annual_income<=800000)and(CIBIL_score>=300 and CIBIL_score<=650)):
    loan_range_40=((40/100)*annual_income)
    loan_range70=((70/100)*annual_income)
    print("you are eligible for getting loan range from",loan_range_40,loan_range70)
elif(CIBIL_score>650 and(annual_income>=350000 and annual_income<=800000)):
    loan_range_40_1=((40/100)*annual_income)    
    loan_range75=((75/100)*annual_income)
    print("you are eligible for getting loan range from",loan_range_40_1,loan_range75)
elif(annual_income>800000 and annual_income<=1500000)and(CIBIL_score>=300 and CIBIL_score<=650):
    loan_range_40_2=((40/100)*annual_income)
    loan_range_80=((80/100)*annual_income)
    print("you are eligible for getting loan range from",loan_range40_2,loan_range_80)
elif(CIBIL_score>650 and (annual_income>800000 and annual_income<=1500000)):
    loan_range_40_3=((40/100)*annual_income)
    loan_range_80_1=((80/100)*annual_income)
    print("you are eligible for getting loan range from",loan_range_40_3,loan_range_80_1)
elif(annual_income>1500000)and(CIBIL_score>=300 and CIBIL_score<=650):
    loan_range_40_4=((40/100)*annual_income)
    loan_range70_1=((70/100)*annual_income)
    print("you are eligible for getting loan range from",loan_range_40_4,loan_range70_1)
elif(CIBIL_score>650)and(annual_income>1500000)and(age>=46 and age<=58):
    loan_range_40_5=((40/100)*annual_income)
    loan_range70_2=((70/100)*annual_income)
    print("you are eligible for getting loan range from",loan_range_40_5,loan_range70_2)
else:
    exit()
    





