import spacy

nlp = spacy.load('en_core_web_md')

# open file with movie descriptions and hold descriptions in the list
movie_desc = []
try:
    with open("movies.txt", "r") as movies_file:
        for lines in movies_file:
            file_content = lines.strip().split("\n")
            movie_desc.append(file_content)
except FileNotFoundError:
    print("No such file!")


# convert file to list of strings
def split_desc():
    desc = []
    for elements in movie_desc:
        for items in elements:
            desc.append(items)
    return desc


# function that will compare given description to database
def find_movie(description):
    result = {}
    movies_list = split_desc()  # list of movies
    nlp_desc = nlp(description)
    for movie in movies_list:
        similarity = nlp(movie).similarity(nlp_desc)  # compare descriptions
        result[similarity] = movie.split(":")[0]  # load similarity and movie name into the dictionary
    return result[max(result)]  # print value with the highest key value


hulk_movie = """Will he save their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator."""

# call function
best_match = find_movie(hulk_movie)
print(best_match)
