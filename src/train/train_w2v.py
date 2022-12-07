import gensim.models
from gensim import utils

corpus_path = "data/interim/oscar_uncased.txt"


class MyCorpus:
    """An iterator that yields sentences (lists of str)."""

    def __iter__(self):
        for line in open(corpus_path):
            # assume there's one document per line, tokens separated by whitespace
            yield utils.simple_preprocess(line.strip())


sentences = MyCorpus()
model = gensim.models.Word2Vec(sentences=sentences, vector_size=300, window=5, min_count=10, workers=3)
model.save("models/word2vec/oscar/oscarw2v.model")
print("Done")
