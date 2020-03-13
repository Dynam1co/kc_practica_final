import requests
from dotenv import load_dotenv
import os
import urllib.request
from os.path import join
import numpy as np


def _url(path):
    return 'https://api.themoviedb.org/3' + path


def _image_url(path):
    return 'https://image.tmdb.org/t/p/original' + path


def get_genres_movies():
    load_dotenv()
    return requests.get(_url('/genre/movie/list?api_key=%s&language=en-US' % os.getenv('API_KEY_TMDB')))


def get_genres_tv():
    load_dotenv()
    return requests.get(_url('/genre/tv/list?api_key=%s&language=en-US' % os.getenv('API_KEY_TMDB')))


def get_movie_popular(pNumPag=1):
    load_dotenv()

    return requests.get(_url('/movie/popular?api_key=%s&language=en-US&page=%s' % (os.getenv('API_KEY_TMDB'), pNumPag)))


def get_tv_popular(pNumPag=1):
    load_dotenv()

    return requests.get(_url('/tv/popular?api_key=%s&language=en-US&page=%s' % (os.getenv('API_KEY_TMDB'), pNumPag)))


def get_prod_company_movie(pId):
    load_dotenv()
    return requests.get(_url('/movie/%s?api_key=%s&language=en-US' % (pId, os.getenv('API_KEY_TMDB'))))


def get_prod_company_tv(pId):
    load_dotenv()
    return requests.get(_url('/tv/%s?api_key=%s&language=en-US' % (pId, os.getenv('API_KEY_TMDB'))))


def get_external_id_movie(pId):
    load_dotenv()
    return requests.get(_url('/movie/%s/external_ids?api_key=%s' % (pId, os.getenv('API_KEY_TMDB'))))


def get_external_id_tv(pId):
    load_dotenv()
    return requests.get(_url('/tv/%s/external_ids?api_key=%s' % (pId, os.getenv('API_KEY_TMDB'))))


def get_credits_movie(pId):
    load_dotenv()
    return requests.get(_url('/movie/%s/credits?api_key=%s&language=en-US' % (pId, os.getenv('API_KEY_TMDB'))))


def get_credits_tv(pId):
    load_dotenv()
    return requests.get(_url('/tv/%s/credits?api_key=%s&language=en-US' % (pId, os.getenv('API_KEY_TMDB'))))


def get_budget_movie(pId):
    load_dotenv()
    return requests.get(_url('/movie/%s?api_key=%s&language=en-US' % (pId, os.getenv('API_KEY_TMDB'))))


def download_image(pIdElemento, pUrl):
    rutaImagen = '..\img'

    try:
        filename = '{}.jpg'.format(pIdElemento)
        full_path = join(rutaImagen, filename)

        urllib.request.urlretrieve(_image_url(pUrl), full_path)

        return full_path
    except Exception as e:
        return np.nan