def get_url(url, encoding = 'utf-8'):
	import requests
    
	user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'

	ses = requests.Session()

	ses.headers.update({'User-agent' : user_agent, 'referer': None})

	r = ses.get(url)

	text = None

	if r.status_code != 200:
		print("[%d Error] %s" % (r.status_code, r.reason))
		quit()
	else:
		text = r.text

	return text