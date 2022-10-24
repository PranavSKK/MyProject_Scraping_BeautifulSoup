import requests

resp=requests.get("https://www.justwatch.com/ag/movie/k-g-f-chapter-1")
from bs4 import BeautifulSoup
soup = BeautifulSoup(resp.text, 'html.parser')

# <---IMDB, Director, Duration, Genre--->
a=soup.find_all(class_="detail-infos__value")
lis=["IMDb Ratings","Genre","Duration","Director Name"]
dis_info={}
for element in range(4):
    dis_info[lis[element]]=a[element].text
# print(dis_info)

# <---Movie Name--->
dis_movie={'Movie Name':f"{soup.title.text}"}
# print(dis_movie)

#<---Casting--->
cast=soup.find(class_="hidden-horizontal-scrollbar__items")
casting=[]
for name in cast:
    casting.append(name.text)
# print('Casting - ', tuple(casting))


#<---Release Year--->
dis_release={'Release Year':f"{soup.find(class_='text-muted').text}"}
# print(dis_release)

#<---Movie Link--->
link=soup.find_all(class_='jw-scoring-listing__rating')
for i in link:
    check=i.a
see=check.get('href')
dis_link={'Movie Link':f"{see}"}
# print(dis_link)

#<---Language--->
resplink=requests.get(f'{see}')
from bs4 import BeautifulSoup
souplang=BeautifulSoup(resplink.text, 'html.parser')

language=souplang.find_all('a')
language_lis=[]
for i in language:
    if(i.text=='Kannada' or i.text=='Hindi'):
       language_lis.append(i.text)
dis_language={'Language':f'{language_lis}'}
# print(dis_language)

def getInfo(*info):
    final=[]
    for i in info:
        final.append(i)
    print(final)

getInfo(dis_info,dis_movie,casting,dis_release,dis_language,dis_link)
    