#parking estimation based on user input

#ask how long user will park

#user enters amount of time in hours
hours=(float(input("How long do you wish to park? ")))

#add accpetable range in numbers only

#calculate cost at rate of $2.00 per hour
estimated_cost = float(hours) * 2.00

#output of cost
print(estimated_cost)

