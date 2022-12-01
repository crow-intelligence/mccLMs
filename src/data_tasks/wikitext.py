import re
import os

from nltk.tokenize import sent_tokenize, word_tokenize

data_root = "data/interim/huwiki"
folders = [e for e in os.listdir(data_root) if os.path.isdir(os.path.join(data_root, e))]

with open("data/interim/huwiki.txt", "w") as outfile:
    for folder in folders:
        articles = [e for e in os.listdir(os.path.join(data_root, folder)) if os.path.isfile(os.path.join(data_root, folder, e))]
        for article in articles:
            with open(os.path.join(data_root, folder, article)) as infile:
                a = infile.read()
                a = re.sub(r"</?doc.*>", "", a)
                sentences = sent_tokenize(a)
                for sentence in sentences:
                    if sentence:
                        words = word_tokenize(sentence)
                        words = [word for word in words if word.isalnum()]
                        if words:
                            outfile.write(" ".join(words) + "\n")

print("done")
