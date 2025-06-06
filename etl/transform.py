import pandas as pd 

def clean_oracle_data(df):
    
    df.columns = [col.lower() for col in df.columns ]
    
    print(df.columns)
    # Remove rows where any of the key fields are missing
    df = df.dropna(subset=['customerid' ,'churn'])

    
    
    df= df.drop_duplicates('customerid' ,keep = 'last')

    # Convert 'TotalCharges' to numeric (handle strings like 'note' by coercing to NaN, then fill with 0.0)
    df['totalcharges'] = pd.to_numeric(df['totalcharges'], errors='coerce').fillna(0.0).astype(float)

    # Same cleaning for 'MonthlyCharges' column
    df['monthlycharges'] = pd.to_numeric(df['monthlycharges'], errors='coerce').fillna(0.0).astype(float)

    df = df.where(pd.notnull(df), None)


    
     # Log and drop negative-value rows
    numerical_col = df.select_dtypes(include = 'number').columns
    
    # Rows with any negative values
    invalid_rows = df[(df[numerical_col] < 0).any(axis=1)]
    
    
    #log  invalid_rows into csv file 
    if not invalid_rows.empty :
        print("⚠️ Found negative values:")
        print(invalid_rows)
        invalid_rows.to_csv('logs/invalid_usage_rows.csv')
    # keep only the valid rows 
    df=df[(df[numerical_col] >= 0 ).all(axis =1)]
    
   
    # Return the cleaned DataFrame
    return df





def clean_user_info(df):
    
    print(df.columns.tolist())
    df.columns = [col.lower() for col in df.columns ]
    print(df.columns.tolist())
    
    #droping rows with customer_id null values 
    df=df.dropna(subset=['customerid'])
   
    # droping the duplicated values in the customer_id and keeping one row 
    df=df.drop_duplicates('customerid', keep= 'last')
    
    # Clean and convert 'data_usage_gb' column to float
    df['tenure'] = pd.to_numeric(df['tenure'], errors='coerce').fillna(0).astype(int)
    

    # Log and drop negative-value rows
    numerical_col = df.select_dtypes(include = 'number').columns
    
    # Rows with any negative values
    invalid_rows = df[(df[numerical_col] < 0).any(axis=1)]
    #filling the null values with  0
    df[numerical_col] = df[numerical_col].fillna(0)
    
    #log  invalid_rows into csv file 
    if not invalid_rows.empty :
        print("⚠️ Found negative values:")
        print(invalid_rows)
        invalid_rows.to_csv('logs/invalid_customer_info_rows.csv')
    # keep only the valid rows 
    df=df[(df[numerical_col] >= 0 ).all(axis =1)]
    
    return df
    
    
    
def join_usage_and_customer_info(usage_df, customer_info):
    
    
   
    
    # Merge usage with customer_info
    merged_df = pd.merge(
        customer_info ,
        usage_df,
        on='customerid',
        how='right'
    )
    
    
    
    
    print(merged_df.isnull().sum())




    return merged_df


    