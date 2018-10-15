import requests, bs4, sys

while(True):
	print('Press Y to continue or N to exit:')
	if(input('') == 'n' or input('') == 'N'):
		sys.exit()
	else:

		artist=input("Enter Artist's Name: ").replace(" ","")
		song=input("Track Name: ").replace(" ","")#azlyrics doesnot take spaces

		# url layout: www.azlyrics.com/lyrics/<artist>/<song>.html
		url='http://www.azlyrics.com/lyrics/%s/%s.html' % (artist,song)

		#to bypass azlyrics' DDoS protection, using headers it believes the program is a browser
		#some sample header on Linux and Windows
		#'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' 
		#'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0
		#FROM MY MACHINE:
		#'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'

		headers = { 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36' }


		res=requests.get(url,headers=headers)
		try:
			res.raise_for_status()
		except Exception as exc:
			print(exc) # print error
			#sys.exit() 
			continue

		print('\nConnecting to: %s' % url)

		site=bs4.BeautifulSoup(res.text,"html.parser")

		for lyrics in site.find_all("div", {"class":""}):
			print(lyrics.text)

