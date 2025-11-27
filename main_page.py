import streamlit as st # pyright: ignore[reportMissingImports]

# Main page content
st.markdown("# Main page: Form🎈")
st.sidebar.markdown("# Main page 🎈")

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

