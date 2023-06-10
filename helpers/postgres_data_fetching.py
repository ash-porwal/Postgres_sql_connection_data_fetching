import psycopg2

class PostgresClient:
    def __init__(self, hostname, port, database, username, password):
        self.hostname = hostname
        self.port = port
        self.db = database
        self.user = username
        self.psswd = password
        self.cur = self.connection()

    def connection(self):
        try:
            self.conn = psycopg2.connect(
                host=self.hostname,
                port=self.port,
                dbname= self.db,
                user=self.user,
                password=self.psswd
                )
            
            #creating cursor
            postgres_cur = self.conn.cursor()
        except Exception as e:
            print(e)
        return postgres_cur


    def extract_data(self):
        try:

            # First lisitng all the public tables inside database
            """
            list all the tables inside a PostgreSQL database using SQL queries. In PostgreSQL, you can query the pg_catalog.pg_tables system catalog view to retrieve information about tables in a database.
            This query selects the tablename column from the pg_catalog.pg_tables view and filters for tables in the 'public' schema. The 'public' schema is the default schema for tables in PostgreSQL unless explicitly specified.
            """
            table_query = '''
                SELECT tablename
                FROM pg_catalog.pg_tables
                WHERE schemaname = 'public'
            '''

            #executing the query
            self.cur.execute(query=table_query)

            tables = self.cur.fetchall()

            # Return list of tables - type
            print("tables object type : ", type(tables))

            for table in tables:

                #here table type will be a tuple, so we need to get table name through indexing
                # print(table[0])
            
                #Fetching all data inside table
                all_data_query = f'''
                SELECT * FROM {table[0]}
                '''

                self.cur.execute(query=all_data_query)

                #fetching and printing the results
                all_rows = self.cur.fetchall()

                print()
                print("********")
                print(f"Printing data for table - {table[0]}")
                print("********")
                print()

                for row in all_rows:
                    print(row)
            
            #closing connection and connection
            self.cur.close()
            self.conn.close()
            print("Connection closed successfully")
        except Exception as e:
            print(e)