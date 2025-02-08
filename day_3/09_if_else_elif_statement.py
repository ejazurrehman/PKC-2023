
age = input("what is your child's age?")
age = int(age)
scholl_entry_requirement = 5
if age==scholl_entry_requirement:
    print("Congratulation! your child is eligible for admission")
elif age > scholl_entry_requirement:
    print("your child is over age, not eligible for admission. Please check other options.")
else:
    print("your child is under age, not eligible for admission. Take Care of Him/Her.")


