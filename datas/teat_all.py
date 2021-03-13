import pandas as pd

df = pd.DataFrame({'temp_c': [17.0, 25.0]},index = ['Portland', 'Berkeley'])
print(df)
df = df.assign(D=5)
print(df)
