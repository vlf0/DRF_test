# Fixed query for getting all column names from using table

class BaseSQLQueries:

    base_query = "SELECT status FROM mm.pats;"

    column_names_query = "SELECT column_name FROM information_schema.columns" \
                         " WHERE table_schema = 'mm' AND table_name = 'pats';"

    # def __init__(self, initial_value):
    #     self.base_limited_query = self.base_query.format(initial_value)
    #     self.column_names_query = self.column_names_query.format(initial_value)


class DeptFilterSQLQueries(BaseSQLQueries):

    base_query = "SELECT * FROM mm.{};"

    def __init__(self, initial_value):
        super().__init__(initial_value)
        self.base_query = self.base_query.format(initial_value)

