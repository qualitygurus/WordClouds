import streamlit as st
import pandas as pd
import numpy as np
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter


st.set_option('deprecation.showPyplotGlobalUse', False)

st.header('Word Clouds by Quality Gurus')
st.markdown('An App by Sandeep Kumar')

#article.text
articletext = st.text_area("Please paste the text here, and press CTR+ENTER", "Text to convert to Word Cloud goes here.")
articletext = articletext + (10 * 'qualitygurus ')
STOPWORDS.update(['apply', 'evaluate', 'analyze', 'analysis', 'edit', 'will', 'using', 'A', 'B', 'C', 'D', 'E'])

left_column, right_column = st.beta_columns(2)

#Background image
backoption = left_column.selectbox('Select Background Image', ['Thumb', 'Bulb', 'Square', 'World Map', 'Car', 'Bird', 'Man', 'Tree1', 'Tree2', 'Cloud', 'Heart'])
backimage = backoption+'.jpg'
mask = np.array(Image.open(backimage))

#Background color
backcolor = right_column.selectbox('Select Background Color', ['white', 'black', 'slategrey', 'wheat', 'firebrick', 'lightgreen', 'lavender'])

#Number of words to be included
wordcount = st.slider('Word Count', min_value=50, max_value=500, value=50, step=50)


plt.figure( figsize=(20,10), facecolor='white')
wc = WordCloud(stopwords=STOPWORDS, font_path="Roboto-Bold.ttf",
               mask=mask, background_color=backcolor,
               max_words=wordcount, max_font_size=256,
               width=mask.shape[1], 
               height=mask.shape[0], contour_width=1, contour_color='steelblue')


wc.generate(articletext)
plt.imshow(wc, interpolation="bilinear")
plt.axis('off')
fig1 = plt.show()
st.pyplot(fig1)

