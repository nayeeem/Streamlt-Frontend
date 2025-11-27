import streamlit as st # type: ignore
import time # type: ignore

st.markdown("# Page 5 📊")
st.sidebar.markdown("# Page 5 📊")

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