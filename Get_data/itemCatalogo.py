class ItemCatalogo:
    def __init__(self, pTipo, pPopularity, pVoteCount, pPosterPath, pId, pAdult, pBackdropPath, pOriginalLanguage, pOriginalTitle, 
            pTitle, pVoteAverage, pOverview, pReleaseDate):

        self.tipo = pTipo
        self.popularity = pPopularity
        self.vote_count = pVoteCount
        self.poster_path = pPosterPath
        self.id = pId
        self.adult = pAdult
        self.backdrop_path = pBackdropPath
        self.original_language = pOriginalLanguage
        self.original_title = pOriginalTitle
        self.genre_ids = []
        self.title = pTitle
        self.vote_average = pVoteAverage
        self.overview = pOverview
        self.release_date = pReleaseDate

    def insertGenreId(self, pId):
        self.genre_ids.append(pId)