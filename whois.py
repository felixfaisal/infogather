from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url ='https://www.whois.com/whois/'
url =input("Enter domain name :")
newurl = my_url+url
my_url = newurl
uClient= uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html,'html.parser')
con=page_soup.findAll("div",{"class":"whois_main_column"})
co=con[0].findAll("div",{"class":"df-block"})
filename="domain.csv"
f = open(filename, "w")

for i in range(0,len(co)):
	#print(containers[i].text+" "+container[i].text)
	header = co[i].findAll("div",{"class":"df-heading"})
	f.write(header[0].text+"\n")
	print(header[0].text.upper())	
	label  = co[i].findAll("div",{"class":"df-label"})
	values = co[i].findAll("div",{"class":"df-value"})
	for j in range(0,len(label)):
		print(label[j].text+" "+values[j].text)
		f.write(label[j].text.replace(",","")+","+values[j].text.replace(",","")+"\n")
	
	print("\n")
	f.write("\n")

f.write("\n")	
f.close()
			

	

