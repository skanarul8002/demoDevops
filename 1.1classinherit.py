import math
class Circle:
      def area(self,r):
          self.r=r
          return 3.14*pow(self.r,2)
      def circumfer(self):
          return 2*3.14*self.r
class Cylinder(Circle):
      def cyarea(self,h):
          self.h=h
          return 2*3.14*self.r*(self.r+self.h)
      def volume(self):
          return 3.14*self.r*self.r*self.h
obj=Cylinder()
circle_area=obj.area(int(input("Enter The Radius of Circle:")))
circl_circum=obj.circumfer()
cylinder_surface=obj.cyarea(int(input("Enter the Hieght of Cylinder:")))
cylinder_vol=obj.volume()
print("Area of Circle is ",circle_area)
print("Circumference of Circle is ",circl_circum)
print("Surface area of Cylinder ",cylinder_surface)
print("Volume of Cylinder is ",cylinder_vol)

# class Circle:
#        def __init__(self,r):
#           self.r=r
#        def cir_area(self):
#            print(f"Area of Circle is {3.14*math.pow(self.r, 2)}")
#        def circl_circum(self):
#            print(f"Circumference of circle is {2*3.14*self.r}")
# class Cylinder(Circle):
#        def __init__(self,r,h):
#           super().__init__(r)
#           self.h=h
#        def surface_area(self):
#            print(f"Surface Area of Cylinder is {2*3.14*self.r*(self.r+self.h)}")
#        def volume(self):
#            print(f"Volume of cylinder is {3.14*self.r*self.r*self.h}")
# obj=Cylinder(1,1)
# obj.cir_area()
# obj.circl_circum()
# obj.surface_area()
# obj.volume()
