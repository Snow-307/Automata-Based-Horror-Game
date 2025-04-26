# -*- coding: utf-8 -*-
"""
Created on Thu May  9 22:39:20 2024

@author: sneha_xqbh6g1
"""
import random
import sys

#game setup

 
#randomly generate key locations
l1 =[1,2,3,4,5,6]
key1=2
l1.remove(key1)
key2=random.choice(l1)
l1.remove(key2)
key3=random.choice(l1)

#display what is present in room
def check_room(room):
    print("Contents of room:")
    if(doll1==room or doll2==room or doll3==room):
        print("Doll")
    if(key1==room or key1==room or key1==room):
        print("Key")
        
def collect_items(room,dollcount,keycount):
    if(doll1==room or doll2==room or doll3==room):
        dollcount=dollcount+1 
    if(key1==room or key1==room or key1==room):
        keycount=keycount+1 
        
    return keycount,dollcount

def ghost_location():
    l3 =[1,2,3,4,5,6]
    ghostloc=random.choice(l3)
    return ghostloc
          
def game_over():
    print("\nYou had no dolls left to save you, and have been killed by the ghost. Skill issue tbh. Game over")
    sys.exit(0)
    
def ghost_attack(dollcount,Ghost):
    if(dollcount>0):
        print("\nYou offer your doll to the ghost to pacify it!")
        dollcount=dollcount-1
        print("Your current doll count is:", dollcount)
        Ghost ="Passive"
        return dollcount,Ghost
    else:
        game_over()

def collect_items(room,keycount,dollcount):
    response1=input("\nCollect items? Y or N\n ")
    if(response1=='Y'):
        if(doll1==room or doll2==room or doll3==room):
            dollcount=dollcount+1
        if(key1==room or key1==room or key1==room):
            keycount=keycount+1
        
        print("\nNumber of keys in Inventory:", keycount,  "\nNumber of dolls in Inventory:", dollcount)
        return keycount,dollcount
    else:
        return keycount,dollcount
    
    
def ghost_active(Ghost,room,keycount,dollcount):
    while (Ghost=="Active"):
        ghostloc = ghost_location()
        if (room==ghostloc):
            print("\nGhost is in this room!")
            dollcount,Ghost=ghost_attack(dollcount,Ghost)
            check_room(room)
            return room
        
        else:
            print("\n\nGhost is not in your room. You got lucky, but beware she could be in any room.")
            
            check_room(room)
            return room
        
            
            
        
print("Welcome to the House of Broken Dolls.")

difficulty = input("Enter your choice of difficulty: \n 1.Easy \n 2.Medium \n 3.Hard \n")

#randomly generate doll locations
if (difficulty=='1'):
    print("You wake up in a dark room having no memory of how you got here. \n \nInstructions : You are locked in a house with 6 rooms and a ghost of a young child. You must explore the house to find 3 keys to successfully escape. There are 3 dolls hidden around the house to help you pacify the ghost if you are to be attacked by it. You can collect the dolls if they are present in the rooms you enter. Good luck!")
    l2 = [1,2,3,4,5,6]
    doll1= random.choice(l2)
    l2.remove(doll1)
    doll2= random.choice(l2)
    l2.remove(doll2)
    doll3= random.choice(l2)
    
    dollcount = 0
    keycount = 0
    Ghost="Passive"

    while True:
        room=int(input("\nWhich room do you wish to enter?"))
        check_room(room)
        keycount,dollcount = collect_items(room,keycount,dollcount)
        
        if(keycount>0):
            Ghost="Active"
            print("\n\nBeware the ghost is active!\n")
            while(Ghost=="Active"): 
                room=input("\nWhich room do you wish to enter?")
                ghost_active(Ghost,room,keycount,dollcount);
               
        else:
            continue
            
        
        
    
elif (difficulty=='2'):
    l2 = [1,2,3,4,5,6]
    doll1= random.choice(l2)
    l2.remove(doll1)
    doll2= random.choice(l2)
    
elif (difficulty=='3'):
    l2 = [1,2,3,4,5,6]
    doll1= random.choice(l2)
    
    
    
     
    


