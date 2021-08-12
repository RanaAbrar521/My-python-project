
#=============================== Q1 ============================================

patients =  [[70,1.8],[80,1.9],[150,1.7]]

def calculate_bmi (weight, height):
    return weight/(height ** 2)

for patient in patients:
    weight, height = patient

    bmi = calculate_bmi(height,weight)
    print("Patient's BMI is :%f"  %bmi)

#=============================== Q2 ============================================
greeting = input("Hello, possible pirate! What's the password? ")
if greeting == "Arrr!":
    print("Go Away, Pirate.")
else:
    print("Greetings, hater of the pirates!")

#=============================== Q3 ============================================

authors = {
    "Charles Dickens": "1870",
    "William Thackeray": "1863",
    "Anthony Trollope": "1882",
    "Gerard Manley Hopkins": "1889"}

for author_date in authors.keys():
    print ("%s" % author_date + " died in " + "%d." % int (authors[author_date]))


#=============================== Q4 ============================================

year = int(input("Greetings! What is your year of origin? "))

if year <= 1900:
    print ("Woah, that's the past!")
elif year > 1900 and year < 2020:
    print ("That's totally the present!")
else:
    print ("Far out, that's the future!!")


#=============================== Q5 ============================================

class classy_Person:
    def __init__(self, first_name, last_name):
        self.first = first_name
        self.last = last_name

    def speak(self):
        print("My name is "+  self.first + " " + self.last)

me = classy_Person("Brandon", "Walsh")
you = classy_Person("Ethan", "Reed")
me.speak()
you.speak()


#=============================== Q6 ============================================

exam_one = int (input("Input exam grade one: "))
exam_two = int (input("Input exam grade two: "))
exam_three = int (input("Input exam grade three: "))
grades = [exam_one, exam_two, exam_three]
sum = 0

for grade in grades:
    sum = sum + grade

avg = sum / len(grades)

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90:
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C"
elif avg <= 69 and avg >= 65:
    letter_grade = "D"
else:
    letter_grade = "F"

count = 1
for grade in grades:
    print("Exam " +str(count) + " : "+ str(grade))
    count += 1

print("Average: " + str(avg))
print("Grade: " + letter_grade)

if letter_grade == "F":
    print ("Student is failing.")
else:
    print ("Student is passing.")




