class Stud:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def grade_calculate(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 80:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "F"


# ======= main function =========
name = input("Enter your name : ")
marks = int(input("Enter your marks : "))   # FIXED

std = Stud(name, marks)
grd = std.grade_calculate()

print(f"Student : {std.name}, Grade : {grd}")   # FIXED

# save to file...
with open("grade.txt", "a") as f:
    f.write(f"{std.name} - {grd}\n")   # FIXED

print("Data saved to grade.txt")