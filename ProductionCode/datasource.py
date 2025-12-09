import psycopg2

import ProductionCode.psqlConfig as config

class DataSource:
    """Class responsible for connecting to the PostgreSQL database and executing queries."""

    def __init__(self):
        """Constructor that initiates a connection to the database."""
        self.connection = self.connect()

    def connect(self):
        """
        Connecting to the PostgreSQL database using credentials from psqlConfig.py.
        
        Returns:
            connection (psycopg2.connection): The database connection object.
        """
        try:
            connection = psycopg2.connect(
                database=config.database,
                user=config.user,
                password=config.password,
                host="localhost"
            )
        except Exception as e:
            print("Connection error:", e)
            exit()
        return connection

    def getSESByCounty(self, county):
        '''
        Arguments: self, county
        Return value: data of the SES from a county
        Purpose: Get data from our data table and return all of the SES from a certain county
        '''
        try:
            # set up a cursor
            cursor = self.connection.cursor()

            # make the query using %s as a placeholder for the variable
            query = "SELECT DISTINCT ses FROM ses_table WHERE countyname = %s;"

            # executing the query and saying that the type variable 
            # should be placed where %s was, the trailing comma is important!
            cursor.execute(query, (county,))
            return cursor.fetchall()

        except Exception as e:
            print ("Something went wrong when executing the query: ", e)
            return None

    def getScoresByCounty(self, county):
        '''
        Arguments: self, county
        Return value: data of the scores from a county
        Purpose: Get data from our data table and return all of the scores from a certain county
        '''
        try:
            # set up a cursor
            cursor = self.connection.cursor()

            # make the query using %s as a placeholder for the variable
            query = "SELECT scores, grade FROM scores_table WHERE countyname = %s;"

            # executing the query and saying that the type variable 
            # should be placed where %s was, the trailing comma is important!
            cursor.execute(query, (county,))
            return cursor.fetchall()

        except Exception as e:
            print ("Something went wrong when executing the query: ", e)
            return None

    def getAllCountyNames(self):
        """Arguments: None
        Return value: List of county names
        Purpose: Fetches all county names from the database for use in the dropdown list."""
        try:
            cursor = self.connection.cursor()
            query = "SELECT DISTINCT countyname FROM scores_table ORDER BY countyname;"
            cursor.execute(query)
            return [row[0] for row in cursor.fetchall()]
        except Exception as e:
            print("Error fetching counties:", e)
            return []