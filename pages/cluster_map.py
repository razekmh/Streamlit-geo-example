import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("Marker Cluster")

with st.expander("See source code"):
    with st.echo():
        m = leafmap.Map(center=[40, -100], zoom=4)
        cities = "https://drive.google.com/uc?export=download&id=1yes7GC64HNBH2OC23GtqYXlPpUXvsVYp"
        regions = "https://drive.google.com/uc?export=download&id=1I0Tcii9hJuI2esB-eDT7Iczv5QoJ-IJ9"

        m.add_geojson(regions, layer_name="SA Regions")
        m.add_points_from_xy(
            cities,
            x="Longitude",
            y="Latitude",
            # color_column="Region",
            icon_names=["gear", "map", "leaf", "globe"],
            spin=True,
            add_legend=True,
        )

m.to_streamlit(height=700)
