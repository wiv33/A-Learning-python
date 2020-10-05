from nltk.tokenize import sent_tokenize

paragraph = "Natural language processing (NLP) is a subfield of computer science, information enginerring, " \
            "and artificial intelligence concerned with the interactions between computers and human (natural) " \
            "languages, in particular how to program computers to process and analyze large amounts of natural " \
            "language data. Challenges in natural language processing frequently involve speech recognition, " \
            "natural language understanding, and natural language generation."
"""
문장으로 나누기
"""
print(sent_tokenize(paragraph))
