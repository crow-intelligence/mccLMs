# Discovering Language Models
_WARNING_: This repo contains suboptimal code.
It is made for educational purposes, and it
is not suitable for any serious usage.

## Data sources
+ [Oscar 2019](https://oscar-project.org/post/oscar-2019/) - Hungarian subset
+ [Wikidumps](https://dumps.wikimedia.org/huwiki/20221120/) - huwiki-20221120-pages-articles-multistream.xml.bz2 dump

## Preparing data
+ extracting text from wiki dump `wikiextractor data/raw/wiki/huwiki-20221120-pages-articles-multistream.xml.bz2 -o data/interim/huwiki`
+ Get sentences from wiki
+ Get sentences from Oscar
+ split sentences tokenized and pre-filtered texts
  (200-500 lines per file is a good choice)
```bash
split -n 18128 data/interim/slices/huwiki.txt data/interim/wiki_slices/huwiki_sliced
```
and
```bash
split -n 305479 data/interim/oscar.txt data/interim/oscar/oscar_split
```

## LMs
+ Pointwise Mutual Information (PMI) Matrix
+ SVD PMI Matrix
+ word2vec (Gensim)
+ bert (transformers)
+ floret (SpaCy & thinC)

### word2vec

### floret
```bash
../../opt/floret/floret cbow -dim 300 -minn 3 -maxn 6 -mode floret -hashCount 4 -bucket 50000 -input data/interim/huwiki.txt -output models/floret/huwiki/huwiki_vectors
```
```bash
../../opt/floret/floret cbow -dim 300 -minn 4 -maxn 5 -mode floret -hashCount 4 -bucket 50000 -input data/interim/oscar.txt -output models/floret/oscar/oscar_vectors
```