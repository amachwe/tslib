from numpy.core.numeric import full
import pandas as pd
import datetime


def full_moon():

    full_moon_df = pd.read_csv("data/full_moon.csv")

    full_moon_df["DateTime"] = full_moon_df[" Date"]+ full_moon_df[" Time"]


    full_moon = set()
    full_moon_list = []
    

    for i in full_moon_df["DateTime"]:
        
        i = datetime.datetime.strptime(i.strip(), "%d %B %Y %I:%M:%S %p")
        i = datetime.date(day=i.day,month=i.month,year=i.year)
        
        
        full_moon.add(i)

    return full_moon,full_moon_list


month = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12
}
def new_moon():

    with open("data/moon_phase.txt","r") as fh:
        year = None
        dates = set()
        dates_list = []
        date = None
        for l in fh:
            d = l.split()
            if d:
                
                if d[0].isnumeric():
                    year = int(d[0])
                    if d[1].isalpha() and len(d[1])==3:
                        date = datetime.date(year=year,month=month[d[1]],day=int(d[2]))
            

                elif d[0].isalpha() and len(d[0]) == 3:

                    date = datetime.date(year=year,month=month[d[0]],day=int(d[1]))
                
            if date:
                dates.add(date)
                dates_list.append(date)

        return dates, dates_list
                


if __name__ == "__main__":
    full_moon()
    new_moon()
    




        
            
