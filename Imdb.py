from bs4 import BeautifulSoup
import re

import sys,re
try:
    import urllib.request as urllib2
except:
    import urllib2
#if len(sys.argv) != 2:
 #   print("\nSyntax: python %s 'Movie title'" % (sys.argv[0]))
  #  exit()
#else :
 #   movie = '+'.join(sys.argv[1].split())


page=urllib2.urlopen("http://www.imdb.com/find?s=tt&q=Gravity")
soup = BeautifulSoup(page.read())
universities=soup.findAll('td',{'class':'result_text'})[0].string
mainlink=soup.findAll('td',{'class':'result_text'})[0].a['href']
print(universities)
print(mainlink)
movie=urllib2.urlopen("http://www.imdb.com/"+mainlink)
soup1 = BeautifulSoup(movie.read())
try:
    #rating = soup1.findAll('div',{'class':'titlePageSprite star-box-giga-star'})[0].string
    rating = soup1.findAll('span',{'itemprop':'ratingValue'})[0].string
    no = soup1.findAll('span',{'itemprop':'ratingCount'})[0].string + ".." +soup1.findAll('span',{'itemprop':'reviewCount'})[0].string
    dsc = soup1.findAll('p',{'itemprop':'description'})[0].string
    dir = soup1.findAll('span',{'class':'itemprop'})[0].string
    info_soup = soup1.findAll('span',{'class':'itemprop'})
    text_soup = soup1.findAll('h4',{'class':'inline'})
    tag_soup = soup1.findAll('div',{'class':'txt-block'})
    print(len(text_soup))
    print(len(info_soup))
    print(len(tag_soup))
    for i in range(len(info_soup)):
        #actors.append(info_soup[i].string)
        print("info.."+info_soup[i].string)

    for i in range(len(text_soup)):
        #actors.append(text_soup[i].string)
        print("text.."+text_soup[i].string)
        print("tag..."+tag_soup[i].text)
    #dsc = soup1.findAll('p',{'itemprop':'description'})[0].string
    #dsc = soup1.findAll('p',{'itemprop':'description'})[0].string

    print("Rating: ",rating,"/ 10.0")
    print("Rating: ",no)
    print("Director: ",dsc+"\n" + dir)
except :
    print("Not Found!")
