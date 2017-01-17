class AnimalShelter(object):
	def __init__(self):
		# do some intialize if necessary
		self.cat = []
		self.dog = []
		self.time = 0

	def enqueue(self, name, type):
		# Write yout code here
		self.time += 1
		if type == 0:
			self.cat.append((name, self.time))
		else:
			self.dog.append((name, self.time))

	# return name as string 
	def dequeueAny(self):
		# Write your code here
		if len(self.cat) == 0:
			return self.dequeueDog()
		elif len(self.dog) == 0:
			return self.dequeueCat()
		else:
			if self.cat[0][1] < self.dog[0][1]:
				self.dequeueCat()
			else:
				self.dequeueDog()

	# return name as string
	def dequeueDog(self):
		# Write your code here
		result = self.dog[0][0]
		del self.dog[0]
		return result

	# return a string
	def dequeueCat(self):
		# Write your code here
		result = self.cat[0][0]
		del self.cat[0]
		return result
