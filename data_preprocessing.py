import pandas as pd

DIR_DATA = 'data/NYPD_Shooting_Incident_Data__Historic_.csv'

pd.options.mode.chained_assignment = None

def data_preprocessing():
    df = pd.read_csv(DIR_DATA, index_col=0)

    df['TIME'] = df['OCCUR_DATE'] + ' ' + df['OCCUR_TIME']
    df['TIME'] = pd.to_datetime(df['TIME'])

    df['JURISDICTION_CODE'] = pd.to_numeric(df['JURISDICTION_CODE'])

    age_levels = pd.Series([
      "<18", "18-24", "25-44", "45-64", "65+"
    ])
    df['PERP_AGE_GROUP'] = pd.Categorical(df['PERP_AGE_GROUP'], categories=age_levels)
    df['VIC_AGE_GROUP'] = pd.Categorical(df['VIC_AGE_GROUP'], categories=age_levels)

    df = df.dropna(subset=['PERP_AGE_GROUP', 'VIC_AGE_GROUP'])

    '''
    columns_to_drop = [
      ''
    ]
    for column in columns_to_drop:
        df.drop(column, axis = 1, inplace=True)
    '''

    return df