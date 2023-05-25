from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/app.py` to customize this app to your heart's desire :heart:


In the meantime, below is an example of what you can do with just a few lines of code:
"""


import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

c = alt.Chart(chart_data).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.subheader('Altair Chart')
st.altair_chart(c, use_container_width=True)

st.subheader('Bar Chart')
st.bar_chart(chart_data)

