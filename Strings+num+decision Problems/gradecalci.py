#create a pgm takes the marks of a student in diff sub as input.Calculate totao marks and avg, the display correspinding grade based on avg.
#Input: mks in math: 85, mks in sci: 90, mks in eng: 78.
#Output: total mks: 253, avg mks: 84.33, grade:A.

m = int(input("Marks in Maths: "))
s = int(input("Marks in Science: "))
e = int(input("Marks in English: "))

total_marks = m+s+e
average_marks = total_marks/3

percentage = (total_marks/300)*100
grade = ""

if percentage > 90:
    grade = "A"
elif percentage > 80 and percentage <= 90:
    grade = "B"
elif percentage > 70 and percentage <= 80:
    grade = "C"
else:
    grade = "P"
print(f"Total marks: {total_marks} \nAverage marks: {average_marks} \nGrade: {grade}")