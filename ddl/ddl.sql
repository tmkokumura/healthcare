CREATE TABLE healthcare(
	id INTEGER PRIMARY KEY AUTOINCREMENT, 
	data_type TEXT, 
	source_name TEXT, 
	source_version TEXT, 
	device TEXT, 
	unit TEXT, 
	creation_date TEXT,
	creation_time TEXT, 
	start_date TEXT,
	start_time TEXT, 
	end_date TEXT,
	end_time TEXT, 
	value REAL
);