movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def isGoodMovie(movieName):
    for x in movies:
        if x['name'] == movieName and x['imdb'] > 5.5:
            return True
    return False

# print(isGoodMovie("Detective"))

def goodMovies():
    imdbMovies = []
    for x in movies:
        if x['imdb'] > 5.5:
            imdbMovies.append(x['name'])
    return imdbMovies

# print(goodMovies())

def sortCategory(category):
    categoryMovies = []
    for x in movies:
        if x['category'] == category:
            categoryMovies.append(x['name'])
    return categoryMovies

# print(sortCategory("Romance"))

def averageMovies():
    score = 0
    for x in movies:
        score += x['imdb']
    return round(score / len(movies), 2)

# print(averageMovies())

def averageCategory(category):
    score = 0
    cnt = 0
    for x in movies:
        if x['category'] == category: 
            score += x['imdb']
            cnt += 1
    return round(score / cnt, 2)

# print(averageCategory('Suspense'))
    