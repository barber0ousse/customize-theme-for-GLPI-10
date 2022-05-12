# Customize your GLPI 10.0

Here is a small package who will permit you to customize your GLPI 10.0

## How it works

You have two things here :
* the *glpi* folder : who contain the files you want to replace to customize your GLPI
* the *scp_creator.py* python file : who will write all the scp lines in a powershell file

### The glpi folder

This is what you have in the glpi folder
```
glpi/
├── css/
│   ├── includes/
│   │   └── logos.scss
│   ├── palettes/
│   │   ├── previews/
│   │   │   └── custom_theme.png
│   │   └── custom_theme.scss
├── pics/
│   ├── logos/
│   │   └── custom_logo.png
│   └── favicon.ico
└── templates/
    └── layout/
        └── parts/
            └── head.html.twig
```

### The python file

In the python file you have two lines to edit and it will work :
```py
windows_path = r"" # Path to your custom files "C:\Users\%userprofile%\glpi"
destination = r"" # Your ssh login to your GLPI server "demo@ip"
```
