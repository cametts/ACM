from split_csv_search import search 
from dash import Input, Output, State, dash_table

def register_long_callbacks(app, long_callback_manager):
    @app.long_callback(
        output=Output(component_id='output', component_property='children'),
        inputs=[
            Input('load_button', 'n_clicks'),
            State(component_id='search_term', component_property='value'),
        ],
        manager=long_callback_manager,
        running = [
            (Output('load_button', 'disabled'), True, False),
            (
                Output('progress_bar', 'style'),
                {'visibility' : 'visible'},
                {'visibility' : 'hidden'},
            )
        ],
        prevent_initial_call = True,
    )

    def update_output_div(n_clicks, input_value):
        #df = pd.DataFrame({'Col1' : input_value}, index=[0])
        df = search(input_value)
        data = dash_table.DataTable(df.to_dict('records'),
            [{"name": i, "id": i} for i in df.columns], 
            id='tbl',
            export_format='xlsx',
            export_headers='display')
        return data