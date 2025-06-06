# Used to connect to Oracle Database
import oracledb 
 # Used for handling CSV files and dataframes
import pandas as pd 

# ----------------------------
# Function to extract data from a CSV file
# ----------------------------

def extract_from_csv(file_path): 
    """
    Extracts data from a CSV file using pandas.

    Parameters:
        file_path (str): Path to the CSV file

    Returns:
        pd.DataFrame: DataFrame containing the CSV data
    """
    try:
    
        df = pd.read_csv(file_path)
        print(f'[csv] Extracted {len(df)} records from {file_path}')
        
      
        return df 
    except Exception as e :
        print(f'[csv] Error reading {file_path}: {e}')
        return pd.DataFrame()
    
    
# ----------------------------
# Function to extract data from Oracle DB
# ----------------------------


def extract_from_oracle (user, password , host, port , service_name , query) :
    
    """
    Connects to an Oracle database and runs a SQL query to extract data.

    Parameters:
        user (str): Oracle username
        password (str): Oracle password
        host (str): Hostname or IP of Oracle DB
        port (int or str): Listener port (typically 1521)
        service_name (str): Pluggable DB or service name (e.g., 'testpdb1')
        query (str): SQL SELECT query to execute

    Returns:
        pd.DataFrame: Query results as a DataFrame
    """
    
    try:
        # Establish connection to Oracle DB
        connection = oracledb.connect(
            user = user ,
            password = password,
        # Create connection string for Oracle in Thin mode

            dsn = f'{host}:{port}/{service_name}'
        
            )
        # Execute query and load result into DataFrame
        df = pd.read_sql(query,con =connection)
        print(f"[Oracle] Extracted {len(df)} records from Oracle DB")
        print('oracle data',df)
        connection.close()   #close the connection 
        return df 

    except Exception as e :
        print(f"[Oracle] Error: {e}")   # log connection/query errors 
        return pd.DataFrame() # return an empty dataframe on failure 
    
    