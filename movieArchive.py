#themoviedb.org sitesinindeki bilgileri console üzerinde çalıştırma
#Siteye kayıt olduğunuzda size özel keyi 10.satıra girerseniz çalışacaktır

import requests
import json    #Optional-(Olmasada olur)

class Movies:
    def __init__(self):
        self.api_url = 'https://api.themoviedb.org'
        self.token = ''
    def keyWord(self,keyword):
        response = requests.get(self.api_url+'/3/search/keyword?api_key='+self.token+'&query='+keyword+'&page=1')
        return response.json()
    def popMov(self):
        response = requests.get(self.api_url+'/3/movie/popular?api_key='+self.token+'&language=en-US&page=all')
        return response.json()

    def nowPlaying(self):
        response = requests.get(self.api_url+'/3/movie/now_playing?api_key='+self.token+'&language=en-US&page=all')
        return response.json()

movie = Movies()
while True:
    user = input('1-Search Keyword\n2-Populer movies\n3-Now Playing\n4-Exit\nChoose number: ')
    if user == '4':
        break
    else:
        if user == '1':
            keyword = input('Please Search: ')
            search = movie.keyWord(keyword)
            search = list(search["results"])
            for i in search:
                print(i["name"])
            choose = input('Do you want to continue?(y/n): ')
            if choose == 'y':
                continue
            else:
                break

        elif user == '2':
            popMovie = movie.popMov()
            popMovie = popMovie['results']
            for i in popMovie:
                print(f'Movie Name: {i["original_title"]}  |  Popularity : {i["popularity"]}')
            choose = input('Do you want to continue?(y/n): ')
            if choose == 'y':
                continue
            else:
                break

        elif user == '3':
            vision = movie.nowPlaying()
            vision = vision['results']
            for i in vision:
                print(f'Movie Name: {i["original_title"]}  |  Overview: {i["overview"]}')
            choose = input('Do you want to continue?(y/n): ')
            if choose == 'y':
                continue
            else:
                break