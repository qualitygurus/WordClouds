import streamlit as st
import pandas as pd
import numpy as np
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import random
from PIL import Image, ImageFilter


def grey_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

st.set_option('deprecation.showPyplotGlobalUse', False)

st.header('Create a Word Cloud for any URL')
st.markdown('An App by Sandeep Kumar')
st.markdown('Right click on the image to save it on your drive')

#article.text

#Text
# articletext = st.sidebar.text_area("Please paste the text here, and press CTR+ENTER", "Text to convert to Word Cloud goes here.")

#Link
import bs4 as bs
import urllib.request
url = st.sidebar.text_input("Please enter the URL here, and press CTR+ENTER", "https://www.qualitygurus.com")
html = urllib.request.urlopen(url).read()
soup = bs.BeautifulSoup(html, features="html.parser")
articletext = soup.get_text()


articletext = articletext + (10 * 'qualitygurus ')
STOPWORDS.update(['apply', 'evaluate', 'analyze', 'analysis', 'edit', 'will', 'using', 'A', 'B', 'C', 'D', 'E'])

#Background image
backoption = st.sidebar.selectbox('Select Background Image', ['Thumb', 'Bulb', 'Square', 'World Map', 'Car', 'Bird', 'Man', 'Tree1', 'Tree2', 'Cloud', 'Heart'])
backimage = backoption+'.jpg'
mask = np.array(Image.open(backimage))

#Contour Width
contourwidth = st.sidebar.slider('Contour Width', min_value=0, max_value=5, value=2, step=1)

#Background color
backcolor = st.sidebar.selectbox('Select Background Color', ['white', 'black', 'slategrey', 'wheat', 'firebrick', 'lightgreen', 'lavender'])

#Number of words to be included
wordcount = st.sidebar.slider('Word Count', min_value=50, max_value=500, value=150, step=50)

#color or monochromatic?
monochrom = st.sidebar.radio("Text Colour:", ('Grey', 'Monochromatic', 'Multi Color'))


plt.figure( figsize=(20,10), facecolor='white')
wc = WordCloud(stopwords=STOPWORDS, font_path="Roboto-Bold.ttf",
               mask=mask, background_color=backcolor,
               max_words=wordcount, max_font_size=256,
               width=mask.shape[1], 
               height=mask.shape[0], contour_width=contourwidth, contour_color='black')


wc.generate(articletext)
#plt.imshow(wc, interpolation="bilinear")
image_colors = ImageColorGenerator(mask)

if monochrom == 'Grey':
  plt.imshow(wc.recolor(color_func=grey_color_func, random_state=3), interpolation="bilinear")
elif monochrom =='Monochromatic':
  plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
else:  
  plt.imshow(wc)
  

plt.axis('off')
fig1 = plt.show()
st.pyplot(fig1)

