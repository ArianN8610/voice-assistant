import psutil as ps


def get_battery_charge() -> str:
    battery = ps.sensors_battery()
    result = f"Battery percentage: {battery.percent}%\n" \
             f"Power plugged in: {battery.power_plugged}\n"

    return result
