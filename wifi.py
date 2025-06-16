
import subprocess
import os
from os import system
from subprocess import CalledProcessError
system('cls' if os.name == 'nt' else 'clear')
# wifi.py
# This script retrieves and displays saved Wi-Fi profiles and their passwords on a Windows machine.

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')


profile = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i or "Perfil de todos los usuarios" in i]
if not profile:
    print("No Wi-Fi profiles found.")
    exit()

for i in profile:
    try:
        result = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
        result = [j.strip() for j in result if j.strip() != ""]
        result = [j for j in result if "Key Content" in j or "Contenido de la clave" in j]
        for j in result:
            if "Key Content" in j:
                result.append(j.split(":")[1][1:-1])
                break
        else:
            print(f"SSID: {i}, Password: Not found")

        try:
            print("{:<30}| {:>}".format(i, result[0]))
        except Exception as e:
            print("{:<30}| {:>}".format(i, "Not found"))
    except Exception as e:
        print("{:<30}| {:>}".format(i, "Not fd"))