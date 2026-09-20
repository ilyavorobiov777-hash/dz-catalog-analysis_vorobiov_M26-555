import math

movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"],
    },
]


def average_rating(movies):
    total = 0
    for movie in movies:
        total = total + movie["rating"]
    return round(total / len(movies), 1)


def catalog_age_stats(movies, current_year=2026):
    ages = []
    for movie in movies:
        ages.append(current_year - movie["year"])
    oldest = max(ages)
    newest = min(ages)
    average = math.ceil(sum(ages) / len(ages))
    return (oldest, newest, average)


def duration_in_hours(minutes):
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours}ч {mins}м"


def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    else:
        return "средне" if rating >= 5 else "слабо"


def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _:
            return "старые"


def print_not_comedy(movies):
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])


def find_first_masterpiece(movies):
    i = 0
    while i < len(movies):
        if movies[i]["rating"] > 9.0:
            print("Первый шедевр:", movies[i]["title"])
            break
        i += 1
    else:
        print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count


def normalize_title(title):
    words = title.split()
    new_words = []
    for word in words:
        new_words.append(word[0].upper() + word[1:])
    return " ".join(new_words)


def make_slug(title):
    return title.lower().replace(" ", "-")


def format_report_line(movie):
    title = normalize_title(movie["title"])
    year = movie["year"]
    rating = movie["rating"]
    duration = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))
    return f'"{title}" ({year}) — {rating}/10, {duration}, жанры: {genres}'


def get_rating(movie):
    return movie["rating"]


def titles_sorted_by_rating(movies):
    sorted_movies = sorted(movies, key=get_rating, reverse=True)
    titles = []
    for movie in sorted_movies:
        titles.append(movie["title"])
    return titles


def top_n_by_rating(movies, n=3):
    sorted_movies = sorted(movies, key=get_rating, reverse=True)
    top = []
    for movie in sorted_movies[:n]:
        top.append((movie["title"], movie["rating"]))
    return top


def count_by_genre(movies):
    counts = {}
    for movie in movies:
        for genre in movie["genres"]:
            counts[genre] = counts.get(genre, 0) + 1
    return counts


def actor_filmography(movies):
    films = {}
    for movie in movies:
        for actor in movie["actors"]:
            titles = films.get(actor, [])
            titles.append(movie["title"])
            films[actor] = titles
    return films


def above_average_rating(movies):
    avg = average_rating(movies)
    return {m["title"]: m["rating"] for m in movies if m["rating"] > avg}


def all_genres(movies):
    genres = set()
    for movie in movies:
        genres = genres | movie["genres"]
    return genres


def common_actors(movie1, movie2):
    return set(movie1["actors"]) & set(movie2["actors"])


def genres_only_in_one(movies_a, movies_b):
    return all_genres(movies_a) - all_genres(movies_b)


def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie


def total_duration_good_movies(movies):
    return sum(m["duration_min"] for m in movies if m["rating"] > 7)


print(average_rating(movies))
print(catalog_age_stats(movies))
print(duration_in_hours(155))
print(rating_tier(9.2), rating_tier(7.0), rating_tier(5.0), rating_tier(4.8))
print(decade_label(2021), decade_label(2020), decade_label(2015), decade_label(2014))
print_not_comedy(movies)
find_first_masterpiece(movies)
find_first_masterpiece(movies[:5])
print(count_long_movies(movies), count_long_movies(movies, 100))
print(normalize_title("silent hours"))
print(make_slug("Silent Hours"))
print(format_report_line(movies[7]))
print(titles_sorted_by_rating(movies))
print(movies[0]["title"])
print(top_n_by_rating(movies, 3))
print(count_by_genre(movies))
print(actor_filmography(movies))
print(above_average_rating(movies))
print(all_genres(movies))
print(common_actors(movies[0], movies[3]))
print(genres_only_in_one(movies[5:6], movies[:5]))
for movie in iter_high_rated(movies):
    print(format_report_line(movie))
print(total_duration_good_movies(movies))
