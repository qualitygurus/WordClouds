import streamlit as st
import pandas as pd
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)

st.header('Word Clouds by')
st.markdown('Quality Gurus')


articletext = st.text_area("Please paste the text here", "Text to convert to Word Cloud goes here.")


#article.text
articletext = articletext + (20 * 'qualitygurus ')



STOPWORDS.update(['apply', 'evaluate', 'analyze', 'analysis'])


wc = WordCloud()
wc.generate(articletext)
plt.imshow(wc, interpolation="bilinear")
plt.axis('off')
fig1 = plt.show()
st.pyplot(fig1)

