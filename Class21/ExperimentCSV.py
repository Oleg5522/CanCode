import csv

name1 = 'Anna'
name2 = 'Victor'

with open('data.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(
        #[name1, name2]
        #data_names
        ('user_name', 'user_address')
    )

    users_data = [
        ['user11', 'address1'],
        ['user22', 'address2'],
        ['user33', 'address3']

    ]

#for user in users_data:
#    with open('data.csv', 'a') as file:
#        writer = csv.writer(file)
#        writer.writerow(user)

with open('data.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(users_data)

#with open('data.txt') as file:
#    src = json.load(file)
#    print(src)