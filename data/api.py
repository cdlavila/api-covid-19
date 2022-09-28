import pandas as pd
from sodapy import Socrata


def get_data(registers_limit, departament_name):
    client = Socrata("www.datos.gov.co", None)
    results = client.get("gt2j-8ykr", limit=registers_limit, departamento_nom=departament_name)
    # Convert to pandas DataFrame
    results_df = pd.DataFrame.from_records(results)
    return results_df
