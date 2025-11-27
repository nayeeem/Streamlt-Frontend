import streamlit as st # type: ignore
import numpy as np # type: ignore
import pandas as pd # type: ignore  
st.markdown("# Page 4 📊")
st.sidebar.markdown("# Page 4 📊")

# Create a text input box
st.write("Text Input Example:")
st.text_input("Your name", key="name")
# You can access the value at any point with:
st.session_state.name


# Create a checkbox to show/hide a dataframe
st.write("Show/Hide DataFrame Example:")
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data # type: ignore
    
    
left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")
expander = st.expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")
    
    
    