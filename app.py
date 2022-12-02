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

import plotly.graph_objects as go
import numpy as np
from jupyter_dash import JupyterDash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

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

import pandas as pd 
import plotly.express as px

df = pd.read_csv(r'us_state_searchwords.csv', sep=',')
df['period_begin'] = pd.to_datetime(df['period_begin']).dt.date.astype(str)
df=df.sort_values("period_begin") # Make sure you sort the time horizon column in ascending order because this column is in random order in the raw dataset


unique_periods = df['period_begin'].unique()

def create_figures(x):
    df_fig = df[df["period_begin"]=="{}".format(unique_periods[x])]
    fig = px.choropleth(df_fig,
                            locations='state_code', 
                            locationmode="USA-states", 
                            color='search_word',
                            color_continuous_scale="Viridis_r", 
                            title='search_word',
                            scope="usa")
    fig.add_scattergeo(
        locations=df_fig['state_code'],
        locationmode="USA-states", 
        text=df_fig['search_word'],
        mode='text',
    )
    return fig




fig0 = create_figures(0)
fig1 = create_figures(1)
fig2 = create_figures(2)
fig3 = create_figures(3)
fig4 = create_figures(4)
fig5 = create_figures(5)
fig6 = create_figures(6)
fig7 = create_figures(7)
fig8 = create_figures(8)
fig9 = create_figures(9)
fig10 = create_figures(10)
fig11 = create_figures(11)
fig12 = create_figures(12)
fig13 = create_figures(13)
fig14 = create_figures(14)
fig15 = create_figures(15)
fig16 = create_figures(16)
fig17 = create_figures(17)
fig18 = create_figures(18)
fig19 = create_figures(19)
fig20 = create_figures(20)
fig21 = create_figures(21)
fig22 = create_figures(22)
fig23 = create_figures(23)
fig24 = create_figures(24)
fig25 = create_figures(25)
fig26 = create_figures(26)
fig27 = create_figures(27)
fig28 = create_figures(28)
fig29 = create_figures(29)
fig30 = create_figures(30)
fig31 = create_figures(31)
fig32 = create_figures(32)
fig33 = create_figures(33)
fig34 = create_figures(34)
fig35 = create_figures(35)
fig36 = create_figures(36)
fig37 = create_figures(37)
fig38 = create_figures(38)
fig39 = create_figures(39)
fig40 = create_figures(40)
fig41 = create_figures(41)
fig42 = create_figures(42)
fig43 = create_figures(43)
fig44 = create_figures(44)
fig45 = create_figures(45)
fig46 = create_figures(46)
fig47 = create_figures(47)



slider_names = {0: '01-02',
1: '01-09',
2: '01-16',
3: '01-23',
4: '01-30',
5: '02-06',
6: '02-13',
7: '02-20',
8: '02-27',
9: '03-06',
10: '03-13',
11: '03-20',
12: '03-27',
13: '04-03',
14: '04-10',
15: '04-17',
16: '04-24',
17: '05-01',
18: '05-08',
19: '05-15',
20: '05-22',
21: '05-29',
22: '06-05',
23: '06-12',
24: '06-19',
25: '06-26',
26: '07-03',
27: '07-10',
28: '07-17',
29: '07-24',
30: '07-31',
31: '08-07',
32: '08-14',
33: '08-21',
34: '08-28',
35: '09-04',
36: '09-11',
37: '09-18',
38: '09-25',
39: '10-02',
40: '10-09',
41: '10-16',
42: '10-23',
43: '10-30',
44: '11-06',
45: '11-13',
46: '11-20',
47: '11-27',}


frames=[go.Frame(data=fig0.data, layout=fig0.layout),
go.Frame(data=fig1.data, layout=fig1.layout),
go.Frame(data=fig2.data, layout=fig2.layout),
go.Frame(data=fig3.data, layout=fig3.layout),
go.Frame(data=fig4.data, layout=fig4.layout),
go.Frame(data=fig5.data, layout=fig5.layout),
go.Frame(data=fig6.data, layout=fig6.layout),
go.Frame(data=fig7.data, layout=fig7.layout),
go.Frame(data=fig8.data, layout=fig8.layout),
go.Frame(data=fig9.data, layout=fig9.layout),
go.Frame(data=fig10.data, layout=fig10.layout),
go.Frame(data=fig11.data, layout=fig11.layout),
go.Frame(data=fig12.data, layout=fig12.layout),
go.Frame(data=fig13.data, layout=fig13.layout),
go.Frame(data=fig14.data, layout=fig14.layout),
go.Frame(data=fig15.data, layout=fig15.layout),
go.Frame(data=fig16.data, layout=fig16.layout),
go.Frame(data=fig17.data, layout=fig17.layout),
go.Frame(data=fig18.data, layout=fig18.layout),
go.Frame(data=fig19.data, layout=fig19.layout),
go.Frame(data=fig20.data, layout=fig20.layout),
go.Frame(data=fig21.data, layout=fig21.layout),
go.Frame(data=fig22.data, layout=fig22.layout),
go.Frame(data=fig23.data, layout=fig23.layout),
go.Frame(data=fig24.data, layout=fig24.layout),
go.Frame(data=fig25.data, layout=fig25.layout),
go.Frame(data=fig26.data, layout=fig26.layout),
go.Frame(data=fig27.data, layout=fig27.layout),
go.Frame(data=fig28.data, layout=fig28.layout),
go.Frame(data=fig29.data, layout=fig29.layout),
go.Frame(data=fig30.data, layout=fig30.layout),
go.Frame(data=fig31.data, layout=fig31.layout),
go.Frame(data=fig32.data, layout=fig32.layout),
go.Frame(data=fig33.data, layout=fig33.layout),
go.Frame(data=fig34.data, layout=fig34.layout),
go.Frame(data=fig35.data, layout=fig35.layout),
go.Frame(data=fig36.data, layout=fig36.layout),
go.Frame(data=fig37.data, layout=fig37.layout),
go.Frame(data=fig38.data, layout=fig38.layout),
go.Frame(data=fig39.data, layout=fig39.layout),
go.Frame(data=fig40.data, layout=fig40.layout),
go.Frame(data=fig41.data, layout=fig41.layout),
go.Frame(data=fig42.data, layout=fig42.layout),
go.Frame(data=fig43.data, layout=fig43.layout),
go.Frame(data=fig44.data, layout=fig44.layout),
go.Frame(data=fig45.data, layout=fig45.layout),
go.Frame(data=fig46.data, layout=fig46.layout),
go.Frame(data=fig47.data, layout=fig47.layout),
        ]



# construct a figure with frames
# fig = go.Figure(fig1)
import time

fig = go.Figure(data=frames[0].data, frames=frames)
fig.update_layout(
            title_x=0.5,
            title_text = unique_periods[0],
            geo_scope='usa', # limite map scope to USA
        )
# fig = fig.update_layout(  
#     updatemenus=[{"buttons": [{"args": [None, {"frame": {"duration": 500, "redraw": True}}],
#                                "label": "&#9654;",
#                                "method": "animate",},],
#                   "type": "buttons",}],
#     sliders=[{"steps": [{"args": [[f.name],{"frame": {"duration": 0, "redraw": True}, "mode": "immediate",},],
#                          "label": f.name, "method": "animate",}
#                         for f in frames],
#              }],)


# Build App
app = JupyterDash(__name__)
app.layout = html.Div(
    [dcc.Graph(id="graph", figure=fig), 
     html.Button("Play", id="dashPlay", n_clicks=0),
     dcc.Slider(id="dashSlider", min=0, max=len(frames)-1, value=0, marks=slider_names),
     dcc.Interval(id="animateInterval", interval=3000, n_intervals=0, disabled=True),
     html.Div(id="whichframe", children=[]),
    ],
)

# core update of figure on change of dash slider    
@app.callback(
    Output("whichframe", "children"),
    Output("graph", "figure"),
    Input("dashSlider", "value"),
)
def setFrame(frame):
    if frame:
        tfig = go.Figure(fig.frames[frame].data, frames=fig.frames, layout=fig.layout)
        fig.update_layout(
            # title_text = '',
            title_text = unique_periods[frame],
            title_x=0.5,
            geo_scope='usa', # limite map scope to USA
            # sliders=[{"currentvalue": {"prefix": "Year=", "font": {'size': 20}}}]
        )
# fig.update_layout(sliders=[{"currentvalue": {"prefix": "Year=", "font": {'size': 20}}}])

        try:
            tfig.layout['sliders'][0]['active'] = frame
        except IndexError:
            pass
        return frame, tfig
    else:
        return 0, fig

# start / stop Interval to move through frames
@app.callback(
    Output("animateInterval","disabled"),
    Input("dashPlay", "n_clicks"),
    State("animateInterval","disabled"),
)
def play(n_clicks, disabled):
    return not disabled
    
@app.callback(
    Output("dashSlider", "value"),
    Input("animateInterval", "n_intervals"),
    State("dashSlider", "value")
)
def doAnimate(i, frame):
    if frame < (len(frames)-1): 
        frame += 1
        # time.sleep(1)
    else:
        frame = 0
    return frame

            # sliders=[{"currentvalue": {"prefix": "Year=", "font": {'size': 20}}}]

# Run app and display result inline in the notebook
app.run_server(mode="inline")



fig.update_layout(
    # title="Plot Title",
    autosize=False,
    width=1800,
    height=600,
)

st.plotly_chart(fig)

# st.dataframe(df)
