# Implicit Inheritance
class Parent(object):

	def Implicit(self):
		print "Parent Implicit()"

class Child(Parent):
	pass

dad = Parent()
son = Child()

dad.Implicit()
son.Implicit()

# Override Explicitly

class Parent(object):

	def override(self):
		print "Parent override()"

class Child(Parent):

	def override(self):
		print "CHILD override()"

dad = Parent()
son = Child()

dad.override()
son.override()
	
#Alter before or after

class Parent(object):

	def altered(self):
		print "PARENT altered()"

class Child(Parent):

	def altered(self):
		print "CHILD, before parent altered()"
		super(Child, self).altered()
		print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.altered()
son.altered()

#all 3 cases

class Parent(object):

	def override(self):
		print "PARENT override()"

	def implicit(self):
		print "PARENT implicit()"

	def altered(self):
		print "PARENT altered()"

class Child(Parent):

	def override(self):
		print "CHILD override()"

	def altered(self):
		print "CHILD, BEfore PARENT altered()"
		super(Child, self).altered()
		print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()




