class base:
      def __init__(self):
          print("This is base class")
class child1(base):
      def __init__(self):
          super().__init__()
          print("This is child 1 class")
class child2(child1):
      def __init__(self):
          super().__init__()
          print("This is child 2 class")
obj=child2()

