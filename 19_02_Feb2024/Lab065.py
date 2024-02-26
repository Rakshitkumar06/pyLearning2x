class Student():
    name = None
    mobile_no = None


    def Watch_recordings(self):
        print("Watch recordings")

    def do_assignments(self): 
        print("Do assignments")

    def do_coding_ass(self):
        print("Do coding assignments")

S1 = Student()
S1.name = "Dhoni"
print(S1.name)
S1.mobile_no = "1234567890"
print(S1.mobile_no)
S1.do_assignments()
S1.Watch_recordings()
S1.do_coding_ass()

S2 = Student()
S2.name = "Kohil"
print(S2.name)
S2.mobile_no ="1234679099"
print(S2.mobile_no)
S2.do_assignments()


class Course():
    course_name = None
    course_no = None

    def type_of_course(self):
        print("Testing course")

    def type_of_language(self):
        print("Language name is python")

C = Course()
C.course_name = "0X python Automation"
print(C.course_name)
C.course_no = 1245
print(C.course_no)
C.type_of_course()
C.type_of_language()

C2 = Course()
C2.course_name = "1X python Automation"
print(C2.course_name)
C2.course_no = 1029
print(C2.course_no)

class Payments():
    payment_type = None
    payment_no = None

    def type_of_payments(self):
        print("Razor payment")

    def type_of_payment_mode(self):
        print("Card payment")

P = Payments()
P.payment_type = "Online UPI payment"
print(P.payment_type)
P.payment_no = 1728
print(P.payment_no)
P.type_of_payments()
P.type_of_payment_mode()