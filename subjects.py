print("Enter Marks Obtained 4 subjects: ")
english = int(input("english :"))
hindi = int(input("hindi :"))
maths = int(input("maths :"))
science = int(input("science :"))
sum = english + hindi + maths + science
print("Total Marks:", sum)
perc = (sum/400)*100
print(end = "Percentage: ")
print(perc)