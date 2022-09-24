import pandas as pd


def filter_columns(data):
    filtered_data = data[['ciudad_municipio_nom', 'departamento_nom', 'edad',
                          'fuente_tipo_contagio', 'estado']]

    filtered_data.columns = ['CIUDAD DE UBICACIÓN', 'DEPARTAMENTO', 'EDAD',
                             'TIPO DE CONTAGIO', 'ESTADO']
    pd.options.display.max_rows = None
    pd.options.display.max_columns = None
    return filtered_data
