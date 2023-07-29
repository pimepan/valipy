from valipy import Valipy
class Foo:
	x:str = 'hello world'
	y:int = 25

x = Foo()
y = Valipy(x).isInstance(Foo).validate() # true

print(y)
print(len(Valipy.__dict__))