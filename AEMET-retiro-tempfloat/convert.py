import pandas as pd

for ano in range(1920, 2021):
    print("Converting: %s" % ano)
    df = pd.read_json('datos-retiro-%s.json' % ano)
    df['tmed'] = df['tmed'].str.replace(',', '.').astype(float)
    df['tmin'] = df['tmin'].str.replace(',', '.').astype(float)
    df['tmax'] = df['tmax'].str.replace(',', '.').astype(float)

    df.to_json('datos-retiro-%s.json' % ano, orient='records')
