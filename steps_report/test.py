import pandas as pd


def is_number_route(my_str):
    new_list = []
    temp = my_str.strip().split(',')
    for i in temp:
        if i.isdigit():
            new_list.append(int(i))
    return new_list


def medium_step(my_str):
    if len(my_str) in (0, 1):
        return 'empty'
    else:
        return my_str[:-1]


def reset_step(my_str):
    if len(my_str) == 1:
        return my_str[0]
    elif len(my_str) == 0:
        return 'empty'
    else:
        return my_str[-1]


# path = r'D:\test.csv'
# new_file = r'D:\test_new.csv'
files_from_sql = r'D:\Отчеты\steps_report\files_from_sql'
files_to_report = r'D:\Отчеты\steps_report\files_to_report'
main_calls = rf'{files_from_sql}\main_calls.csv'
calls_to_report = rf'{files_to_report}\main_calls.csv'

df = pd.read_csv(main_calls, sep=';')
df.fillna('unknown', inplace=True)
df['route'] = df['route'].apply(is_number_route)
df['medium_step'] = df['route'].apply(medium_step)
df['reset_step'] = df['route'].apply(reset_step)
df = df.explode('medium_step')
# df_new = df.explode('route')

df.to_csv(calls_to_report, sep=';', index=False)

print(df.head())
print(df.info())
print(df.shape)
print(df['route'])

# df.to_csv(new_file, sep=';', index=False)
# df_new.to_csv(r'D:\wtf.csv', sep=';', index=False)
print('-' * 50)

# print(df_new.head())
