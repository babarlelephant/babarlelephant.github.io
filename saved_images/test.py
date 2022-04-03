import requests
import shutil

url = "http://babarlelephant.free-hoster.net/visiting-the-wuhan-seafood-market/lapinallee6.jpg"
a_session = requests.Session()
a_session.get(url)
print(a_session.cookies)
print(a_session)
r = a_session.get(url,headers={"referrer":url,"accept":"image/jpeg"})
print(r.content)
quit()


headers={"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"accept-encoding": "gzip, deflate, br",
"accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
"cache-control": "no-cache",
"dnt": "1",
"pragma": "no-cache",
"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
"sec-ch-ua-mobile": "?0",
"sec-ch-ua-platform": '"Windows"',
"sec-fetch-dest": "document",
"sec-fetch-mode": "navigate",
"sec-fetch-site": "none",
"sec-fetch-user": "?1",
"upgrade-insecure-requests": "1",
"user-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
"referrer":"http://babarlelephant.free-hoster.net/visiting-the-wuhan-seafood-market/lapinallee6.jpg",
"Cookie":"set-cookie"}
#"Cookie":"sc_is_visitor_unique=rx8305768.1638462653.4179A8BD96A74F80A098D356F78DC5D7.1.1.1.1.1.1.1.1.1; __test=9fd246262ad6951909066972aafb24c6; sc_is_visitor_unique=rx9692532.1645929025.3A4E5185A8B44F218E08782A5FAD0ACE.13.13.13.12.10.10.9.9.6"}

headers["accept"] = "image/jpeg"

if 1:
	url = "http://babarlelephant.free-hoster.net/visiting-the-wuhan-seafood-market/lapinallee6.jpg"
	response = requests.get(url,headers=headers)
	with open('1.jpg', 'wb') as out_file:
		#shutil.copyfileobj(response.raw, out_file)
		out_file.write(response.content)
		print(response.content)
		print(response.headers)
		
	del(response)

if 0:
	url="https://cms-bucket.ws.126.net/2019/1231/d6007de0j00q3d77g00j4c0014000mic.jpg"
	response = requests.get(url,headers=headers)
	with open('2.jpg', 'wb') as out_file:
		#shutil.copyfileobj(response.content, out_file)
		out_file.write(response.content)
	del(response)