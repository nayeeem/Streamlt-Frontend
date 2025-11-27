import streamlit as st # type: ignore
import pandas as pd # type: ignore
import numpy as np # type: ignore

st.markdown("# Page 3 🎉")
st.sidebar.markdown("# Page 3 🎉")


# Create and display a line chart
st.write("Here's a line chart:")
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)



# Create and display a map
st.write("Here's a map:")
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

