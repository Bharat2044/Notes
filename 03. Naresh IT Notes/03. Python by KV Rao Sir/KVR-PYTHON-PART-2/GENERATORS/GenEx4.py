#GenEx4.py
def getcourses():
	yield "PYTHON"
	yield "HTML"
	yield "Java"
	yield "C"

#main Program
k=getcourses() # Here k is an object of type <class, 'generator'>
print(next(k))
print(next(k))
print(next(k))
print(next(k))
