import math
class Rectangle:
      def area(self,l,b):
          self.l=l
          self.b=b
          return self.l*self.b
      def perimeter(self):
          return 2*(self.l+self.b)
class Cuboid(Rectangle):
      def surface(self,h):
          self.h=h
          return 2*(self.l+self.b+self.h)
      def volume(self):
          return self.l*self.b*self.h
obj=Cuboid()
rec_area=obj.area(6,4)
rec_perimeter=obj.perimeter()
cuboid_sur=obj.surface(9)
cuboid_vol=obj.volume()
print("Area of Rectangle is ",rec_area)
print("Perimeter of Rectangle is ",rec_perimeter)
print("Surface area of Cuboid is ",cuboid_sur)
print("Volume of Cuboid is ",cuboid_vol)