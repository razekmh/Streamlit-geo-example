import streamlit as st
import leafmap.foliumap as leafmap

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)

m = leafmap.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)
