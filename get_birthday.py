from datetime import datetime

users = [{"name": "Raul", "birthday": datetime(year=2017, month=11, day=7)},
    {"name": "Kamila", "birthday": datetime(year=2018, month=11, day=6)},
    {"name": "Moruk", "birthday": datetime(year=2010, month=11, day=4)},
    {"name": "Jamy", "birthday": datetime(year=2017, month=11, day=3)},
    {"name": "Jully", "birthday": datetime(year=2017, month=11, day=9)},
    {"name": "Burlem", "birthday": datetime(year=2017, month=11, day=9)}
    ]

### Функція get_birthdays_per_week() приймає список словників з іменами людей і днями народження у форматі datetime. Виводить список співробітників у яких день народження цього тижня
def get_birthdays_per_week(users):  
    names_users_birthday_Monday = []
    names_users_birthday_Tuesday = []
    names_users_birthday_Wednesday = []
    names_users_birthday_Thursday = []
    names_users_birthday_Friday = []
    birthday_on_Monday = "" 
    birthday_on_Tuesday = "" 
    birthday_on_Wednesday = ""
    birthday_on_Thursday = ""
    birthday_on_Friday = ""
    current_datetime = datetime.now()
    current_datetime = current_datetime.timetuple()
    current_day_year = current_datetime.tm_yday
    current_year = current_datetime.tm_year
    birthday_range = current_day_year + 7
    
    for user in users:
        user_name = user["name"]
        user_birthday = user["birthday"]
        user_birthday_tuple = user_birthday.timetuple()
        user_birthday_day_year = user_birthday_tuple.tm_yday
        now_year_user_birthday = user_birthday.replace(current_year)

        if user_birthday_day_year <= birthday_range:
            day_of_week = now_year_user_birthday.strftime('%A')
            
            if day_of_week == "Sunday" or day_of_week == "Saturday" or day_of_week == "Monday":
                names_users_birthday_Monday.append(user_name)
                name_users_Monday = ", ".join(names_users_birthday_Monday)
                birthday_on_Monday = f"Monday: {name_users_Monday}"
            elif day_of_week == "Tuesday":
                names_users_birthday_Tuesday.append(user_name)
                name_users_Tuesday = ", ".join(names_users_birthday_Tuesday)
                birthday_on_Tuesday = f"{day_of_week}: {name_users_Tuesday}"    
            elif day_of_week == "Wednesday":
                names_users_birthday_Wednesday.append(user_name)
                name_users_Wednesday = ", ".join(names_users_birthday_Wednesday)
                birthday_on_Wednesday = f"{day_of_week}: {name_users_Wednesday}"
            elif day_of_week == "Thursday":
                names_users_birthday_Thursday.append(user_name)
                name_users_Thursday = ", ".join(names_users_birthday_Thursday)
                birthday_on_Thursday = f"{day_of_week}: {name_users_Thursday}"
            elif day_of_week == "Friday":
                names_users_birthday_Friday.append(user_name)
                name_users_Friday = ", ".join(names_users_birthday_Friday)
                birthday_on_Friday = f"{day_of_week}: {name_users_Friday}"    

    if birthday_on_Monday != "":
        print(birthday_on_Monday)     
    if birthday_on_Tuesday != "":
        print(birthday_on_Tuesday)
    if birthday_on_Wednesday != "":
        print(birthday_on_Wednesday)     
    if birthday_on_Thursday != "":
        print(birthday_on_Thursday)    
    if birthday_on_Friday != "":
        print(birthday_on_Friday)  
           
    return


get_birthdays_per_week(users)
