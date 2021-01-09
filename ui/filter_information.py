import pandas as pd


def filter_columns(data):
    filtered_data = data[['ciudad_municipio_nom', 'ciudad_municipio_nom', 'edad',
                          'fuente_tipo_contagio', 'estado', 'pais_viajo_1_nom']]

    filtered_data.columns = ['CIUDAD', 'CIUDAD DE UBICACIÓN', 'EDAD',
                             'TIPO DE CONTAGIO', 'ESTADO', 'PAÍS DE PROCEDENCIA']
    pd.options.display.max_rows = None
    pd.options.display.max_columns = None
    return filtered_data
