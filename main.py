# --------------------------------------------------
# NAME: Adewumi Nasirudeen Adeyinka
# DEPARTMENT: Computer Science
# APPLICATION NUMBER: PG202452612787
# COURSE: CSC 803/ CSC 825
# TOPIC: Demonstrating the Four Features of OOP in Python
# DATE: 01/11/2025


from abc import ABC, abstractmethod  # Used for abstraction


# --------------------------------------------------
# BASE CLASS: PERSON (Abstraction)
# --------------------------------------------------
class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def show_details(self):
        """Abstract method to be defined by subclasses"""
        pass


# --------------------------------------------------
# CHILD CLASS 1: STUDENT (Inheritance + Encapsulation + Polymorphism)
# --------------------------------------------------
class Student(Person):
    def __init__(self, name, age, student_id, scores):
        super().__init__(name, age)
        self.student_id = student_id
        self.__scores = scores  # Encapsulation (private attribute)

    def set_scores(self, scores):
        """Allows safe update of scores"""
        if 0 <= scores <= 100:
            self.__scores = scores
        else:
            print("❌ Invalid score! Must be between 0 and 100.")

    def get_scores(self):
        """Public method to access private score"""
        return self.__scores

    def show_details(self):
        """Polymorphism: same method name, different behavior"""
        print(f"\n📘 STUDENT DETAILS:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Student ID: {self.student_id}")
        print(f"Score: {self.__scores}")


# --------------------------------------------------
# CHILD CLASS 2: TEACHER (Inheritance + Polymorphism)
# --------------------------------------------------
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def show_details(self):
        """Polymorphism again"""
        print(f"\n📗 TEACHER DETAILS:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Subject: {self.subject}")


# --------------------------------------------------
# MAIN PROGRAM (INTERACTIVE PART)
# --------------------------------------------------
def main():
    print("\n=======================================")
    print("     SIMPLE SCHOOL MANAGEMENT SYSTEM   ")
    print("=======================================\n")

    print("Choose who you want to register:")
    print("1. Student")
    print("2. Teacher")

    choice = input("Enter 1 or 2: ")

    if choice == "1":
        name = input("\nEnter student name: ")
        age = int(input("Enter age: "))
        student_id = input("Enter student ID: ")
        scores = float(input("Enter student score (0-100): "))

        student = Student(name, age, student_id, scores)
        print("\n✅ Student registered successfully!")
        student.show_details()

    elif choice == "2":
        name = input("\nEnter teacher name: ")
        age = int(input("Enter age: "))
        subject = input("Enter subject taught: ")

        teacher = Teacher(name, age, subject)
        print("\n✅ Teacher registered successfully!")
        teacher.show_details()

    else:
        print("Invalid choice! Please restart program.")

    print("\n=== THANK YOU FOR USING THE SYSTEM ===\n")


# --------------------------------------------------
# RUN THE PROGRAM
# --------------------------------------------------
if __name__ == "__main__":
    main()
