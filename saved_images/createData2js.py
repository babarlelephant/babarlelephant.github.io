f = open("list_of_saved_images.txt","r")

t = dict()

r = f.readline()
while len(r) >0:
	#print(r)
	r = r.split("\n")[0].split("\r")[0].split("\t")
	if len(r)==2:
		if len(r[0])>0:
			t.update({r[1]:r[0]})
	r = f.readline()
f.close()


f = open("../data.js","r",encoding="utf-8")
g = open("../data2.js","w",encoding="utf-8")
r=f.readline()
while len(r) >0:
	w = 0
	l = r.split("\n")[0].split("\r")[0].split("\t")
	if len(l) >= 3 and len(l[0])==0 and (len(l[1])==0 or (not l[1]=="HTML" and not l[1]=="#")):
		url = l[2].split("\n")[0].split("\r")[0]
		if url.startswith("http"):
			if url in t:
				rr = l[0]+"\t"+l[1]+"\tsaved_images/"+t[url]+"\t"+l[2]+"\n"
				g.write(rr)
				w= 1
	if w == 0:
		g.write(r)
	r=f.readline()
