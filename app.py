import requests
import pandas as pd
import streamlit as st
import plotly.express as px
pd.set_option('display.max_columns', None)  # or 1000
pd.set_option('display.max_rows', None)  # or 1000
pd.set_option('display.max_colwidth', None)  # or 199
pd.set_option('display.max_columns', None)
st.set_page_config(layout="wide")
pd.set_option('display.max_colwidth', None)


def _max_width_():
    max_width_str = f"max-width: 1300px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>
    """,
        unsafe_allow_html=True,
    )


_max_width_()

st.markdown("<h1 style='text-align: center; color: black;'>US - States search words in time</h1>", unsafe_allow_html=True)

df = pd.read_csv(r'state_market_tracker - Kopie.csv', sep='\t')
df=df[['period_begin','state','state_code','property_type','median_sale_price']]
df=df[ (df['property_type']=='Single Family Residential')] 
df.rename({'median_sale_price':'Median Sales Price ($)'},axis=1, inplace=True)
df['period_begin'] = pd.to_datetime(df['period_begin']).dt.date.astype(str)
df=df.sort_values("period_begin") # Make sure you sort the time horizon column in ascending order because this column is in random order in the raw dataset

fig = px.choropleth(df,
                    locations='state_code', 
                    locationmode="USA-states", 
                    color='Median Sales Price ($)',
                    color_continuous_scale="Viridis_r", 
                    scope="usa",
                    animation_frame='period_begin',
                    ) 

fig.add_scattergeo(
    locations=df['state_code'],
    locationmode="USA-states", 
    text=df['Median Sales Price ($)'],
    mode='text',
)

fig.update_layout(
    # title="Plot Title",
    autosize=False,
    width=1800,
    height=600,
)

st.plotly_chart(fig)

st.dataframe(df)
