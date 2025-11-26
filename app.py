import streamlit as st # type: ignore
import pandas as pd # type: ignore
import numpy as np # type: ignore
import time # type: ignore


# Set the title of the app
st.title('My First Streamlit App')

# Create a form with a slider and a checkbox
def form_callback():
    st.write(st.session_state.my_slider)
    st.write(st.session_state.my_checkbox)



# Create a form
st.write('Form Example:')
with st.form(key='my_form'):
    slider_input = st.slider('My slider', 0, 10, 5, key='my_slider')
    checkbox_input = st.checkbox('Yes or No', key='my_checkbox')
    submit_button = st.form_submit_button(label='Submit', on_click=form_callback)






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





left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")
    
    
    
    
    
# Add a progress bar
'Starting a long computation...'
# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'