import pandas as pd

animals = ["Lions", "Tigers", "Bears", "Dogs", "Cats"] # List Collection

df = pd.DataFrame(animals) # Convert our list to a format to which Pandas can use

print(df)

df.to_csv("output.csv") # This give us our output
