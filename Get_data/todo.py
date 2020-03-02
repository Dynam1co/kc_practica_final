import requests
from dotenv import load_dotenv
import os


def _url(path):
    return 'https://api.themoviedb.org/3' + path


def get_genres_movies():
    load_dotenv()
    return requests.get(_url('/genre/movie/list?api_key=%s&language=en-US' % os.getenv('API_KEY_TMDB')))


def get_genres_tv():
    load_dotenv()
    return requests.get(_url('/genre/tv/list?api_key=%s&language=en-US' % os.getenv('API_KEY_TMDB')))


def get_movie_popular(pNumPag=1):
    load_dotenv()

    return requests.get(_url('/movie/popular?api_key=%s&language=en-US&page=%s' % (os.getenv('API_KEY_TMDB'), pNumPag)))


def get_tv_popular():
    pass


def get_detail_movie():
    pass


def get_detail_tv():
    pass


def get_external_id_movie():
    pass


def get_external_id_tv():
    pass


def get_credits_movie():
    pass


def get_credits_tv():
    pass


def get_images_movie():
    pass


def get_images_tv():
    pass
