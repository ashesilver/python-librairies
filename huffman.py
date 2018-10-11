#!/bin/usr/python3.7




def ocuCount(st):
	dico = {}

	for x in st:
		try:
			dico[x]+=1
		except:
			dico[x]=1

	return(dico)



def makeATree(dico={'a':1,'b':2}):





