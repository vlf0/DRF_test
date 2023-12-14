# Fixed query for getting all column names from using table
column_names_query = "SELECT column_name FROM information_schema.columns WHERE table_schema = 'mm' AND table_name = 'dbkis';"