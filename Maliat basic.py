info_or_salary = input("\nenter I or i for your info or enter S or s for your salary count:") 
 
if (info_or_salary == "I" or info_or_salary == "i"): 
    print("\n\t---------this is a info card---------") 
    name = input("\t   please enter your first name:") 
    family = input("\t   please enter your last name:") 
    heigh = int(input("\t   please enter your heigh in cm:")) 
    age = int(input("\t   how old are you?")) 
    print("\t-------------------------------------") 
 
    print(f""" 
            <--------------------------> 
                 hello {name} {family} 
                 you are {heigh}cm tall 
                 and {age} years old 
            <--------------------------> 
            """) 
 
     
elif(info_or_salary == "S" or info_or_salary == "s"): 
    print("\n-------this is a salary managment system-------") 
    salary = int(input("\n\tplease enter your salary: ")) 
    print("\n-----------------------------------------------") 
    insurance = salary * 0.93 
    tax = insurance * 0.91 
 
    print(f""" 
<-----------------------------------------------------------> 
        your income before insurance {salary} 
        your income after insurance {insurance} 
        your income after insurance and tax {tax} 
<-----------------------------------------------------------> 
                """) 
 
 
else: 
    print("error you have entered a wrong option")