from os.path import exists
import os


f = open("list_of_saved_images.txt","r")
g = open("renumbered.txt","w")

tab = []

D = dict()

M = 0
r = f.readline()

while len(r) > 0:
	t = r.split("\n")[0].split("\r")[0].split("\t")
	if len(t) == 2:
		if len(t[0])==0:
			if t[1].startswith("http"):
				tab.append(t[1])
		else:
			#print(t)
			D.update({t[1]:t[0]})
			m = int(t[0].split(".")[0])
			if m > M:
				M=m
	r = f.readline()
print(M)
M+=1

notfound = []
for n in tab:
	print(n)
	if not n in D:
		k = "mass_downloader\\"+n.split("/").pop()
		if exists(k):
			print(" ",k)
			fn = str(M)+".jpg"
			g.write(fn+"\t"+n+"\n")
			os.system("copy "+k+" "+"mass_downloader\\renumbered\\"+fn)
			M+=1
		else:
			k = "mass_downloader\\"+n.split("/").pop().split(".")[0]+".jpg"
			if exists(k):
				print(" ",k,"  .jpg")
				fn = str(M)+".jpg"
				g.write(fn+"\t"+n+"\n")
				os.system("copy "+k+" "+"mass_downloader\\renumbered\\"+fn)
				M+=1
			else:
				print("not found", k)
				notfound.append(n)
g.write("\nnotfound:\n")
for a in notfound:
	g.write("\t"+a+"\n")