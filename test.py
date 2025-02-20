#File testing to see if Dash webpage will display anything
import dash 
from dash import dcc, html

app = dash.Dash(__name__) #initialize app 

#test layout
app.layout = html.Div
([

    html.H1("Dash is working.", style = {"textAlign": "centered", "color": "blue"}),

    dcc.Graph(id = "stock-graph") #tester graph
])

if __name__ == '__main__':
    app.run_server(debug = False)