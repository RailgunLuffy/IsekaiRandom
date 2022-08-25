import requests
import random
from bs4 import BeautifulSoup
from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.

BASE_ISEKAI_URL = 'https://myanimelist.net/anime/genre/62/Isekai?page={}'

def home(request):
    return render(request, 'myapp/isekai.html')

def result(request):
    isekai_result = []
    def getIsekaiList(pageNo):
        response = requests.get(BASE_ISEKAI_URL.format(pageNo))
        data = response.text
        soup = BeautifulSoup(data, features='html.parser')

        post_listings = soup.find(class_='seasonal-anime-list',).find_all('div', {'class':'js-anime-category-producer seasonal-anime js-seasonal-anime js-anime-type-all js-anime-type-1'})

        for post in post_listings:
            title = post.find(class_='link-title').text
            url = post.find(class_='link-title').get('href')
            image_url = post.find(class_='image').find('img').get('data-src')
            # synosis = post.find(class_='preline').text
    
            isekai_result.append((title, url, image_url))
    
    getIsekaiList('1')
    getIsekaiList('2')
    getIsekaiList('3')

    result = {
        'isekai_result': random.choice(isekai_result),
    }
    
    return render(request, 'myapp/result.html', result)