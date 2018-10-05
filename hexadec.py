#!/bin/python3
# -*- coding : utf-8 -*-

__credits__ = "Tersinet thibault"


class Number():
	"""docstring for Number"""
	def __init__(self, ref):
		self.ref = ref
		self.duplicata = None
		self.indx = {"numbers":('0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'),"letters":('0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f')}
		self.state = "dec" if type(ref)==int else "hex" 
	

	def reverse(self):
		a=self.duplicata
		b=self.ref
		self.ref = a
		self.duplicata = b
		self.state = 'dec' if self.state == "hex" else 'hex'

	def hexaToDec(self):
		a=self.ref
		b=0
		for i in range(0,len(a)):
			b=16*b+int(self.indx["numbers"][self.indx["letters"].index(a[i])])
		self.duplicata= b
	

	def decToHexa(self):
		
		self.duplicata = ""
		a = self.ref
		while a != 0:
			b = a%16
			b=self.indx["letters"][self.indx["numbers"].index(str(b))]

			a = int (a / 16)
			self.duplicata+=b
		self.duplicata = ''.join(reversed(self.duplicata))

	def __add__(self, other):
		if self.state=="dec" and other.state=="dec" :
			return self.ref+other.ref
		elif self.state != other.state :
			for x in (self,other):
				if x.state != 'dec' :
					x.hexaToDec()
					x.reverse()
					a = self+other
					x.reverse()
					return a
		else :
			for x in (self, other):
				x.hexaToDec()
				x.reverse()
			a = self+other
			self.reverse(),other.reverse()
			return a

	def __sub__(self, other):
		if self.state=="dec" and other.state=="dec" :
			return self.ref-other.ref
		elif self.state != other.state :
			for x in (self,other):
				if x.state != 'dec' :
					x.hexaToDec()
					x.reverse()
					a = self-other
					x.reverse()
					return a
		else :
			for x in (self, other):
				x.hexaToDec()
				x.reverse()
			a = self-other
			self.reverse(),other.reverse()	
			return a

	def __repr__(self):
		if self.duplicata == None:
			return str(self.ref)
		return str(self.ref)+"="+str(self.duplicata)

"""
#dec
test_1, test_3 = Number(645),Number(6544)

test_3.decToHexa()

test_4 = Number(42)

#hex
test_2 = Number('2a')
test_5 = Number('545e')

test_2.hexaToDec()

#disp
print(str(test_3.duplicata)+"\n"+str(test_2.duplicata)+'\n')
print(test_2-test_5)

"""