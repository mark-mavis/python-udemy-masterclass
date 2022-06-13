
import pandas as pd

data_frame = pd.DataFrame(
    {
        "Name":[
            "Braund, Mr Owen Harris", 
            "Allen, Mr. William Henry", 
            "Bonnell, Miss. Elizabeth"
            ],
        "Age": [22, 35, 58],
        "Sex": [
            "male", 
            "male", 
            "female"
            ],
    }
)

print(data_frame)

age_group = data_frame["Age"]
print(age_group)

#Creating Series from scratch
ages = pd.Series([49, 20, 59], name="Age")
print(ages)

print(data_frame.describe())
