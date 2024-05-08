import streamlit as st
import pandas as pd 
import base64
import plotly.express as px

st.set_page_config(layout = 'wide')

st.markdown(
    """
    <style>
        footer {display: none}
        [data-testid="stHeader"] {display: none}
    </style>
    """, unsafe_allow_html = True
)

# Logo
logo = "data/pwc.png"
logo_html = f'<div style="display: flex; justify-content: flex-end;"><img src="data:image/png;base64,{base64.b64encode(open(logo, "rb").read()).decode()}" style="width: 80px;"></div>'
st.markdown(f"{logo_html}", unsafe_allow_html=True)

# Open CSS
with open('styles.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html = True)

# Header: H1-H6 (define font size in styles.css)
header = "Jsme PwC. Pomůžeme vašemu byznysu v oblasti auditu, daní, práva či poradenství, ať už jde o technologie, fúze, udržitelnost či kybernetickou bezpečnost."
st.markdown(f'<h3>{header}</h3>', unsafe_allow_html=True)

# Different background color section - use text or headers
lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
st.markdown(f'<div class="custom_section_grey"><p class="text black_text">{lorem}</p></div>', unsafe_allow_html=True)
st.markdown(f'<div class="custom_section_orange"><p class="text white_text">{lorem}</p></div>', unsafe_allow_html=True)

# Defined text colors and how to use them
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."

st.markdown(f'<p class="text yellow_text">{text}</p>', unsafe_allow_html = True)
st.markdown(f'<p class="text tangerine_text">{text}</p>', unsafe_allow_html = True)
st.markdown(f'<p class="text orange_text">{text}</p>', unsafe_allow_html = True)
st.markdown(f'<p class="text rose_text">{text}</p>', unsafe_allow_html = True)
st.markdown(f'<p class="text red_text">{text}</p>', unsafe_allow_html = True)
st.markdown(f'<p class="text black_text">{text}</p>', unsafe_allow_html = True)
st.markdown(f'<p class="text dark_grey_text">{text}</p>', unsafe_allow_html = True)
st.markdown(f'<p class="text medium_grey_text">{text}</p>', unsafe_allow_html = True)
st.markdown(f'<p class="text grey_text">{text}</p>', unsafe_allow_html = True)
st.markdown(f'<p class="text light_grey_text">{text}</p>', unsafe_allow_html = True)

# Data
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
})
st.markdown('####')
col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):     
        st.markdown(f'<p class="text black_text">Age of Individuals</p>', unsafe_allow_html = True)

        custom_color = ['#D04A02']  

        fig = px.bar(
        df,
        x='Name',
        y='Age',
        color_discrete_sequence=custom_color
        )
        
        st.plotly_chart(fig, use_container_width=True)

with col2:
    st.dataframe(df, hide_index=True, use_container_width=True)

# Create the button
btn = st.button("Herel")
if btn:
    st.markdown(f'<p class="text black_text">There</p>', unsafe_allow_html = True)
