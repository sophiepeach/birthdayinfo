def age():
    """Asks for the date of user's birth and the current date in order to calculate and print the users age
    and a birthday message when applicable. Date of birth values are passed to three functions which print the
    corresponding birthstone, Chinese zodiac animal, and astrological zodiac sign respectively."""
    birthday_string = input("Enter your birthday in the form month_day_full year, for example: 1 1 1990 ")
    today_string = input("Enter today's date in the same form, for example: 1 12 2005 ")
    b = birthday_string.split(" ")
    t = today_string.split(" ")
    bd_month = int(b[0])
    bd_day = int(b[1])
    bd_year = int(b[2])
    today_month = int(t[0])
    today_day = int(t[1])
    today_year = int(t[2])
    before_bd_age = (today_year - bd_year) - 1
    after_bd_age = today_year - bd_year
    if bd_year > today_year:
        print("Please start over!")
        return
    if bd_day > 31 or today_day > 31:
        print("Please start over!")
        return
    if bd_month > 12 or today_month > 12:
        print("Please start over!")
        return
    if bd_month == today_month and bd_day == today_day:
        print("Today is your birthday! Happy Birthday!")
        print("Your age is {}".format(after_bd_age))
    if bd_month == today_month and bd_day > today_day:
        print("Your age is {}".format(before_bd_age))
    if bd_month == today_month and bd_day < today_day:
        print("Your age is {}".format(after_bd_age))
    if bd_month > today_month:
        print("Your age is {}".format(before_bd_age))
    if bd_month < today_month:
        print("Your age is {}".format(after_bd_age))
    birthstone(bd_month)
    animals(bd_year)
    star_sign(bd_month, bd_day)


def birthstone(month):
    """Uses a month's number to get the stone for that month and prints it."""
    stones = ["stone", "garnet", "amethyst", "aquamarine", "diamond", "emerald",
              "pearl/alexandrite", "ruby", "peridot", "sapphire", "tourmaline/opal",
              "topaz/citrine", "tanzanite/zircon/turqouise"]
    print("Your birthstone is", stones[month])


def animals(y):
    """Takes a given year and calculates the assigned animal in the cycle for that year and prints it."""
    z = ["monkey", "rooster", "dog", "pig", "rat", "ox", "tiger", "rabbit", "dragon", "snake", "horse", "sheep"]
    n = y % 12
    print("Your Chinese zodiac animal is the", z[n])


def star_sign(x, d):
    """Uses a month and day date to determine that day's astrological zodiac sign and prints it."""
    if x == 1:
        if d < 20:
            star = "Capricorn"
        else:
            star = "Aquarius"
    if x == 2:
        if d < 19:
            star = "Aquarius"
        else:
            star = "Pisces"
    if x == 3:
        if d < 21:
            star = "Pisces"
        else:
            star = "Aries"
    if x == 4:
        if d < 20:
            star = "Aries"
        else:
            star = "Taurus"
    if x == 5:
        if d < 21:
            star = "Taurus"
        else:
            star = "Gemini"
    if x == 6:
        if d < 21:
            star = "Gemini"
        else:
            star = "Cancer"
    if x == 7:
        if d < 23:
            star = "Cancer"
        else:
            star = "Leo"
    if x == 8:
        if d < 23:
            star = "Leo"
        else:
            star = "Virgo"
    if x == 9:
        if d < 23:
            star = "Virgo"
        else:
            star = "Libra"
    if x == 10:
        if d < 23:
            star = "Libra"
        else:
            star = "Scorpio"
    if x == 11:
        if d < 22:
            star = "Scorpio"
        else:
            star = "Sagittarius"
    if x == 12:
        if d < 22:
            star = "Sagittarius"
        else:
            star = "Capricorn"
    print("Your astrological zodiac sign is {}".format(star))


age()
