def lp(n):
    if n % 4 == 0:
        if n % 100 == 0 and n % 400 != 0:
            return "is not a leap year"
        else:
            return "is a leap year"
    else:
        return "is not a leap year"