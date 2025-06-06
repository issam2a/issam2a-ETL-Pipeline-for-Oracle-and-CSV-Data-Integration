import oracledb 
import pandas as pd 



def load_cleaned_data_to_csv(df):
    df=df.to_csv('data/teleomCustomerChrum.csv', index=False)
    
    return df

def load_cleaned_data_oracle(df ,user, password , host, port , service_name) :
    try :
        connection = oracledb.connect(
            user= user ,
            password = password,
            dsn = f'{host}:{port}/{service_name}'
        )
        cursor= connection.cursor()
        
        # Prepare data for insertion
        data_to_insert = list(df.itertuples(index=False, name=None))
        
        insert_sql = """
            insert into report (customerID,Gender,SeniorCitizen,Partner,Dependents,Tenure,PhoneService,
            MultipleLines,InternetService,OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,StreamingTV
            ,StreamingMovies,Contract,PaperlessBilling,PaymentMethod,MonthlyCharges,TotalCharges,Churn)
            
            VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13, :14, :15, :16, :17, :18, :19, :20, :21)
        
            """
        cursor.executemany(insert_sql , data_to_insert)
        
        connection.commit()
        print("✅ Data successfully inserted into usage_report.")
        
    except oracledb.Error as e :
        print("❌ Error inserting data:", e)
    finally:
        # Clean up
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()