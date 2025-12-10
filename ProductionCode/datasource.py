import psycopg2

import .config.git.ignore.psqlConfig as config

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

    def areaByBuilding(self, building):
        '''
        Arguments: self, building
        Return value: list of dorms with largest area for a specified building
        Purpose: Get data from our data table and return the dorms with largest area for a specified building
        '''
        try:
            # set up a cursor
            cursor = self.connection.cursor()

            # make the query using %s as a placeholder for the variable
            query = "SELECT * FROM dorm_table WHERE building = %s ORDER BY area;"

            # executing the query and saying that the type variable 
            # should be placed where %s was, the trailing comma is important!
            cursor.execute(query, (county,))
            return cursor.fetchall()

        except Exception as e:
            print ("Something went wrong when executing the query: ", e)
            return None

    def areaByRoomType(self, room_type):
        '''
        Arguments: self, room_type
        Return value: list of dorms with largest area for a specified room type
        Purpose: Get data from our data table and return the dorms with largest area for a specified room type
        '''
        try:
            # set up a cursor
            cursor = self.connection.cursor()

            # make the query using %s as a placeholder for the variable
            query = "SELECT * FROM dorm_table WHERE room_type = %s ORDER BY area;"

            # executing the query and saying that the type variable 
            # should be placed where %s was, the trailing comma is important!
            cursor.execute(query, (county,))
            return cursor.fetchall()

        except Exception as e:
            print ("Something went wrong when executing the query: ", e)
            return None

    def areaByFloorType(self, floor_type):
        '''
        Arguments: self, floor_type
        Return value: list of dorms with largest area for a specified floor type
        Purpose: Get data from our data table and return the dorms with largest area for a specified floor type
        '''
        try:
            # set up a cursor
            cursor = self.connection.cursor()

            # make the query using %s as a placeholder for the variable
            query = "SELECT * FROM dorm_table WHERE floor_type = %s ORDER BY area;"

            # executing the query and saying that the type variable 
            # should be placed where %s was, the trailing comma is important!
            cursor.execute(query, (county,))
            return cursor.fetchall()

        except Exception as e:
            print ("Something went wrong when executing the query: ", e)
            return None

    def getAllBuildingNames(self):
        """Arguments: None
        Return value: List of building names
        Purpose: Fetches all building names from the database for use in the dropdown list."""
        try:
            cursor = self.connection.cursor()
            query = "SELECT DISTINCT building FROM dorm_table ORDER BY building;"
            cursor.execute(query)
            return [row[0] for row in cursor.fetchall()]
        except Exception as e:
            print("Error fetching counties:", e)
            return []

    def getAllRoomTypes(self):
        """Arguments: None
        Return value: List of room types
        Purpose: Fetches all room types from the database for use in the dropdown list."""
        try:
            cursor = self.connection.cursor()
            query = "SELECT DISTINCT room_type FROM dorm_table ORDER BY room_type;"
            cursor.execute(query)
            return [row[0] for row in cursor.fetchall()]
        except Exception as e:
            print("Error fetching counties:", e)
            return []

    def getAllFloorTypes(self):
        """Arguments: None
        Return value: List of floor types
        Purpose: Fetches all floor types from the database for use in the dropdown list."""
        try:
            cursor = self.connection.cursor()
            query = "SELECT DISTINCT floor_type FROM dorm_table ORDER BY floor_type;"
            cursor.execute(query)
            return [row[0] for row in cursor.fetchall()]
        except Exception as e:
            print("Error fetching counties:", e)
            return []