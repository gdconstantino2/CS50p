def main():
    x = input("What time' s it? ")
    y = convert(x)
    if (y <= 8) and (y>= 7):
        print("breakfast time")
    elif (y<= 13) and (y>= 12):
        print("lunch time")
    elif (y<= 19 and y>= 18):
        print("dinner time")

def convert(time):
    if (time.lower().strip().endswith("a.m.")):
        hours, j_minutes = time.strip().split(":") #it has minutes + a.m
        minutes, timer = j_minutes.split(" ")
        minutes_float = float(minutes)
        minutes_float = minutes_float / 60
        if hours == "12":
            hours = int(hours) - 12
        new_hour = int(hours) + minutes_float
        return new_hour
    elif (time.lower().strip().endswith("p.m.")):
        hours, j_minutes = time.strip().split(":") #it has minutes + a.m
        minutes, timer = j_minutes.split(" ")
        minutes_float = float(minutes)
        minutes_float = minutes_float / 60
        if hours != "12":
            new_hour = int(hours) + minutes_float + 12
        else:
            new_hour = int(hours) + minutes_float
        return new_hour
    else:
        hours, minutes = time.strip().split(":")
        hours_float = float(hours)
        minutes_float = float(minutes)
        minutes_float = minutes_float / 60
        new_hour = hours_float + minutes_float
        return new_hour

if __name__ == "__main__":
    main()
