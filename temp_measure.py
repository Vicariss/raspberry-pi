from gpiozero import CPUTemperature
from time import sleep, strftime

"""
TODO 
- implement cli features
- add average temperature
- *enovee - implement graphs - how much/why/when temp changing over time?
"""

while True:
    cpu = CPUTemperature()
    cpu_temperature = cpu.temperature
    hour_now = strftime('%H:%M:%S')
    if cpu_temperature > 60:  # check if temp is too high
        data = f"{cpu_temperature}°C - *{hour_now}*"
    else:
        data = f"{cpu_temperature}°C - {hour_now}"
    with open('temperature_history.txt', 'a') as f:
        f.write(f"{data}\n")
    sleep(10)  # seconds
    