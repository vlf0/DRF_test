

def dataset_to_dict(lst):
    drf_queryset = {'id': lst[0],
                    'name': lst[1],
                    'date1': lst[2],
                    'date2': lst[3]
                    }
    return drf_queryset

