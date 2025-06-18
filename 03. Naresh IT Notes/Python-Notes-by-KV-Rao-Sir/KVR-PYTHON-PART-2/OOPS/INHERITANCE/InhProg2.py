#InhProg2.py
class C1:
    def disp1(self):
        print("C1--disp1()")
class C2(C1):
    def disp2(self):
        print("C2--disp2()")
#Main Program
o2=C2()
o2.disp1()
o2.disp2()