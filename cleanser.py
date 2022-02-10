import pandas as pd
import os

print(os.path.getsize("Downloads/archive/US_Accidents_Dec20_updated.csv"))
df = pd.read_csv(r'Downloads/archive/US_Accidents_Dec20_updated.csv')
df.dropna(inplace = True)
df.drop(inplace = True, columns = ["ID", "Start_Time", "End_Time", "Description", "Number", "Street", "County", "Zipcode", "Country", "Timezone", "Airport_Code", "Weather_Timestamp"]) # remove all unwanteds

mnwd = 0
mxwd = 0
# change categorical to numeric
for col_name in df.columns:
    df[col_name].replace(True, 1, inplace = True)
    df[col_name].replace(False, 0, inplace = True)
    if(df[col_name].dtype == 'object' and col_name not in ["City", "State"]): # change all objects and T/F as their cat. codes IF it's not a City or State
        df[col_name]= df[col_name].astype('category')
        df[col_name] = df[col_name].cat.codes

mxwd = max(df["Wind_Direction"])
mnwd = min(df["Wind_Direction"])

df.to_csv("Downloads/archive/modified/US_Accidents_complete.csv", index = False)
print(os.path.getsize("Downloads/archive/modified/US_Accidents_complete.csv"))
print(f"Min Wind_Dir: {mnwd}\nMax Wind_Dir: {mxwd}")
print("\nDone")