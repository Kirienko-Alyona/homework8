from datetime import datetime

users = [{"name": "Raul", "birthday": datetime(year=2017, month=11, day=7)},
    {"name": "Kamila", "birthday": datetime(year=2018, month=11, day=6)},
    {"name": "Moruk", "birthday": datetime(year=2010, month=11, day=4)},
    {"name": "Jamy", "birthday": datetime(year=2017, month=11, day=3)},
    {"name": "Jully", "birthday": datetime(year=2020, month=11, day=2)},
    {"name": "Burlem", "birthday": datetime(year=2021, month=11, day=1)},
    {"name": "Daren", "birthday": datetime(year=2011, month=11, day=9)},
    {"name": "Jaky", "birthday": datetime(year=2011, month=11, day=10)}
    ]

### Функція get_birthdays_per_week() приймає список словників з іменами людей і днями народження у форматі datetime. Виводить список співробітників у яких день народження цього тижня
def get_birthdays_per_week(users: list):  
    user_list = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': []
    }
    
    current_date = datetime.now()
   # birthday_range = define_days_interval(current_date)
    current_day_year = current_date.timetuple().tm_yday
    current_year = current_date.timetuple().tm_year
    birthday_range = current_day_year + 7    
    
    for user in users:
        user_birthday_day_year = user["birthday"].timetuple().tm_yday
        now_year_user_birthday = user["birthday"].replace(current_year)

        if current_day_year < user_birthday_day_year <= birthday_range:
            day_of_week = now_year_user_birthday.strftime('%A')
            
            if day_of_week in ['Sunday', 'Saturday', 'Monday']:
                user_list.get('Monday').append(user["name"])
            elif day_of_week == 'Tuesday':
                user_list.get('Tuesday').append(user["name"])
            elif day_of_week == 'Wednesday':
                user_list.get('Wednesday').append(user["name"])
            elif day_of_week == 'Thursday':
                user_list.get('Thursday').append(user["name"])
            elif day_of_week == 'Friday':
                user_list.get('Friday').append(user["name"])

    print_user_list(user_list)   

    return

def print_user_list(user_list: dict):
    for key, value in user_list.items():
        if value:
            print(f"{key}: {', '.join(value)}")

    return

get_birthdays_per_week(users)