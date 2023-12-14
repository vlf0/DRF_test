
# def dataset_to_dict(columns, vals):
#     drf_queryset = dict(zip(keys_list, zip(*values_list)))
#     return drf_queryset

# print(dataset_to_dict(['id', 'name', 'create_dt', 'dates2'], [('a', 'b'), ('c', 'd'), ('e', 'f')]))


def dataset_to_dict(lst):
    drf_queryset = {'id': lst[0],
                    'name': lst[1],
                    'date1': lst[2],
                    'date2': lst[3]
                    }
    return drf_queryset





