def is_leap_year(year):
    if year % 4 == 0:
        print(year)
        if year % 100 == 0:
            print(year)
            if year % 400 == 0:
                print(year)
                return True
            else:
                print(year)
                return False
        else:
            print(year)
            return True
    else:
        print(year)
        return False


def is_leap_year2(year):
    if year % 4:
        print("yes")
        if year % 100:
            print(year)
            if year % 400:
                print(year)
                return True
            else:
                print(year)
                return False
        else:
            print(year)
            return True
    else:
        print("First Check")
        # Every time only above print statement will execute because of not proper defined if condition
        return False


# is_leap_year(2000)



# is_leap_year2(2000)



print(20/4)
# 5.0
print(20//4)
# 5
