#!/usr/binp/python3

def do(inp,spacingFlag =" "):
	liH=[]
	inp += spacingFlag
	while inp != "":
		temp,x,i = "","",0
		while x!=spacingFlag:
			temp += inp[i]
			x = inp[i+1]
			i+=1
		liH.append(temp)
		inp = inp[len(temp)+1:]
	return liH

def optimized(inp,flag=" ",conversor=False):
	li = [""]
	count = 0
	for x in inp :
		if x!=flag :
			li[count]+=x
		else :
			count+=1
			li.append("")
	if conversor :
		return [int(x) for x in li if x!='']
	return [x for x in li if x!='']
