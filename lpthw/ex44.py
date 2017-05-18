'''class Parent(object):

	def implicit(self):
		print("Parent implicit")


class Child(Parent):
	pass

dad = Parent()
child = Child()


dad.implicit()
child.implicit()

###########

class Parent(object):

	def override(self):
		print("Parent override()")


class Child(Parent):
	def override(self):
		print("Child override()")

dad = Parent()
child = Child()


dad.override()
child.override()

############

class Parent(object):
	def altered(self):
		print("Parent altered()")


class Child(Parent):
	def altered(self):
		print("Child, before Parent altered()")
		super(Child, self).altered()
		print("Child, after Parent altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()
'''
#############

class Parent(object):
	def override(self):
		print("Parent override()")

	def implicit(self):
		print("Parent implicit()")

	def altered(self):
		print("Parent altered()")

class Child(Parent):
	def override(self):
		print("Child override")

	def altered(self):
		print("Child, before parent altered()")	
		super(Child, self).altered()
		print("Child, after parent altered()")


dad = Parent()
child = Child()

dad.implicit()
child.implicit()

dad.override()
child.override()

dad.altered()
child.altered()

