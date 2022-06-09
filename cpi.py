def compoundRecursion(principal, compounded, duration, rate, numberOfRecursions):
    if numberOfRecursions == 0:
        totalDuration = compounded * duration
    elif numberOfRecursions != 0:
        totalDuration = duration
    if duration == 0:
        return principal
    else:
        newDuration = totalDuration - 1
        amount = principal*(1+(rate/compounded))
        return compoundRecursion(amount, compounded, newDuration, rate, 1)
   
x=int(input("Enter the principle amount"))
y=int(input("Enter the no.of times compounded per year"))
z=int(input("Ente the time period in years"))
j=float(input("Enter the interest rate"))
k=int(input("Enter the number of recursions "))

print (compoundRecursion(x, y, z, j, 0))
