import shutil

import requests

cookie="sc_is_visitor_unique=rx8305768.1638462653.4179A8BD96A74F80A098D356F78DC5D7.1.1.1.1.1.1.1.1.1; __test=9fd246262ad6951909066972aafb24c6; sc_is_visitor_unique=rx9692532.1645929025.3A4E5185A8B44F218E08782A5FAD0ACE.13.13.13.12.10.10.9.9.6"


url = 'https://i02piccdn.sogoucdn.com/b3fba75a4446dab2'

f = open("list_of_saved_images.txt","r")
t = dict()
r = f.readline()
i=1

while len(r) >0:
	print(r)
	r = r.split("\n")[0].split("\r")[0].split("\t")
	if len(r)==2:
		t.update({r[1]:r[0]})
		i+=1
		r = f.readline()
f.close()

g = open("failed_requests.txt","a")
h = open("list_of_saved_images.txt","a")

f = open("../data.js","r",encoding="utf-8")
r=f.readline()
while len(r) >0:
	l = r.split("\t")
	#print(r)
	if len(l) >= 3 and len(l[0])==0 and (len(l[1])==0 or (not l[1]=="HTML" and not l[1]=="#")):
		url = l[2].split("\n")[0].split("\r")[0]
		print(url)
		if 1:
			if url.startswith("http") and not url in t:
				ok = 0
				response = requests.get(url, stream=True)
				if response.status_code == 200:
					with open(str(i)+'.jpg', 'wb') as out_file:
						shutil.copyfileobj(response.raw, out_file)
					if not response.content.startswith(b"<html>"):
						t.update({url:i})
						h.write(str(i)+".jpg\t"+url+"\n")
						i+=1
						ok = 1
				if ok == 0:
					g.write(url+"\n")
			#print(response.content)
			#quit()
	r=f.readline()



