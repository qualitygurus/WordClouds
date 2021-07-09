import streamlit as st
import pandas as pd
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)

st.header('Word Clouds by Quality Gurus')
st.markdown('An App by Sandeep Kumar')


articletext = st.text_area("Please paste the text here, and press CTR+ENTER", "Text to convert to Word Cloud goes here.")


#article.text
articletext = articletext + (10 * 'qualitygurus ')



STOPWORDS.update(['apply', 'evaluate', 'analyze', 'analysis'])



plt.figure( figsize=(20,10), facecolor='k')

stopwords = list(STOPWORDS) + ['edit','will' ]
wc = WordCloud(stopwords=stopwords, font_path="Roboto-Bold.ttf",
               background_color="white", max_words=200,
               max_font_size=300, random_state=40,
               width=2000, height=1000)
wc.generate(articletext)
plt.imshow(wc, interpolation="bilinear")
plt.axis('off')
fig1 = plt.show()
st.pyplot(fig1)
