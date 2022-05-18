class A:
    def feature1(self):
        print('Feature 1 is working')

    def feature2(self):
        print('Feature 2 is working')

class B(A):
    def feature3(self):
        print('Feature 3 is working')

    def feature4(self):
        print('Feature 4 is working')


class C(A,B):
    def feature5(self):
        print('Feature 5 is working')

    def feature6(self):
        print('Feature 5 is working')


a1 = A()
a1.feature1()               #Grand-Parent Class
a1.feature2()       


b1 = B()
b1.feature1()
b1.feature2()               #Parent Class
b1.feature3()
b1.feature4()


c1 = C()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()               #Child Class/Multiple
c1.feature5()
c1.feature6()





"""
This program is an example of inheritance,
the class names should be professional
but i used simple alphabets for making an easy template
and to facilitate myself in future with this concept 

"""
