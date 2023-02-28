import spacy

# load language models
nlp = spacy.load("en_core_web_md")

mini_nlp = spacy.load("en_core_web_sm")


sample_words = "friend mate partner happy jolly merry"

tokens = nlp(sample_words)
tokens2 = mini_nlp(sample_words)

print("language model MD")
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

print("language model SM")
for token1 in tokens2:
    for token2 in tokens2:
        print(token1.text, token2.text, token1.similarity(token2))

# Some result are strange. For example merry and jolly have 0.999999761581421 when using MD model
# but only 0.189406961202621 when using SM model. Some values are obvious but some need some explanation.
# I have choose synonyms so I was expecting much higher values in some comparations.

