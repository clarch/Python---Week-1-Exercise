# #We have a class defined for vehicles. Create two new vehicles called car1 and car2. Set car1 to be a red convertible worth $60,000 with a name of Fer, and car2 to be a blue van named Jump worth $10,000.
# # define the Vehicle class
# class Vehicle:
#     name = ""
#     kind = "car"
#     color = ""
#     value = 100.00
#     def description(self):
#         desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
#         return desc_str
# # your code goes here
# car1 = Vehicle()
# car1.color = "red"
# car1.name = "Fer"
# car1.kind = "Convertible"
# car1.value = 60000

# car2 = Vehicle()
# car2.color = "blue"
# car2.name = "Jump"
# car2.kind = "van"
# car2.value = 10000

# # test code
# print car1.description()
# print car2.description()





# #Add "Jake" to the phonebook with the phone number 938273443, and remove Jill from the phonebook.
# phonebook = {
#     "John" : 938477566,
#     "Jack" : 938377264,
#     "Jill" : 947662781
# }

# # write your code here
# del phonebook["Jill"]
# phonebook["Jake"] = 938273443

# # testing code
# if "Jake" in phonebook:
#     print "Jake is listed in the phonebook."
# if "Jill" not in phonebook:
#     print "Jill is not listed in the phonebook."


# #3
# #In this exercise, you will need to print an alphabetically sorted list of all functions in the re module, which contain the word find.
# import re

# # Your code goes here