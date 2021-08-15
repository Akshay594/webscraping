from bs4 import BeautifulSoup
from pprint import pprint

with open('index.html') as f:
	soup = BeautifulSoup(f, 'html.parser')

div_elem_1 = soup.find('div', {'class':'parent1'}).find('li').findAll()
div_elem_2 = soup.find('div', {'id':'parent2'})
each_li_elelm = soup.find('div', {'class':'parent1'}).findAll('li')
each_li_elelm_2 = soup.find('div', {'id':'parent2'}).findAll('li')
# print(div_elem_1.find('li', {'class':'l1'}).text)


pprint(each_li_elelm_2)

# print(div_elem_2.find('li'))