# while & for loops

# while loop
x=0
while (x<5):
    print(x)
    x=x+1

x=0
while(x <= 5):
    print(x)
    x=x+1

# for loop

for x in range(4,10):
    print(x)

# develop array
# this is an array of numbers from Mon to Sun

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for i in (days): # loop through array
    print(i)

# this is an array of days with break function

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for i in (days):
    if (i=="Fri"):break # break the loop when i is equal to Fri
    print(i)

# this is an array of days with continue function

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for i in (days):
    if (i=="Fri"):continue # skip the Fri and continue with the next day
    print(i)
