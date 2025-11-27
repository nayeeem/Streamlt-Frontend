import streamlit as st # type: ignore
import pandas as pd # type: ignore
import numpy as np # type: ignore   

st.markdown("# Page 2 ❄️")
st.sidebar.markdown("# Data Frame ❄️")

# Create a simple DataFrame
st.write('DataFrame Example:')
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df # pyright: ignore[reportUnusedExpression]


# Display title and table
# Display the DataFrame as a table
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))





# This example uses Numpy to generate a random sample, 
# but you can use Pandas DataFrames, Numpy arrays, or 
# plain Python arrays. Display a random dataframe
st.write("And here's a random dataframe:")
dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

 
 
 
#Let's expand on the first example using the Pandas Styler object to highlight some elements in the interactive table.
# Display a styled dataframe
st.write("Here's a styled dataframe:")
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))



