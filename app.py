import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import pandas as pd

########### Define your variables ######

# here's the list of possible columns to choose from.
#list_of_columns =['city', 'state', 'killed', 'injured', 'date', 'type', 'time']

# mycolumn='state'
# #myheading1 = f"Wow! That's a lot of {mycolumn}!"
# mygraphtitle = 'School Shootings over a 10 year period'
# mycolorscale = 'Reds' # Note: The error message will list possible color scales.
# mycolorbartitle = "Hundreds"
# tabtitle = 'Something has to change'
# sourceurl = 'https://plot.ly/python/choropleth-maps/'
# githublink = 'https://github.com/austinlasseter/dash-map-usa-agriculture'


########## Set up the chart


df = pd.read_csv('./assets/CNN_School_Shooting_File_7_26_2019.csv')

for col in df.columns:
    df[col] = df[col].astype(str)

df['text'] = df['date'] + 'time' + df['time'] + '<br>' + \
    'City' + df['city'] + 'State' + df['state'] + '<br>' + \
    'Deaths' + df['killed'] + 'Injuries' + df['injured'] + '<br>' + \
    'School Type' + df['type']

fig = go.Figure(data=go.Choropleth(
    locations=df['CDCODE'],
    z=df['victims'].astype(float),
    locationmode='USA-states',
    colorscale='Reds',
    autocolorscale=False,
    text=df['text'], # hover text
    marker_line_color='white', # line markers between states
    colorbar_title="Hundreds"
))

fig.update_layout(
    title_text='2011 US Agriculture Exports by State<br>(Hover for breakdown)',
    geo = dict(
        scope='usa',
        projection=go.layout.geo.Projection(type = 'albers usa'),
        showlakes=True, # lakes
        lakecolor='rgb(255, 255, 255)'),
)

#fig.show()


app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run_server(debug=True, use_reloader=False)  


########### Initiate the app
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# server = app.server
# app.title=tabtitle

########### Set up the layout

# app.layout = html.Div(children=[
#     html.H1(myheading1),
#     dcc.Graph(
#         id='figure-1',
#         figure=fig
#     ),
#     html.A('Code on Github', href=githublink),
#     html.Br(),
#     html.A("Data Source", href=sourceurl),
#     ]
# )

############ Deploy
if __name__ == '__main__':
    app.run_server()
