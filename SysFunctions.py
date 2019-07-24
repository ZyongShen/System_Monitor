import psutil


def cpu_stats():
    cores = psutil.cpu_count()
    physical_cores = psutil.cpu_count(logical=False)
    print("Cores: " + str(cores) + " and " + "Physical Cores: " + str(physical_cores))
    freq = psutil.cpu_freq()
    print("Frequencies: " + str(freq))
    values = psutil.cpu_stats()
    switches = values[0]
    interrupts = (values[1], values[2])
    calls = values[3]
    item = input("switches, interrupts, or calls?")
    item = str(item.lower())
    if item is "switches":
        print(str(switches))
    elif item is "interrupts":
        print(str(interrupts))
    elif item is "calls":
        print(str(calls))


def network_io():
    netStats = psutil.net_io_counters()
    stat1 = input("What network value would you like?")
    stat1 = stat1.lower()
    stat1 = str(stat1)
    if stat1 is "all":
        for stat in netStats:
            print(str(stat) + ", ")
    elif stat1 is "bytes":
        print(str(netStats[0]) + "and " + str(netStats[1]))
    elif stat1 is "packets":
        print(str(netStats[2]) + "and " + str(netStats[3]))
    elif stat1 is "errors":
        print(str(netStats[4]) + "and " + str(netStats[5]))
    elif stat1 is "drops":
        print(str(netStats[6]) + "and " + str(netStats[7]))

def check_Temps():
    fah = input("Fahrenheit or Celcius? yes or no.")
    if fah is "yes":
        TorF = True
    else:
        TorF = False
    temps = psutil.sensors_temperatures(TorF)

def my_battery():
    battery_stats = psutil.sensors_battery()
    stat = input("battery percent, time left, or plugged in?")
    stat = stat.lower()
    stat = str(stat)
    if stat is "battery percent":
        used = 100.0 - float(battery_stats[0])
        print(str(battery_stats[0]))
        print("Amount used: " + str(used))
    elif stat is "time left":
        format = input("Seconds, minutes, or hours?")
        format = str(format.lower())
        if format is "seconds":
            print(str(battery_stats[1]) + " seconds")
        elif format is "minutes":
            mins = battery_stats[1] / 60
            print(str(mins) + " minutes")
        elif format is "hours":
            hrs = battery_stats[1] / 360
            print(str(hrs) + " hours")
    elif stat is "plugged in":
        if battery_stats[2] is True:
            print("Yes")
        elif battery_stats[1] is False:
            print("No")
        else:
            print("Don't know")



