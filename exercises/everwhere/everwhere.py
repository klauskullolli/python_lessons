from datetime import timedelta, datetime


Filename1 = "timezones.lst"
Filename2 = "today.lst"


def read_timefile(Filename1):
    data = list()
    try:
        with open(Filename1, "r") as f:
            for line in f:
                w1, w2, w3 = line.split(" ", maxsplit=2)
                data.append((w1, w2, w3))
        return data
    except OSError as error:
        exit("fileerror")


def read_today(Filename2):
    try:
        today_list = []
        dict_keys = ["time", "time_zone", "event"]

        with open(Filename2, "r") as f:
            for line in f:
                w1, w2, w3 = line.split(" ", maxsplit=2)
                # w3 = w3.strip[1, -1]
                dict_values = [w1, w2, w3]
                today_dict = dict(zip(dict_keys, dict_values))
                today_list.append(today_dict)
        return today_list
    except OSError as error:
        print(error)
        exit("filerror")


def cal_timedelta(offset_script):
    sign_offset = offset_script[3]
    if ":" in offset_script:
        offset_min = int(offset_script[4:-3]) * 60 + int(offset_script[-2:])
    else:
        offset_min = int(offset_script[4:]) * 60
    return sign_offset, offset_min


def dict_for_delta_cal(time_file_data):
    dict_delta = {}
    for t in time_file_data:
        zone, offset_utc = t[0:2]
        zone = zone[:-1]
        info_offset = cal_timedelta(offset_utc)
        dict_delta[zone] = info_offset
    return dict_delta


def convert_UTC(sign_offset, offset_min, time_script):
    time_script_min = 60 * int(time_script.split(":")[0]) + int(
        time_script.split(":")[1]
    )
    if sign_offset == "-":
        times_UTC_min = time_script_min + offset_min
    elif sign_offset == "+":
        times_UTC_min = time_script_min - offset_min
    return times_UTC_min


# 24*60 = 1440 min  ===> 2400 min


def standard_time_convert(min):

    sign = 1 if min >= 0 else -1

    min = abs(min)

    hour = min // 60

    days = hour // 24
    hour = hour % 24

    min = min % 60

    days = days if sign > 0 else -(days + 1)

    day = "Undefined"
    if days == 0:
        day = "Today"
    elif days == 1:
        day = "Tomorrow"
    elif days == -1:
        day = "Yesterday"
    elif days > 1:
        day = f"{days} days from now"
    else:
        day = f"{abs(days)} days ago"

    return day, f"{hour:02}:{min:02}"


def convert_UTC_data(delta_dict, today_list):
    converted_utc_list = []
    for today in today_list:
        time = today["time"]
        time_zone = today["time_zone"]
        event = today["event"]

        sign_offset, offset_min = delta_dict[time_zone]

        time_min_utc = convert_UTC(sign_offset, offset_min, time)
        print(time_min_utc)
        day, time = standard_time_convert(time_min_utc)

        converted_utc_list.append((day, time, event))
    return converted_utc_list


def main():

    # today_list = read_today(Filename2)
    # print(today_list)

    # time_delta_data = read_timefile(Filename1)
    # print(time_delta_data)
    # offset_script = "UTC-3:30"
    # sign_offset, offset_min = cal_timedelta(offset_script)

    # print(sign_offset)
    # print(offset_min)

    # time_script = "07:30"  # 7*60 + 30 = 450
    # times_UTC = convert_UTC(sign_offset, offset_min, time_script)
    # print(times_UTC)

    time_file_data = read_timefile(Filename1)
    dict_delta = dict_for_delta_cal(time_file_data)
    # print(dict_delta)
    today_list = read_today(Filename2)
    # print(today_list)
    converted_utc_list = convert_UTC_data(dict_delta, today_list)

    for i in converted_utc_list:
        print(i)

    pass


if __name__ == "__main__":
    main()

    # left split is default split
    # right split is rsplit

    # sentence = '07:30 CET "Good Morning Ljubljana!"'

    # splitted  =  sentence.rsplit(" ", maxsplit=1)
    # print(splitted)

    # a, b  = [1, 2]
    # print(a)
    # print(b)
