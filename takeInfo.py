#!/usr/bin/python3

def do(labonnebonnestring):
	labonnebonnestring+=" "
	liH=[]
	while labonnebonnestring != "":
		i=0
		temp = ""
		x=""
		while x!=" ":
			temp += labonnebonnestring[i]
			x = labonnebonnestring[i+1]
			i+=1

		liH.append(temp)
		labonnebonnestring = labonnebonnestring[len(temp)+1:]
	return liH

