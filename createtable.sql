/* Check that the table doesn't already exist in the database. If it does,remove it from the database */
DROP TABLE IF EXISTS ses_table;

/* Create the table in the database & give it a name */
CREATE TABLE ses_table (

/* Tell the database which data to import, what its name in the database should be, & the type of data to import */
	countyname text,
	ses float,
    grade int
);

/* Check that the table doesn't already exist in the database. If it does,remove it from the database */
DROP TABLE IF EXISTS scores_table;

/* Create the table in the database & give it a name */
CREATE TABLE scores_table (

/* Tell the database which data to import, what its name in the database should be, & the type of data to import */
	countyname text,
	scores float,
    grade int
);
