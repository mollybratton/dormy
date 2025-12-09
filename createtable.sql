/* Check that the table doesn't already exist in the database. If it does,remove it from the database */
DROP TABLE IF EXISTS dorm_table;

/* Create the table in the database & give it a name */
CREATE TABLE dorm_table (

/* Tell the database which data to import, what its name in the database should be, & the type of data to import */
	building text,
	room_number text,
	room_type text,
    area int,
	floor_type text
)
