# Fixed query for getting all column names from using table

class BaseSQLQueries:

    base_limited_query = "SELECT * FROM mm.{} LIMIT 5;"

    column_names_query = "SELECT column_name FROM information_schema.columns" \
                         " WHERE table_schema = 'mm' AND table_name = '{}';"

    def __init__(self, initial_value):
        self.base_limited_query = self.base_limited_query.format(initial_value)
        self.column_names_query = self.column_names_query.format(initial_value)


class FilterSQLQueries(BaseSQLQueries):

    base_query = "SELECT id, name FROM mm.{} LIMIT 5;"

    def __init__(self, initial_value):
        super().__init__(initial_value)
        self.base_query = self.base_query.format(initial_value)

