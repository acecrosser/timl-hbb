from data.dbase.models import distinct, sum_title, today


def general_make_order(table, id_user, month) -> str:
    work_data = distinct(name='grouping', table=table, id_user=id_user, period=month)
    end_list = ''
    for i in work_data:
        sum = sum_title(table=table, id_user=id_user, period=month, grouping=i[0], name='grouping')
        end_list += f'{i[0]} --- <b>{sum[0]}</b> руб.\n'
    return end_list


