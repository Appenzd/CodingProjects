#Daniel A, Ben M, Cora R, Iz T Final Computer Science Project

import os

os.system('pip3 install selenium')
os.system('pip3 install wikipedia-api')
os.system('pip3 install time')

os.system('clear')

from selenium import webdriver
import wikipediaapi
import time

start_time = time.time()

#This is where you put the links to the first and last wikipedia articles.

firstArticleLink = input('What is your starting wikipedia article(please paste link): ')
secondArticleLink = input('What is your ending wikipedia article(please paste link): ')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)


# firstArticleLink = 'wikipedia.org/wiki/Rockstar_San_Diego'
# secondArticleLink = 'wikipedia.org/wiki/New_York_City_Police_Department_Emergency_Service_Unit'


firstArticleLink = firstArticleLink.replace('_', ' ')
secondArticleLink = secondArticleLink.replace('_', ' ')
#getting the name of the articles.
firstArticle = firstArticleLink.split('wikipedia.org/wiki/')
secondArticle = secondArticleLink.split('wikipedia.org/wiki/')

wiki = wikipediaapi.Wikipedia('en')

titles = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
pathfound = False
pagecount = -1
solution = 0
parh = 0
i = 0

for title in wiki.page(firstArticle[1]).links.keys():
  if title == secondArticle[1]:
        print(title, firstArticle[1])
        solution = title, firstArticle[1]
        pathfound = True
        break  
  tupel = title, firstArticle[1]
  titles[0].append(tupel)


while pathfound != True:
  i = 0
  pagecount = pagecount + 1
  for title in titles[pagecount]:
    i = i + 1
    print('I am currently getting links from ' + title[0] + " I have " + str(len(titles[pagecount]) - i) + ' more to go')
    for name in wiki.page(title[0]).links.keys():
      if title[0] == secondArticle[1]:
        solution = title
        pathfound = True
        break
      tupel = name, title[0]
      titles[pagecount + 1].append(tupel)
    if pathfound == True:
      break
  if pathfound == True:
    break

i = 0
path = solution[0]
pathfound = False

for page in titles[pagecount]:
  if page[0] == solution[0]:
    path = page[1] + ' ---> ' + path
    solution = page
    break

while pathfound != True:
  i += 1
  for page in titles[pagecount - 1]:
    if page[0] == solution[1]:
      path = page[1] + ' ---> ' + path
      pathfound = True
      break


#final text using the first article and the last article
print('Path found was ' + str(path))


for 有时候 in path.split(' ---> '):
  driver.get('https:/en.wikipedia.org/wiki/  ' + 有时候)
  time.sleep(3)

def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))


time_convert(time.time() - start_time)
