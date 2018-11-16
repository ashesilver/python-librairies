#!/bin/usr/python3.7
# -*- coding:utf-8 -*-

def helper():
	pass

class Code(object):
	def __init__(self, tag):
		self.tag = tag
		self.index = {".":"print()",",":"input()","+":"+=1","-":"-=1","[":"ouvrir boucle","]":"fermer boucle",">":"case droite","<":"case gauche"}
		self.list = [0]
		self.indic = 0
		self.loop_count = 0

	def __repr__(self):
		return self.exec()

	def modify(self, other):
		print("old =", self.tag, self)
		print("new = ",other.tag, other)
		ans = input("conserve changes ? (True/False)")
		if ans:
			self.tag = other.tag

	def next_input(self, ascii_value):
		self.inp = ascii_value

	def exec(self):
		output = ""
		for x in range(len(self.tag)):
			y = self.index[self.tag[x]]
			if y == "print()":
				output+=chr(self.list[self.indic])
			elif y == "input()":
				try :
					self.list[self.indic] = ord(self.inp[0])
				except :
					pass
				finally :
					self.inp = self.inp[1:]
			elif y == "case droite":
				self.indic += 1
				try:
					tmp = self.list[self.indic] + 1
				except:
					self.list.append(0)
				else:
					tmp = None
			elif y == "case gauche":
				if self.indic < 1:
					pass
				else :
					self.indic -= 1
			elif y == "+=1":
				self.list[self.indic] += 1
			elif y == "-=1":
				if self.list[self.indic] < 1 :
					pass
				else :
					self.list[self.indic] -= 1
			elif y == "ouvrir boucle":
				save_tag = self.tag

				for i in range(x,len(self.tag)-1):
					if self.index[self.tag[i]] == "ouvrir boucle" :
						self.loop_count += 1
					elif self.index[self.tag[i]] == "fermer boucle" :
						self.loop_count -= 1
					if self.loop_count<1:
						self.tag = self.tag[x+1:i]
						len_boucle = len(self.tag)
						break

				while self.list[self.indic] > 1 :
					output+=self.exec()
				self.tag = save_tag
				x+=len_boucle
		return output


