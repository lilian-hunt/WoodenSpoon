import sys
import os
if len(sys.argv) == 1:
	print("No file specified")
	sys.exit()
file = sys.argv[1]
if os.path.exists(file) == False:
	print("Could not read file")
	sys.exit()
with open(str(file),"r") as line:
	the_file = line.readlines()
winners ={}
if len(sys.argv) == 1:
	print("No file specified")
for i in the_file:
	winner,loser = i.split(" d. ")
	if winner not in winners:
		winners[winner] = 1
	else:
		winners[winner] +=1
onlywon1 = []
maxvalue =0
for key, value in winners.items():
	if value>maxvalue:
		maxvalue = value
if maxvalue == 1:
	a, loser = the_file[0].split(" d. ")
	loser = loser.rstrip()
	print(str(loser)+" wins the wooden spoon!\n")
	print("F: "+str(the_file[0].rstrip()))
	sys.exit()
check = []
for i in winners:
	if (winners[i]) == 1:
		onlywon1.append(i)

def biggerloser(listoflosers):
	for i in listoflosers:
		interest = i
		x = i
		checker = 0
		for numchecks in range(maxvalue-1):
			for line in the_file:
				string =  " d. "+str(x)	
				if string in line:
					win, los = line.split(" d. ")
					checker +=1
					x = win
			if checker == maxvalue-1:
				therealloser = interest
	return therealloser
only1wonreal = biggerloser(onlywon1)
finals = ["F: ", "SF: ","QF: "]
for line in the_file:
	string =  only1wonreal + " d. "
	if string in line:
		win,los = line.split(" d. ")
		thelos = (los.rstrip())
if thelos == "Bye":
	print("No one wins the wooden spoon.")
else:
	print(thelos,"wins the wooden spoon!\n")
	x = thelos
	for i in range(maxvalue):
		thestr = ""
		if (maxvalue-i-1)<3:
			thestr += (finals[maxvalue-i-1])
		else:
			thestr += ("R"+str(i+1)+": ")
		for i in the_file:
			string =  " d. "+ (x)
			if string in i:
				win, los = i.split(" d. ")
				i=i.rstrip()
				thestr += i
				x = win
				break
		print(thestr)
