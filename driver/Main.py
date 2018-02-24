'''
Created on 25-Feb-2018

@author: palashsarkar
'''
from datahandling import RabinKarp as rab

sent=input("Enter base string: ")
strtomch=input("Enter string to be matched: ")

sent.strip()
strtomch.strip()

rab.RabinKarpMatcher(sent,strtomch)



