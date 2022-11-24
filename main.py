import random
print("Name =")

name=["Anand Sharma","Ankit Chaturvedi","Jitendra Singh","Dhiraj Thakare",
      "Rajesh Saini","Aakash Saxena","Ravi Maurya","Sejal Khurana",
      "Ganesh Kumawat", "Ashish Mundra","Dhairya Saraswat","Bhawana Gupta",
      "Chanchal Sharma","Rahul Singh","Vikash Tailor","Ainul Huda"]

random_person=random.sample(name,k=4)
print("Team 1 =")
print(random_person)
name = [i for i in name if i not in random_person]
random_person1=random.sample(name,k=4)
print("Team 2 =")
print(random_person1)
name = [i for i in name if i not in random_person1]
random_person2=random.sample(name,k=4)
print("Team 3 =")
print(random_person2)
name = [i for i in name if i not in random_person2]
random_person3=random.sample(name,k=4)
print("Team 4 =")
print(random_person3)
print("Thank you")

