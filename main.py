from etl.extract import extract_from_csv, extract_from_oracle
from etl.transform import clean_user_info,clean_oracle_data, join_usage_and_customer_info
from etl.load import load_cleaned_data_oracle, load_cleaned_data_to_csv
import pandas as pd 

user='etl_user'
password= 'etl_pass'
host='localhost'
port='1521'
service_name = 'testpdb1'
query = "select * from service_usage"



customer_info = extract_from_csv("data/customer_info.csv")



oracle_data= extract_from_oracle(
    user= user ,
    password= password,
    host= host,
    port= port,
    service_name= service_name,
    query= query 
)

usage_clean = clean_oracle_data(oracle_data)
user_info_clean = clean_user_info(customer_info)
final_df = join_usage_and_customer_info(usage_clean,user_info_clean)

load_cleaned_data_to_csv(final_df)


load_cleaned_data_oracle(
    df= final_df,
    user= user,
    password= password ,
    host= host,
    port= port,
    service_name= service_name 
)



print(user_info_clean.isnull().sum())