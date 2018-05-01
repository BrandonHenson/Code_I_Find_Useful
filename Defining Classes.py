v1 = input("What's the first value? ")
v2 = input("What's the second value? ")



class MyNewClass(object):
	def AddValues(v1,v2):
		 return int(v1) + int(v2)
	def SubtractValues(v1,v2):
		 return int(v1) - int(v2)
		
	def MultiplyValues(v1,v2):
		 return int(v1) * int(v2)
		
	def DivideValues(v1,v2):
		 return int(v1) / int(v2)
		 
		 
		 
		 
		 
AddAnswer = MyNewClass.AddValues(v1,v2)
print("The answer to the question " + str(v1)+ '+'+ str(v2) + " is " + str(AddAnswer))


MinusAnswer = MyNewClass.SubtractValues(v1,v2)
print("The answer to the question " + str(v1)+ '-'+ str(v2) + " is " + str(MinusAnswer))

MultiplyAnswer = MyNewClass.MultiplyValues(v1,v2)
print("The answer to the question " + str(v1)+ '*'+ str(v2) + " is " + str(MultiplyAnswer))


DivideAnswer = MyNewClass.DivideValues(v1,v2)
print("The answer to the question " + str(v1)+ '/'+ str(v2) + " is " + str(DivideAnswer))
