import pandas as pd

# Create a sample dataframe
data = {'int_col': [1, 2, 3, 4, 5],
        'float_col': [1.1, 2.2, 3.3, 4.4, 5.5],
        'string_col': ['a', 'b', 'c', 'd', 'e']}
df = pd.DataFrame(data)

# Dynamically choose the lowest integer type
int_cols = df.select_dtypes(include=['int']).columns
df[int_cols] = df[int_cols].apply(pd.to_numeric, downcast='integer')

# Dynamically choose the lowest floating-point type
float_cols = df.select_dtypes(include=['float']).columns
df[float_cols] = df[float_cols].apply(pd.to_numeric, downcast='float')

# Print the memory usage of the dataframe
print(df.memory_usage(deep=True))

# Output the optimized dataframe
print(df)
