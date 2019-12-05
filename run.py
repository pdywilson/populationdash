import pandas as pd
import collections

# df2 = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
df = pd.read_csv('data/data1.csv')


print(df.loc[df['Country Name'].isin(['Canada','United States'])])

countries_selected = ['Canada']

df_filtered = df.loc[df['Country Name'].isin(countries_selected)]

print(df_filtered)

data = []

for index, row in df.iterrows():
  country = row[0]
  for i, elt in enumerate(row[4:]):
    year = i + 1960
    data.append({'name': country, 'mode': 'lines+markers', 'x': year, 'y': elt})




# filtered.to_dict('records')

# for row in df:
#   print(row)
#   print(row['Country Name'])
#   a = aggregation[row['Country Name']]

  # a['name'] = row['Country Name']
  # a['mode'] = 'lines+markers'

  # a['x'].append(row['year'])
  # a['y'].append(row[field])


# a['name'] = row['Country Name']
# a['mode'] = 'lines+markers'

# a['x'].append(row['year'])
# a['y'].append(row[field])

