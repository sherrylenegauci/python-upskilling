import math

firstname = input("Enter your first name: ")
lastname = input("Enter your last name: ")
print(f"Hello {firstname} {lastname}! Welcome to Python Upskilling")
email = input("Enter your school email (@ilearn.edu.mt): ")
print(f"Your email is {email}")

username:str = input("Enter your username: ")
steps:int = int(input("Enter the number of steps you have walked today: "))
distance_km:float = float(input("Enter the distance you have walked today (km): "))
goal_achieved:bool = input("Have you achieved your daily goal? (yes/no): ").strip().lower() == "yes"

print ("---------Fitness Summary--------------")
print(f"Name: {firstname} {lastname}")
print(f"Email: {email}")
print(f"Steps: {steps}")
print(f"Distance (km): {distance_km}")
print(f"Goal Achieved: {goal_achieved}")
print ("--------------------------------------")

radius:float = float(input("Enter the radius of the track (m): "))
circumference:float = 2 * math.pi * radius #converts from int to float
print(f"The circumference of the track is {round(circumference, 2)} m")