from new_student import Student


student = Student(name="Edward", surname="agle")
print(student)

try:
    student = Student(name="Edward", surname="agle", id="toto")
    print(student)
except TypeError as e:
    print("TypeError:", e)

try:
    student = Student(name="Edward", surname="agle", login="Edagle")
    print(student)
except TypeError as e:
    print("TypeError:", e)
