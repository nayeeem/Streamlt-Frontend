import streamlit as st # type: ignore
import pandas as pd # type: ignore

st.markdown("# Page 6 📊")
st.sidebar.markdown("# Page 6 📊")

# Create a selectbox to choose a number from the dataframe
st.write("Selectbox Example:")
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

# Create a selectbox
option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

# Display the selected option
'You selected: ', option # type: ignore


# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)
