payment =int(input("how much you pay? "))
membership = input("are you join or stor? (y/n)")
discount =input("do you have discount? (y/n)")


if payment >1000000 or (membership and discount):
    amountpayable = payment/2
    print(f"""Amounpayable: {amountpayable}""")
else:
    print ("shoping done")