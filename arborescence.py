# coding: utf-8

import os

windows_path = r"C:\Users\dimitri.clary\GLPI\glpi"
Separator = "\\"
destination = r"admin-si@tipi.tisseo-ingenierie.fr"

with open("scp.ps1", "w") as script:
    for path, dirs, files in os.walk(windows_path):
        for filename in files:
            linux_path = path[len(windows_path):].replace("\\", "/")
            command = "scp " + path + "\\" + filename +" " + destination + ":/var/www/html/glpi" + linux_path + "\r"
            script.write(command)