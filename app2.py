import streamlit as st
import pandas as pd
from newspaper import Article
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

st.header('Word Clouds by')
st.markdown('Quality Gurus')

article = Article('https://asq.org/cert/resource/docs/2016/CSQP%202016%20Final%20BOK.pdf')

article.download()
article.parse()

#article.text
article.text = article.text + (20 * 'qualitygurus ')
article.text


STOPWORDS.update(['apply', 'evaluate', 'analyze', 'analysis'])
STOPWORDS

wc = WordCloud()
wc.generate(article.text)
plt.imshow(wc, interpolation="bilinear")
plt.axis('off')
plt.show()
