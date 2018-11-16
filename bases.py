#!/bin/python3
# -*- coding : utf-8 -*-

__credits__ = "Tersinet thibault"


class Number():
	"""class for your numbers"""
	def __init__(self, ref, state=10):
		self.ref = ref
		self.duplicata = None
		self.indx = {"numbers":('0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35'),"letters":('0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')}
		self.state = state
	

	def reverse(self):
		a=self.duplicata
		b=self.ref
		self.ref = a
		self.duplicata = b


	def dec(self):
		a=self.ref
		b=0
		for i in range(0,len(a)):
			b=self.state*b+int(self.indx["numbers"][self.indx["letters"].index(a[i])])
		self.duplicata= b
		self.state = 10
	

	def base(self, base):
		
		self.duplicata = ""
		a = self.ref
		while a != 0:
			b = a%base
			b=self.indx["letters"][self.indx["numbers"].index(str(b))]

			a = int (a / base)
			self.duplicata+=b
		self.duplicata = ''.join(reversed(self.duplicata))
		self.state = base
	

	def __add__(self, other):
		if self.state==other.state and self.state == 10 :
			return self.ref+other.ref
		else :
			for x in (self, other):
				if not x.state == 10 :
					x.dec()
					x.reverse()
			a = self+other
			for x in (self, other):
				if not x.state == 10 :
					x.reverse()
			return a

	def __sub__(self, other):
		if self.state==other.state and self.state == 10 :
			return self.ref-other.ref
		else :
			for x in (self, other):
				if not x.state == 10 :
					x.dec()
					x.reverse()
			a = self-other
			for x in (self, other):
				if not x.state == 10 :
					x.reverse()
			return a

	def __repr__(self):
		if self.duplicata == None:
			return str(self.ref)
		return str(self.ref)+" = "+str(self.duplicata)
