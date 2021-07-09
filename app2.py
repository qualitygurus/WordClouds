import streamlit as st
import pandas as pd
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

st.header('Word Clouds by')
st.markdown('Quality Gurus')

articletext = "This is a long text to check the function of word cloud"


#article.text
articletext = articletext + (20 * 'qualitygurus ')



STOPWORDS.update(['apply', 'evaluate', 'analyze', 'analysis'])


wc = WordCloud()
wc.generate(articletext)
plt.imshow(wc, interpolation="bilinear")
plt.axis('off')
fig1 = plt.show()
st.pyplot(fig1)
