import pandas as pd

dict_names = {
  
    "Name": [
    
      "David Murphy",
      "John Doyle",
    
  ],
  "Age": [23,43],
  "Sex": ["male", "male"]
                  
}
  
df = pd.DataFrame(dict_names)
  
print(df)
print(df.describe())