salary = int(input("enter your monthly salary: "))
child = input("do you have children? (y/n)")

if salary <= 10000000:
    tax=0
elif salary <= 25000000:
    tax = (salary - 10000000) * 0.10
else:
    tax = 1500000 + (salary - 25000000) * 0.20
    
if child == "y":
    tax = max(0, tax - 500000)

    
print(f"salary:, {salary} ")
print(f"has child: {child} ")
print(f"""final tax:, {int(tax)}""" )