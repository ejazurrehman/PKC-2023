# print("I am learning python")
# print("I am learning python")
# print("I am learning python")

# # define a function
# # 01

# def print_haider():
#     print("I am learning python")
#     print("I am learning python")
#     print("I am learning python")

# print_haider()

# # 02
# def print_ejaz():
#     text = "I am learning python with Dr. Ammar"
#     print(text)
#     print(text)
#     print(text)

# print_ejaz()

# # # 03
# def print_ejaz(text):
#     print(text)
#     print(text)
#     print(text)

# print_ejaz("I am learning python with Dr. Ammar")

# # defining a function with logical operators

# # this calculator will add two numbers and return the result, either child study in school or college

# def school_age_calculator(): 
#     name = input("Enter your name: ")
#     age = int(input("Enter your age: "))
#     if age >= 5 and age <= 18:
#         print(f"{name} you are in school")
#     else:
#         print(f"{name} you are not in school")
# school_age_calculator()

# this calculator will add two numbers and return the result, either child study in school or college or not in any one

def school_calculator():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    if age >= 5 and age <= 18:
        print(f"{name} you are in school")
    elif age >= 19 and age <= 25:
        print(f"{name} you are in college")
    else:
        print(f"{name} you are not in school or college")

school_calculator()

# defining a fuciton with mathematical operators

# define a future age funciton

# this funciton will ask for your current age and return your age after x number of years
# def future_age_calculator():
#     name = input("Enter your name: ")
#     current_age = int(input("Enter your current age: "))
#     years = int(input("Enter the number of years: "))
#     future_age = current_age + years
#     print(f"Your future age will be {future_age}")

# future_age_calculator()  # calling the function




