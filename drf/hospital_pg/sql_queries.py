# Fixed query for getting all column names from using table

class SQLQueries:

    column_names_query = "SELECT column_name FROM information_schema.columns" \
                         " WHERE table_schema = 'mm' AND table_name = '{}';"

    def choose_table(self, table_name):
        return self.column_names_query.format(table_name)




