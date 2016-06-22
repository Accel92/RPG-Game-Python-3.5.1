from sys import exit
import random
import time

from ..chars1 import Knight
from ..chars1 import Mage
from ..chars1 import Shadow
from ..chars1 import Huntsman

from ..core import my_player
from ..core.error_log import wrong_choice

class Welcome(object):
	
	def start(self):
		
		print( '''\n\n\t\t\t" SHAZAKIN "\n\n\n
		Chapter 1. The beginning\n
		\nIt's been a while since you were awake...
		\nI'm glad you finally regained consciousness, I've been wating.
		\nYou might have lost your memories. It is such a cliche in this world,
		\nbut looking at your confused face it is possible.
		\nWhat is your name? Do you remember? 
		''')
		name = ""
		while True:
			print("<pick number>")
			print("1. Yes my name is...")
			print("2. Uh... No, I don't remember.")
			choose_name = input("\n>")
			if choose_name == "1":
				print("Yes, what is it?\n")
				name = input("...my name is ")
				name = name.capitalize()
				if len(name) <= 2:
					print("ERROR: invalid name, try again\n")
					continue
				break
			elif choose_name == "2":
				print("That's a pity, try again.\n")
			else:
				print(wrong_choice)
		
		my_player.set_name(name)
		print("\nThat is correct, %s, now then... " % my_player.get_name())
		print("Who are you? Can you recall? ")
		
		while True:
			print("\n1. My lady, I remember, I am King's faightful knight")
			print(" I await orders.")
			print("\n2. Yes, Wizard of the Astaroth Magic Entourage.")
			print("\n3. Would you please don't act so dignified?")
			print(" I know who I am, shades have already spoken...")
			print("\n 4. Bow's be my friend... and prey... yeah, prey")
			num_spec = input(">")
			if num_spec == "1":
				spec = Knight()	
				break
			elif num_spec == "2":
				spec = Mage()
				break
			else:
				print(wrong_choice)
		
		my_player.set_spec(spec)
		my_player.set_skills()
		print("%s, the %s" %(my_player.get_name(), my_player.get_spec().profession_name) + ", that sounds good...")
		
		while True:
			if num_spec == "1":
				print("My liege, It is me who is your servant... for now. Let's take our leave, shall we?")
				print("1. Let's stand up, I'll take my sword, armor and look around")
			elif num_spec == "2":
				print("I did hope you would remember, old one")
				print("1. You don't plan on telling me who you are, I know, let us go.")
			elif num_spec == "3":
				print("Yes.")
				print("... < Proceed >")
			elif num_spec == "4":
				print("1. Let's stand up, I'll take my stuff, robe and look around")
				print("1. Let's stand up, I'll take my stuff, robe and look around")

			print("2. < Sleep some more. >.")
			print("3. I don't care, this whole situation is lame, seriously.")
			what_do = input(">")
			
			if what_do == "1":
				break
			elif what_do == "2":
				print("What do now: ")
				what_do_now = input("1. Let's go\n2. Let's sleep some more\n>")
				if what_do_now == "1":
					break
				elif what_do_now == "2":
					pass
				else:
					print(error_log.wrong_choice)
			elif what_do == "3":
				print("You can always leave whis world, is that what you wish for?")
				yes_no = input("1. Yes\n2. No\n>")
				if yes_no == "1":
					print("K. Thx. Bye.")
					exit(0)
				elif yes_no == "2":
					print("Then let me take my leave now, good luck...\n")
					break
				else:
					print(wrong_choice)
			else:
				print(wrong_choice)

		print("We are done for now. I need to leave, take care %s" % my_player.get_name())
		print("press enter when ready to go")
		input()
		print("We will proceed when we reach zero:\n")
		i = 1
		while i > 0:
			print(i)
			i -= 1
			time.sleep(1)
		print("")
		return 'second_location'
