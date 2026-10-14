import pandas as pd 

data={

    "Name":["Pratik","Rishabh","Aadarsh","Pratik"],
    "Age":[23,21,20,23],
    "City":["Surat","Mumbai","MP","Surat"]
}
print("Original set")
df=pd.DataFrame(data)
print(df)

print("\nInformation of set")
df.info()

df=df.drop_duplicates()

df["Name"]=df["Name"].str.strip().str.title()
df["City"]=df["City"].str.strip().str.title()

print("\ndata preproccessed data set: ")
print(df)
df.to_csv("preproccessed_data.csv",index=False)

print("\npreproccessed data save successfully")

