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

## LMs
+ Pointwise Mutual Information (PMI) Matrix
+ SVD PMI Matrix
+ word2vec (Gensim)
+ bert (transformers)
+ floret (SpaCy & thinC)