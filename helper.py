# Cast attributes to datetime stamp 
def to_datetime(df, nasa=False, space=False):
    if nasa:
        df.Start_Datetime = pd.to_datetime(df.Start_Datetime)
        df.End_Datetime = pd.to_datetime(df.End_Datetime)
        df.CME_Time = pd.to_datetime(df.CME_Time)
    if space:
        df.Start_time = pd.to_datetime(df.Start_time)
        df.Max_time = pd.to_datetime(df.Max_time)
        df.End_time = pd.to_datetime(df.End_time)
    
    return df

def seperateImportance(df, col_name='importance', numbers=True, letters=True):
    if letters:
        df['importance_1'] = df[col_name].str.slice(start=0, stop=1)
    if numbers:
        df['importance_2'] = df[col_name].str.slice(start=1).astype('float')
    return df


