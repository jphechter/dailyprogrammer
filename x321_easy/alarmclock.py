#!/usr/bin/python3

def main():
    print("Enter a time.")
    time = input()
    if checkInputFormat(time) == True:
        print(convertTimeToText(time))
    else:
        print("That's not right.")

def checkInputFormat(timeEntered):
    if len(timeEntered) != 5:
        return False
    for i in range(0,2):
        if not timeEntered[i].isdecimal():
            return False
    if timeEntered[2] != ":":
        return False
    for i in range(3,5):
        if not timeEntered[i].isdecimal():
            return False
    return True

def convertTimeToText(timeEntered):
    hour = int(timeEntered[0:2])
    minute = int(timeEntered[3:5])
    am_pm = None
    textConversion = ["-", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "thirty", "forty", "fifty"]
    # Noon or Midnight
    if hour == 0:
        hour = textConversion[12]
        am_pm = "am"
    if hour == 12:
        hour = textConversion[12]
        am_pm = "pm"
    # Morning
    if 1 <= hour < 12:
        hour = textConversion[hour]
        am_pm = "am"
    # Afternoon
    if 12 < hour <= 23:
        hour = textConversion[hour%12]
        am_pm = "pm"
    if minute == 0:
        minute = ""
    if 1 <= minute <= 20:
        minute = textConversion[minute] + " "
    if minute//10 >= 2:
        minute = textConversion[20+(minute//10-2)]
        if int(timeEntered[4]) >= 1:
            minute = minute+textConversion[0]+textConversion[int(timeEntered[4])]
        minute = minute + " "
    time = "It's " + hour + " " + minute + am_pm
    return time

if __name__ == "__main__": main()