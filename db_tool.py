import psycopg2

class ShortLinkDB:
    def __init__(self, host, port, dbname, user, password):
        self.host = host
        self.port = port
        self.dbname = dbname
        self.user = user
        self.password = password

    
    def get_provisions(self, num_rows) -> list[tuple]:
        conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                dbname=self.dbname,
                user=self.user,
                password=self.password
            )
        cur = conn.cursor()
        cur.execute("SELECT provision FROM provisioning LIMIT {}".format(str(num_rows)))
        rows = cur.fetchall()
        conn.close()
        return rows

    def insert_provision_bulk(self, data_list):
        try:
            # Connect to the database
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
            sql = "INSERT INTO provisioning (provision, is_used, used_time) VALUES (%s, %s, %s)"

            # Execute the INSERT statement for each item in the data_list
            cur.executemany(sql, data_list)

            # Commit the changes to the database
            conn.commit()

            # Close the cursor and connection
            cur.close()
            conn.close()
        except:
            raise

    def create_link(self, transaction_id, target_url, request_time, requesters_ip, requesters_browser, requesters_device, short_url):
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
            insert_query = "INSERT INTO url_link (transaction_id, target_url, request_time, requesters_ip, requesters_browser, requesters_device, short_url) VALUES (%s, %s, %s, %s, %s, %s, %s)"


            # Execute the INSERT statement
            cur.execute(insert_query, (transaction_id, target_url, request_time, requesters_ip, requesters_browser, requesters_device))


            # Commit the changes to the database
            conn.commit()

            # Close the cursor and connection
            cur.close()
            conn.close()
        except:
            raise


    