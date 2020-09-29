import spacy

# python -m spacy download en
nlp = spacy.load('en')

sentence = "Natural language processing (NLP) is a subfield of computer science, information engineering, " \
           "and artificial intelligence concerned with the interactions between computers and human (natural) " \
           "languages, in particular how to program computers to process and analyze large amounts of natural " \
           "language data."

doc = nlp(sentence)
