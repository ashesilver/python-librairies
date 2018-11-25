#!/bin/usr/python3
# -*- coding : utf-8 -*-


def cond(a,b,c):
	return b if a else c

def liVide():
	return []

def estVide(a):
	return True if a==[] else False

def tete(a):
	return a[1:]

def queue(a):
	return a[0]

def cons(a,b):
	return b.insert(0,a)

