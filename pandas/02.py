
from turtle import pd
import pandas as pd
# Filter in pandas
data={
    "Name": ["Ali", "Sara", "Ahmed", "Lina", "Omar"],
    "Age": [25, 30, 22, 28, 35],
    "City": ["Karachi", "Lahore", "Islamabad", "Karachi", "Lahore"]
}
df = pd.DataFrame(data)
# Filter rows where Age > 25
filtered_df = df[df["Age"] > 25]
print("filtered_df",filtered_df)

# age > 25 and city is Karachi
filtered_df2 = df[(df["Age"] > 25) & (df["City"] == "Karachi")]
print("filtered_df2",filtered_df2)
# age < 30 or city is Lahore
filtered_df3 = df[(df["Age"] < 30) | (df["City"] == "Lahore")]
print("filtered_df3",filtered_df3)

# Select specific columns after filtering
filtered_df4 = df.loc[df["Age"] > 25, ["Name", "City"]]
print("filtered_df4",filtered_df4)

# Reset index after filtering
filtered_df5 = df[df["Age"] > 25].reset_index(drop=True)
print("filtered_df5",filtered_df5)


# df.info()
