#!/usr/bin/python3

def do(labonnebonnestring, liH=[]):
	while labonnebonnestring != "":
		temp,x,i = "","",0
		while x!=" ":
			temp += labonnebonnestring[i]
			x = labonnebonnestring[i+1]
			i+=1
		liH.append(temp)
		labonnebonnestring = labonnebonnestring[len(temp)+1:]
	return liH

