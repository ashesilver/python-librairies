#!/usr/bin/python3

def do(spacingFlag =" "):
	liH=[]
	labonnebonnestring += " "
	while labonnebonnestring != "":
		temp,x,i = "","",0
		while x!=spacingFlag:
			temp += labonnebonnestring[i]
			x = labonnebonnestring[i+1]
			i+=1
		liH.append(temp)
		labonnebonnestring = labonnebonnestring[len(temp)+1:]
	return liH
