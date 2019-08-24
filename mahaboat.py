#!/usr/bin/env python


print "*%\@/*%$%*\@/*%$%*\@/*%$%*\@/*%$%*<*>*%$%*\@/*%$%*\@/*%$%*\@/*%$%*\@/*%$%*\@/*"
print "*  X   !   X   !   X   !   X   !       !   X   !   X   !   X   !   X   !   X *"
print "*      O       O       O    *** I   LOVE  XNXX ***     O       O       O     *"
print "*  X   !   X   !   X   !   X   !       !   X   !   X   !   X   !   X   !   X *"
print "*%/@\*%$%*/@\*%$%*/@\*%$%*/@\*%$%*<*>*%$%*/@\*%$%*/@\*%$%*/@\*%$%*/@\*%$%*/@\*"

while 1:
	x=input("\n enter your birth year\n")
	x%=7
	print "your mahaboat is:"
	print x
	y=raw_input("\n enter your day,\n 1)sun\n 2)mon\n 3)tue\n 4)wed\n 5)thu\n 6)fri\n 7)sat\n")
		
	a=0
	b=0
	if y == "sun":
		a+=1
		c=b+1
	elif y == "mon":
		a+=2
		c=b+2
	elif y == "tue":
		a+=3
		c=b+3
	elif y == "wed":
		a+=4
		c=b+4
	elif y == "thu":
		a+=5
		c=b+6
	elif y == "fri":
		a+=6
		c=b+0
	elif y == "sat":
		a+=7
		c=b+5
	else:
		print "fuck you\n"
	if x<a:
		x+=7
	o=x-a	
	
	if o == 1:
		print "you are ahtun"	
	
	elif o == 2:
		print "you are raza"
	elif o == 3:
		print "you are adipati"

	elif o == 4:
		print "you are marana"
	elif o == 5:
		print "you are thike"
	elif o == 6:
		print "you are puti"
	elif o == 0:
		print "you are binga"
	else:
		print "fuck you"

	raw_input("press <enter> to continue")
	
	
	age=input("\n enter your age\n")		
	cur=age+c-1
	
	cur%=8
	
	if cur == 1:
		print "you are in sun"	
	elif cur == 2:
		print "you are in moon"
	elif cur == 3:
		print "you are in mars"
	elif cur == 4:
		print "you are in marcury"
	elif cur == 5:
		print "you are in saturn"
	elif cur == 6:
		print "you are in jupiter"
	elif cur == 7:
		print "you are in rahu"
	elif cur == 0:
		print "you are in venus"
	else:
		print "fuck you , something is wrong"
	
	
	raw_input("press <enter> to restarting")

