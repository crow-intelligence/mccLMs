# Discovering Language Models
_WARNING_: This repo contains suboptimal code.
It is made for educational purposes, and it
is not suitable for any serious usage.

## Prerequisits
+ a modern web browser (Chrome or Mozilla)
+ a Google account
+ working internet connection

## How to use Colab notebooks
+ open the Notebooks folder on GitHub
+ click on the notebook you'd like to run on Colab
![gh](https://github.com/crow-intelligence/mccLMs/blob/main/imgs/Screenshot%20from%202022-12-07%2010-11-27.png)
+ click on the Open in Colab badge
![oic](https://github.com/crow-intelligence/mccLMs/blob/main/imgs/Screenshot from 2022-12-07 10-19-44.png)
+ the notebook is now available in Colab
![nic](https://github.com/crow-intelligence/mccLMs/blob/main/imgs/Screenshot from 2022-12-07 10-11-27.png)
+ save the notebook into your own Colab folder on 
Google Drive
![stc](https://github.com/crow-intelligence/mccLMs/blob/main/imgs/Screenshot from 2022-12-07 10-11-39.png)
+ Copy [this](https://drive.google.com/drive/folders/1-tPDfuPU7PvcEnaEv2U4X3giTRoyFnCy?usp=sharing)
Google Drive folder to your own `Colab Notebooks` folder
+ run the first cell of your notebook on Colab
![rcl](https://github.com/crow-intelligence/mccLMs/blob/main/imgs/Screenshot from 2022-12-07 10-42-08.png)
+ allow it run, grant permissions to Colab,
and you'll see sth like the following
![run](https://github.com/crow-intelligence/mccLMs/blob/main/imgs/Screenshot from 2022-12-07 10-43-56.png)
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
Modify corpus path and the path of model_save
before running this script.
```bash
python src/train/train_w2v.py
```
### floret
```bash
../../opt/floret/floret cbow -dim 300 -minn 3 -maxn 6 -mode floret -hashCount 4 -bucket 50000 -input data/interim/huwiki.txt -output models/floret/huwiki/huwiki_vectors
```
```bash
../../opt/floret/floret cbow -dim 300 -minn 4 -maxn 5 -mode floret -hashCount 4 -bucket 50000 -input data/interim/oscar.txt -output models/floret/oscar/oscar_vectors
```