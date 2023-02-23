import psycopg2

class PandoraHistory:
    def __init__(self, host, port, dbname, user, password):
        self.host = host
        self.port = port
        self.dbname = dbname
        self.user = user
        self.password = password

    def insert_result(self, transaction_id, target_url, request_time, requesters_ip, requesters_browser, requesters_device, short_url):
        # Connect to the database
        try:
            conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                dbname=self.dbname,
                user=self.user,
                password=self.password
            )

            # Create a cursor object
            cur = conn.cursor()

            # Construct the INSERT statement
            insert_query = "INSERT INTO short_link (transaction_id, target_url, request_time, requesters_ip, requesters_browser, requesters_device, short_url) VALUES (%s, %s, %s, %s, %s, %s, %s)"


            # Execute the INSERT statement
            cur.execute(insert_query, (transaction_id, target_url, request_time, requesters_ip, requesters_browser, requesters_device))


            # Commit the changes to the database
            conn.commit()

            # Close the cursor and connection
            cur.close()
            conn.close()
        except:
            raise


    