
birthday_dict = {"January":1,"February":2, "March":3,"April":4,"May":5,"June":6,"July":7,
                 "August":8,"September":9,"October":10,"November":11,"December":12}
birthdays = []
edited_birthdays = []

for x in range(5):
    birthdays.append(input(f"Enter your birthday user{x}: ").split())


playing = True
while playing:
    if len(birthdays) == 0:
        playing = False
    else:
        earliest = birthdays[0]
        for y in range(len(birthdays[:])):
            if birthday_dict.get(birthdays[y][0]) == birthday_dict.get(earliest[0]):
                if birthdays[y][1] < earliest[1]:
                    earliest = birthdays[y]
            elif birthday_dict.get(birthdays[y][0]) < birthday_dict.get(earliest[0]):
                earliest = birthdays[y]
        edited_birthdays.append(earliest)
        birthdays.remove(earliest)
for x in range(len(edited_birthdays)):
    print(f"{edited_birthdays[x][0]} {edited_birthdays[x][1]}")









