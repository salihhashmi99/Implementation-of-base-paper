***Public Requirement Dataset***
In this research, authors used PURE dataset which contains 79 requirements documents in different forms. It is publicly available on the internet for research use. In this dataset 
requirements documents had written in natural English language. And it can be used for NLP tasks such as ambiguity detection, identification and requirements categorisation

***Data Preporcessing***
After uploading the dataset successfully, we will have to preprocess the dataset because some sentences or paragraphs in these documents are irrelevant to the requirements and need to be
excluded from requirement sentences. For this purpose, we performed this task in three steps: tokenization, data cleaning, and normalization.

**Tokenization**
During Tokenization, requirements document is broken up into smaller segments.This process is also called data preparation. The requirements document in this process is broken into 
paragraphs, and the paragraph into sentences. In our experiments, we used sentence tokenization function nltk, which is a python library used to extract English sentences from a document

**Data Cleaning**
The objective of data cleaning process is to clean all irrelevant tokens from requirement sentences. This task is based on three steps. Punctuation removal, occur in this step such as full stops, question marks, commas,colons, etc are removed from the requirement sentences.
The second step is stop-word removal like high frequency words, such as (’they’, ’them’, ’their’, you,should, from etc) that don’t add any essential information to the requirement sentence.
The last step of data cleaning task is Non-alphabetic tokens removal that didn’t contain useful information. In our model, we used python library called Natural Language Tool Kit (NLTK).
This library contains most of the stop words in English language.

**Normalization**
In normalization process, we aimed to convert all the words to a more uniform sequence by transform it to a common base form. For normalization, we’ll use lemmatization to convert each 
word to its base (root) form. Lemmatization is preferred over stemming because it produces actual words (e.g., "running" becomes "run" instead of "runn"). In this task, we improve the text
modelling and matching.

***Feature Extraction (Vectorization)***
After Data pre-processing, the second step in our methodology is to extract representative features from the requirement sentences using a various number of features extraction 
techniques used in the NLP.
In research, authors used four vectorization techniques in NLP. Two of them are syntactical based methods: TF and TF-IDF. The other two vectorizatin methods are semantically based 
methods: Word2Vec4 and BERT5.

**Term Frequency**
Term Frequency is one of the basic vectorization methods and information retrieval in NLP. In our approach, we use this method to count how many times each word in the requirement 
sentences appears in all requirement documents and represent it as a vector. We created words dictionary containing all normalized words in the requirement document. This process also 
called bag of words (BOW). The rows corresponds to a requirement sentence and each column represents a unique word. The occurrence number in case the word is exist in the sentence 
increasing by one.

**Term Frequency Inverse Document Frequency**
In this technique of TF-IDF (Term Frequency Inverse Document Frequency), we quantify a word in requirement documents. Weight of each word were computed which signifies of its 
importance in all requirement documents. This method is widely used in information retrieval in NLP. This methods will improve the basic features that can be extracted from the 
requirement sentences so that can differentiate between NFR categories.

**Word2Vec**
Word2vec is a common word embedding model provided by Google to improve words representation. In our research, Word2Vec is used to enhance the numeric representation of the words through 
increase the accuracy of capturing word context from a document in semantic and syntactic words relationship. The value of each feature in the word representation ranging from zero to one.

The objective of using this model in this study is to invest the affect of semantic representation for requirement sentences using big data model to achieve high accuracy in NFR 
classification.

**Bi-directional Encoder Representations from Transformers**
BERT is a text representation technique stands for Bi-directional Encoder Representations from Transformers. BERT is an inflection point in the application of machine learning for NLP 
and confirmed to be state-of-the-art for a wide range of NLP tasks such semantic analysis and text classification. In this research paper, authors used BERT model with Masked-LM strategy
to represent requirement sentences in semantic numerical vectors. Then, they trained the classifiers on top of the transformer output of the BERT model.
