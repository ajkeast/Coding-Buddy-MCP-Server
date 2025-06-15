import os
from dotenv import load_dotenv
from typing import List, Optional, Dict, Any
from contextlib import contextmanager
import mysql.connector
from mysql.connector import Error

# Load environment variables
load_dotenv()

class SQLTools:
    def __init__(self):
        """Initialize the SQLTools class with database connection parameters from environment variables."""
        self.host = os.getenv('SQL_HOST', 'localhost')
        self.user = os.getenv('SQL_USER')
        self.password = os.getenv('SQL_PASSWORD')
        self.database = os.getenv('SQL_DATABASE')

    @contextmanager
    def get_connection(self):
        """Context manager for database connections.
        
        Yields:
            mysql.connector.connection: Database connection object
            
        Raises:
            Error: If connection to the database fails
        """
        connection = None
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            yield connection
        except Error as e:
            print(f"Error connecting to MySQL database: {e}")
            raise
        finally:
            if connection and connection.is_connected():
                connection.close()

    def list_databases(self) -> str:
        """List all databases in the MySQL server.
        
        Returns:
            str: A formatted string containing all database names, one per line
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SHOW DATABASES")
            databases = [db[0] for db in cursor.fetchall()]
            return "\n".join(databases)

    def list_tables(self) -> str:
        """List all tables in the current database.
        
        Returns:
            str: A formatted string containing all table names, one per line
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SHOW TABLES")
            tables = [table[0] for table in cursor.fetchall()]
            return "\n".join(tables)

    def execute_query(self, query: str) -> str:
        """Execute a SQL query and return the results as a formatted string.
        
        Args:
            query (str): The SQL query to execute
            
        Returns:
            str: A formatted string representation of the query results
                  Each row is on a new line, with columns separated by tabs
                  
        Raises:
            Error: If the query execution fails
        """
        with self.get_connection() as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(query)
            results = cursor.fetchall()
            
            if not results:
                return "No results found."
                
            # Get column names from the first result
            columns = list(results[0].keys())
            
            # Create header
            output = "\t".join(columns) + "\n"
            
            # Add rows
            for row in results:
                output += "\t".join(str(row[col]) for col in columns) + "\n"
                
            return output

    def get_table_schema(self, table_name: str) -> str:
        """Get the schema information for a specific table.
        
        Args:
            table_name (str): Name of the table to get schema for
            
        Returns:
            str: A formatted string containing the table schema information
                 Each column's information is on a new line
                 
        Raises:
            Error: If the table doesn't exist or schema retrieval fails
        """
        with self.get_connection() as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(f"DESCRIBE {table_name}")
            schema = cursor.fetchall()
            
            if not schema:
                return f"No schema found for table '{table_name}'"
                
            # Format each column's information
            output = f"Schema for table '{table_name}':\n"
            for column in schema:
                output += f"Column: {column['Field']}\n"
                output += f"Type: {column['Type']}\n"
                output += f"Null: {column['Null']}\n"
                output += f"Key: {column['Key']}\n"
                output += f"Default: {column['Default']}\n"
                output += f"Extra: {column['Extra']}\n\n"
                
            return output

# 