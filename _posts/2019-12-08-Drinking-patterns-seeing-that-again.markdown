---
layout: post
title: NLP = No loser Permitted?
date: 2019-12-09 19:32:24.000000000 +09:00
author: Shan J.
---

How will you represent the semantic meanings of word in a sentence, sounds challenging right?

### Curse of dimensionality

Humans have rich representations of words that let us extract the features, the simplest might be the one-hot representation, it treats the word completely independent of each other. For example, the feature of word in “**word** is‘dog’ ” is as dis-similar to “**word** is ‘thinking’ ” than it is to “**word** is ‘cat’ ”.

The dense-feature representation tried to solve this problem by representing the core feature with a vector. Each feature corresponds to several input vector entries. No explicit encoding of feature combinations. One NLP scholar have shared the summarization of feature extraction magic in the field. 

Instead of seeking the help from external knowledge base, just vector addition and subtraction with cosine similarity is enough for solving the problem. This trick works in a few different flavors:

### Word Embedding Flavors

* SVD-based vectors
* Word2vec
* GloVe (hybrid) 

The Word embeddings have already become the de facto standard in NLP and the vector representations are: 

* Distributed: Rather than sparse in the linear model, distributed throughout all the indices; 
* Distributional: The word distribution is derived from a corpus.

### Basic Naming rules in Data Science

In Columbia, courses with certain key words are pretty popular these days. Especially these come with statistical learning and modelling tutorials which not only gives hands-on experience of programming language exploratory analysis, but also crucial mindset for data science in practice.

1. **Deep Learning**: In neural network models, when we have more than one hidden layer, then it is said that we are having a deep network, so we call the architecture ***Deep Learning***.
2. **Machine Learning**: 
3. **Data Mining**:






