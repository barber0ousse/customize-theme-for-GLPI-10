# coding: utf-8

import os

windows_path = r"" # Path to your custom files "C:\Users\%userprofile%\glpi"
separator = "\\"
destination = r"" # Your ssh login to your GLPI server "demo@ip"

with open("scp.ps1", "w") as script:
    for path, dirs, files in os.walk(windows_path):
        for filename in files:
            linux_path = ":/var/www/html/glpi" + path[len(windows_path):].replace(separator, "/")
            command = "scp " + path + separator + filename + " " + destination + linux_path + "\r"
            script.write(command)
