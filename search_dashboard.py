from dash import Dash, html, dcc, Input, Output, State, dash_table
from dash.long_callback import DiskcacheLongCallbackManager
import diskcache
import os
import sys
from callbacks import register_long_callbacks
from split_csv_search import search 


#if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
#    os.chdir(sys._MEIPASS)

## Diskcache
cache = diskcache.Cache("./cache")
long_callback_manager = DiskcacheLongCallbackManager(cache)

app = Dash() #, long_callback_manager=long_callback_manager)

app.layout = html.Div(children=[
    html.H1(children='ACM Searchable Database'),

    html.Div(children='''
        A searchable database of Arabic-language documents from the ACM repository.
    '''),

    html.Div(children=[
        html.Br(),
        html.Br(),
        dcc.Input(id='search_term', value='', type='text'),
        html.Button('Search', id='load_button', n_clicks=0),
    ]),
    html.Div(children=[
        html.Br(),
        html.Progress(id='progress_bar'),
    ]),
    html.Br(),
    html.Div(id='output'),
])

register_long_callbacks(app, long_callback_manager)

# #Load the counts
# @app.callback(Output(component_id='counts', component_property='data'), Input('load_button', 'n_clicks'))
# def load_data(n_clicks):
#     counts = load_counts()
#     return counts

def main():
    app.run_server(debug=False)


if __name__ == '__main__':
    main()
    