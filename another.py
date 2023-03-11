
print('Saving In file...
with open("members.csv", "w", encoding='UTF-8') as f:
    writer = csv.writer(f, delimiter=",", lineterminator="\n")
    writer.writerow(['username'])
    for user in all_paticipant:
        if user.username:
            username = user.username

        writer.writerow([username,
                         ])
print('Members scraped successfully.')
