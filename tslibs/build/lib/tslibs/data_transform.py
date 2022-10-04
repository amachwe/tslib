import pandas as pd
import libs.data_client as dc

def currency_to_dataframe(sym):
    data = dc.get_data_single(sym)
    return pd.DataFrame(data[0])