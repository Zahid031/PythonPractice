class MyComplexNumber:
    def __init__(self,real=0,img=0):
        print("My complex constructor executing..")
        self.real_part=real
        self.img_part=img

    def displayComplex(self):
            print("{0}+{1}j".format(self.real_part,self.img_part))

cmplx1=MyComplexNumber(40,50)
cmplx1.displayComplex()