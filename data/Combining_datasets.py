directory = r'files'
df_list = []

for i in os.listdir(directory):
    if i.endswith(".csv"):
        filepath = os.path.join(directory, i)
        df = pd.read_csv(filepath)
        df_list.append(df)
        
combined_df = pd.concat(df_list)
combined_df.to_csv('twitter_data.csv', index=False)
