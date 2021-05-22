# End-of-term exam

- Each student will be randomly assigned 2 topics, one about NLP and one about Python.

- The main focus will be on the NLP topic, but sufficient knowledge (at least that equivalent to a passing grade) must be
demonstrated in __both topics__ to pass the exam.

## Online examination

Due to the current situation, all exams will be held on Microsoft Teams.
This means:
- there is no preparation time after you are assigned topics,
- you must have your camera turned on,
- you must be prepared to share your screen and start writing code. We recommend that you already have Jupyter or Colab running when you start the exam.

## Exam times and location

|Date | Time | Location|
|-----|------|---------|
| May 25 (Tue) | 10:15 | Teams |
| Jun 01 (Tue) | 10:15 | Teams |
| Jun 08 (Tue) | 10:15 | Teams |


# I. NLP topics

## 1. Intro to NLP

* NLP tasks
   * Tokenization, lemmatization, POS tagging, language modelling
* Text representations
   * One hot encoding, TF-IDF
* Feature vectors, classification pipeline, logistic regression

## 2. Embeddings

* Problems with one-hot encoding
* Creating word embeddings, cosine similarity of word vectors
* Using word embeddings in NLP tasks

## 3. Deep Learning for NLP

* Learning types (supervised, unsupervised, classification, regression, clustering)
* Constructing train, validation and test sets
* Terminology
   * Loss function
   * Batch size
   * Epoch
   * Learning rate
* Feed forward neural networks
   * Neurons, activation functions, softmax
* Difference between feed forward and recurrent neural networks
 
## 4. Sequence modeling

* 3 basic types
    * Example applications
* What are the sequence elements? Pros and cons.
* Padding and batching

## 5. Transformers

* Attention
    * Basic idea not the exact formulation
* Transformer
    * Motivation
    * Basic components
    * Positional encoding

## 6. BERT

* Contextualized embeddings
* BERT tokenization
* BERT components
* Finetuning
* Applications

## 7. Evaluation metrics on NLP tasks
* Why do we use other metrics than accuracy?
* Evaluation of universal dependancy trees
* F-score
* ROUGE

## 8. Universal Dependecies

* What is in a dependency tree?
* What is CoNLL-U?
* Learning dependency parsing
    * Basic ideas, not step-by-step

# II. Python topics

## 1. Introduction

* What is Jupyter?
* Cell types, cell magic
* Kernel
* Short history of Python
* Python community, PEP, Pythonista

## 2. Functions and generators

* args, kwargs
* Default arguments
* Lambda functions
* Generators, yield statement

## 3. Type system

* Static vs. dynamic typing
* Built-in types (numeric, boolean), operators
* Mutability

## 4. Sequence types

* list vs. tuple
* Operators
* Advanced indexing
* Extra: time complexity of basic operations (lookup, insert, remove, append etc.)
* Set type and operations

## 5. Strings

* Character encodings: Unicode vs. UTF-8, encoding, decoding
* Common string operations
* String formatting (mention at least two kinds)

## 6. Object oriented programming I.

* Data attributes, methods, class attirbutes
* Inheritance, `super`
* Duck typing
* Magic methods, operator overloading

## 7. Object oriented programming II.

* Assignment, shallow copy, deep copy
* Object introspection
* Class decorators, static methods, class methods
* Properties

## 8. List comprehension

* Basic list comprehension (you should be able to write one)
* Generator expressions
* Extra: iteration protocol, writing an iterator class
* Set and dict comprehension
* `yield` keyword

## 9. Exception handling

* Motivation
* Basic keywords
* Defining exception classes

## 10. Context managers

* Motivation
* Basic usage
* Defining context managers

## 11. Decorators

* What are decorators?
* `@wraps` decorator
* Decorators with parameters
* Classes as decorators

## 12. Functional Python

* map, filter, reduce

## 13. `numpy`

* `ndarray`
    * Defining ndarrays (mention at least 3 functions)
    * array attributes
* Indexing and advanced indexing
* Operations an arrays
    * Mention at least 5 operations
* Extra: broadcasting
