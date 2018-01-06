# #import the library used to query a website
# import urllib2
#
# #specify the url
# wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
#
# #Query the website and return the html to the variable 'page'
# page = urllib2.urlopen(wiki)
#
# #import the Beautiful soup functions to parse the data returned from the website
# from bs4 import BeautifulSoup
#
# #Parse the html in the 'page' variable, and store it in Beautiful Soup format
# soup = BeautifulSoup(page)
#
# #Make content legible
# print(soup.prettify())
#
# #get content and tags
# soup.title
#
# #get content between tags as strings
# soup.title.string
#
# #get ahref tags, doesn't return b/w
# soup.a
#
# #use find_all() instead
# all_links = soup.find_all("a")
#
# #iterate to get only links
# for link in all_links:
# 	print(link.get("href"))
#
# #
# #
# #
# # script = html.new_tag(
# #                     "script",
# #                     src=self.path,
# #                     type='application/javascript')
# #                 html.body.insert(0, script)
# #                 flow.response.content = str(html).encode("utf8")
# #
# # <script src="http://httpserverIP:8080/script.js"></script>


# counter = 0
# for letter in s:
#     print("Counter: {} and Letter: {}".format(counter,letter))
#     counter+=1
#
# import re
# m = re.search(r"\d", s)
# print(m)
#
# import re
# x = 'Your number is <b>123</b>'
# print(re.search('(?<=Your number is )<b>(\d+)</b>',x).group(1))

# import requests
#
# session = requests.Session()
# index_url   = 'http://livefootball.ws/'
# index_request = session.get(index_url)
#
# #change encoding of the response
# index_request.encoding = 'CP1251'
#
# #print page content
# print(index_request.text)



