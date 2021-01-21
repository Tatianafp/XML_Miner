from extract_xml import extrair_anotacoes
import base64
from base64 import b64decode
import datetime
import io
import tempfile


from urllib.parse import quote as urlquote
import urllib
import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_table

#import flask

import pandas as pd

correct_names = {
        'Ato_Abono_Permanencia': 'Abono de Permanência',
        'Ato_Aposentadoria': 'Aposentadoria',
        'Ato_Cessao': 'Cessão',
        'Ato_Exoneracao_Comissionado': 'Exoneração - Comissionado',
        'Ato_Exoneracao_Efetivo': 'Exoneração - Efetivo',
        'Ato_Nomeacao_Comissionado': 'Nomeação - Comissionado',
        'Ato_Nomeacao_Efetivo': 'Nomeação - Efetivo',
        'Ato_Retificacao_Comissionado': 'Retificação - Comissionado',
        'Ato_Retificacao_Efetivo': 'Retificação - Efetivo',
        'Ato_Reversao': 'Reversão',
        'Ato_Substituicao': 'Substituição',
        'Ato_Tornado_Sem_Efeito_Apo': 'Tornar sem efeito - Aposentadoria',
        'Ato_Tornado_Sem_Efeito_Exo_Nom': 'Tornar sem efeito - Exoneração e Nomeação',
        'todos_atos': 'Todos os atos'
}

def create_layout(app):
    return html.Div([
    html.Link(href="https://fonts.googleapis.com/css2?family=Raleway&display=swap", rel="stylesheet"),
    html.Div([
        html.Div([
            html.H1('KnEDLe Miner', className='card-title'),
            html.H2('Extrator de anotações feitas no NidoTat', className='card-subtitle'),
            html.H2('e armazenadas em arquivos XML', className='card-subtitle'),
            dcc.Upload(
                id='upload-data',
                children=html.Div([
                    html.Img(src='assets/img/file.svg', className='card-logo-pdf'),
                    html.H3('Arraste e solte o XML aqui', className='text-pdf'),
                    html.Button('Selecione no seu Computador', className='choose-button')
                ], className='card-pdf-box'),
                # Allow multiple files to be uploaded
                multiple=True
            ),
            html.Div(className="options-extrair",children = [
                dcc.Dropdown(id='modo-extracao', className ="input",
                    searchable=False,
                    clearable=False,
                    options=[
                        {"label": "todos os atos juntos","value": "junto",},
                        {"label": "separado por tipo de ato","value": "separado",},
                        ],
                    placeholder="junto",
                    value = "junto", 
                ),
                html.Button(children=["extrair atos"], className="Button", id="extrair-button", n_clicks=0),
            ]),
        ], className='card'),
        
        html.Div(id='output-data-upload'),], className='row'),
    #html.Img(src='assets/img/undraw_reviewed_docs_neeb 1.svg', className='background-img'),
])

def parse_contents(contents, filename, date):
    global df_dict
    content_type, content_string = contents.split(',')

    content = b64decode(content_string, validate=True)
    try:
        if 'xml' in filename:
            temp_xml = open('tmp_file.xml', 'wb+')
            temp_xml.write(content)
            temp_xml.close()

            acts_dfs = extrair_anotacoes('tmp_file.xml')

    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    list_of_tables = []
    for act_name in acts_dfs:
        df = acts_dfs[act_name]
        df.to_csv("./csv/" + act_name + ".csv", index=False)
        download_button = html.Div([
            html.A(id='download', children="Download CSV", href=f"./csv/{act_name}.csv")
        ]) if df.shape[0] > 0 else None 
        list_of_tables.append(\
            html.Div([
                html.H2(correct_names[act_name], className='text-act'),
                html.H4("Ocorrências no PDF: " + str(df.shape[0]), className='text-ocu'),

                dash_table.DataTable(
                    data=df.to_dict('records'),
                    columns=[{'name': i, 'id': i} for i in df.columns],
                    style_cell={
                        'overflow': 'hidden',
                        'textOverflow': 'ellipsis',
                        'maxWidth': '50px',
                        'height':'auto'
                    }, 
                    style_table={
                        'maxHeight': '700px',
                        'overflowY': 'auto',
                        'overflowX': 'auto',
                        'marginBottom': '40px'
                    }
                ),
                download_button,
            ], className='card-csv')\
        )

    return html.Div(list_of_tables)

def organize_content(list_of_contents, list_of_names, list_of_dates,xmls):
    i = 0
    for contents, filename, date in zip(list_of_contents, list_of_names, list_of_dates):
        content_type, content_string = contents.split(',')

        content = b64decode(content_string, validate=True)
        try:
            if 'xml' in filename:
                temp_xml = tempfile.mkstemp(prefix=str(i), suffix='.xml')
                #
                temp_file = open(temp_xml[0], 'wb+')
                temp_file.write(content)
                #temp_xml.close()

                xmls.append(temp_xml[1])
                i += 1

        except Exception as e:
            print(e)
            return html.Div([
                'There was an error processing this file.'
            ])

def file_download_link(filename):
    """Create a Plotly Dash 'A' element that downloads a file from the app."""
    location = "/download/{}".format(urlquote(filename))
    return html.A(id='download', children="Download CSV", href=location)

def return_tables(xmls,modo):
    acts_dfs = extrair_anotacoes(xmls,modo)

    #close_files(xmls)

    list_of_tables = []
    for act_name in acts_dfs:
        df = acts_dfs[act_name]
        
        if df.shape[0] > 0 :
            '''
            csv_string = df.to_csv("./csv/" + act_name + ".csv",index=False, encoding='utf-8')
            csv_string = "data:text/csv;charset=utf-8," + \
                urllib.parse.quote(csv_string)

            '''
            dff = df
            csv_string = dff.to_csv(index=False, encoding='utf-8')
            csv_string = "data:text/csv;charset=utf-8," + \
                urllib.parse.quote(csv_string)

            download_button = html.A(
                children=['Download CSV'],
                id='download-link',
                download="annotations_teste.csv",
                href=csv_string,
                target="_blank")
        else:
            download_button = None 
        list_of_tables.append(\
            html.Div([
                html.H2(correct_names[act_name], className='text-act'),
                html.H4("Ocorrências no PDF: " + str(df.shape[0]), className='text-ocu'),

                dash_table.DataTable(
                    data=df.to_dict('records'),
                    columns=[{'name': i, 'id': i} for i in df.columns],
                    style_cell={
                        'overflow': 'hidden',
                        'textOverflow': 'ellipsis',
                        'maxWidth': '150px',
                        'height':'auto'
                    }, 
                    style_table={
                        'maxHeight': '700px',
                        'overflowY': 'auto',
                        'overflowX': 'auto',
                        'marginBottom': '40px'
                    }
                ),
                download_button,
            ], className='card-csv')\
        )

    return html.Div(list_of_tables)


def main_callbacks(app):
    @app.callback(
        Output('output-data-upload', 'children'),
        [
            Input('extrair-button','n_clicks')
        ],
        [
            State('modo-extracao','value'),
            State('upload-data', 'contents'),
            State('upload-data', 'filename'),
            State('upload-data', 'last_modified')
        ])
    def update_output(extrair,modo,list_of_contents, list_of_names, list_of_dates):
        if extrair != 0 and (list_of_contents is not None):
            xmls = []
            organize_content(list_of_contents, list_of_names, list_of_dates,xmls)

            children = [return_tables(xmls,modo)]
            return children

