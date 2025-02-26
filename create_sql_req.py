import pandas as pd

df = pd.read_csv('./google_dataset.csv')

sql = "INSERT INTO event VALUES"
values =  [] 

for i, row in df.iterrows():
    values.append(f"({row['event_id']}, {row['event_date']}, {row['customer_id']},"
    f"{row['is_attend']}, {row['group_ids']}, {row['teacher_ids']},"
    f"{row['attendance_id']})")

sql_req = sql+',\n'.join(values)+";"

with open("insert_request.sql", "w", encoding="utf-8") as file:
    file.write(sql_req)