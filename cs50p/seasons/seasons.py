from datetime import date
import inflect
import sys



def main():
    p = inflect.engine()

    #prompt user for date of birth in yyyy-mm-dd
    try:
        y1, m1, d1 = input("Date of birth:" ).split('-')
        do = date(int(y1), int(m1), int(d1)) #do is short for Date Object!
    except ValueError:
        sys.exit("Invalid date")

    #todays date
    td = get_today()

    #get numerals of how old user is
    mins = how_old(td, do)

    #print output
    words = p.number_to_words(mins, andword="")
    final = f"{words} minutes".capitalize()
    print(final)


def get_today():
    return date.today()

def how_old(td, do):
    days = td - do
    m = days.total_seconds() / 60 #'days' is a timedelta object, thats the only reason I can use total_seconds(), its a timedelta method!
    mi = round(m)
    return mi

if __name__ == "__main__":
    main()


