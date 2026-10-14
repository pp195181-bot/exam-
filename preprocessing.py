import pandas as x

df=x.DataFrame ({
    "post":["Good product"," Bad services","Good product",None],
    "like":["10","5","10","3"]
})

print(df.info())

df=df.drop_duplicates()
df["post"]=df["post"].fillna("unknown")
df["like"]= x.to_numeric(df["like"],errors="coerce")
df["like"]=df["like"].fillna(0)

df.to_csv("proccessed_social_data.csv",index=False)

print(df)
print("processed file saved")

