# --------------
class_1 = ["Geoffrey Hinton", "Andrew Ng", "Sebastian Raschka", "Yoshua Bengio"]
class_2 = ["Hilary Mason", "Carla Gentry", "Corinna Cortes"]
new_class = class_1 + class_2
print(new_class)
new_class.append("Peter Warden")
print(new_class)
new_class.remove("Carla Gentry")
print(new_class)
courses = {"Math" : 65, "English" : 70, "History" : 80, "French" : 70, "Science" : 60}
total = 0
for i in courses:
    total += courses[i]
print(total)
percentage = total / len(courses)
print(percentage)
mathematics = {"Geoffrey Hinton" : 78, "Andrew Ng" : 95, "Sebastian Raschka" : 65, "Yoshua Benjio" : 50, "Hilary Manson" :70, "Corinna Cortes" : 66, "Peter Warden" : 75}
topper = min(mathematics)
print(topper) 
topper = topper.split() 
first_name = topper[0] 
last_name = topper[1]
full_name = last_name + " " + first_name
print(full_name)
certificate_name = full_name.upper()
print(certificate_name)




