#Prompt the user to input a date in month-day-year
#output in yyyy-mm-dd
#if not a valid date, prompt the user again, assume each month has no more than 31 days!
def main():
    month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    o = ""
    d1 = ""
    while True:
        try:

            date = input("Date: ")

            if "/" in date:
                #string slice
                date = date.split('/')
                #Declare Variables
                m = date[0]
                m = int(m)
                d = date[1]
                d = int(d)
                y = date[2]
                #validate
                if d > 31 or d < 0:
                    print("try again")
                    continue
                elif len(y) > 4:
                    print("try again")
                    continue
                elif m < 0 or m > 12:
                    print("try again")
                    continue
                else:
                    pass
                #convert to str
                m = f"{m:02d}"
                d = f"{d:02d}"
                #combine all strings together
                o = f"{y}-{m}-{d}" 
                print(o)
                break

            if "," in date and " " in date: ###
                #slice string
                date = date.replace(',', ' ')
                date = date.split(" ") #returns a list
                final = [part for part in date if part] #Get explanation for this###
                #declare year-month-day variables
                m = final[0]
                d = final[1]
                d = int(d)
                y = final[2]
                m1 = month.index(m) + 1 #Analyze: .index()
                #validate year and day
                if d > 31 or d < 0:
                    print("try again")
                    continue
                elif len(y) > 4:
                    print("try again")
                    continue
                else:
                    pass
                #convert variables to string
                m1 = f"{m1:02d}"    ##Analyze: Format Specifiers
                d1 = f"{d:02d}"      ##Analyze: Format Specifiers
                #combine all strings together
                o = f"{y}-{m1}-{d1}"    ##Analyze: Format Specifiers
                print(o)
                break

        except ValueError:
            continue
        except EOFError:
            break
main()
