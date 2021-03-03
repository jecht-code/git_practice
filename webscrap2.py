#Using 'automate the boring stuff' continue to learn more about webscrape
#page 237 download files from web with requests module.

# import requests

# res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

# try:
#     res.raise_for_status()
# except Exception as exc:
#     print('There is a aproblem: %s' % (exc))
# print(type(res))

# print(res.status_code)

# print(len(res.text))

# print(res.text[:250])

import requests, bs4
res = requests.get('http://nostarch.com')
res.raise_for_status()
#passing additional argument 'features' type can vary lxml, html, etc.
noStarchSoup = bs4.BeautifulSoup(res.text, features="lxml")
print(type(noStarchSoup))
