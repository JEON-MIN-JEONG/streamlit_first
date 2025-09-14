import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

plt.rcParams['font.family'] = "AppleGothic"

data = pd.DataFrame({
    '이름': ['연준', '선미님', '동완님'],
    '나이': [33, 25, 26],
    '키' : ['171', '165', '175']
})

st.dataframe(data, use_container_width = True)

fig, ax = plt.subplots()
ax.bar(data['이름'], data['나이'])
st.pyplot(fig)

barplot = sns.barplot(x = '이름', y = '나이', data=data, ax=ax, palette='Set2')
fig = barplot.get_figure()

st.pyplot(fig)