units=int(input('please enter the number of units you havev consumed:'))

if(units < 50):
    amount=units *4.80
    surchrage=31
elif(units<=100):
    amount = 160 ((units-50)*3.25)
    surchrage=41
elif(units<=200):
    amount = 130 + ((units-50)*3.25)
    surchrage=41
else:
    amount = 160+ ((units-50)*3.25)
    surchrage=41
total= amount+surchrage
print("Electricity bill= %.2f" %total)