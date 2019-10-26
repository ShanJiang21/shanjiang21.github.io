---


layout: post
title: Python text processing 1
date: 2019-10-22 11:32:24.000000000 +09:00
author: Shan Jiang
tags:
    - Python
    - Computational Social Science 

---

<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML' async></script>
**Standardized Computing, Standardized Research**

>  

#### Installing `Tensorflow` and `Keras`  

```python
pip install tensorflow
pip install keras
```

```python
from nltk import word_tokenize
from nltk import bigrams
from nltk import trigrams
from nltk import ngrams
```

#### Data scapping 

You can either use `urlopen` or `request.get` while the latter one consist of two steps 

```python
## Source from Yale law center
url1  = urlopen('http://avalon.law.yale.edu/19th_century/gettyb.asp').read()

```

```python
url2 = raw_input("Enter a website to extract the URL's from: ")
r  = requests.get("http://" +url2)
data = r.text

```

```python
## text cleaning
soup = BeautifulSoup(url)
text = soup.p.contents[0]
text_1 = text.lower() 
text_2 = re.sub('\W', ' ', text_1)
```

#### Wrangling Web data

