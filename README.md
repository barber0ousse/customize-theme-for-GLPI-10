# Customize your GLPI 10.0

Here is a small package who will permit you to customize your GLPI 10.0

## How it works

You have two things here :
* the *glpi* folder : who contain the files you want to replace to customize your GLPI
* the *scp_creator.py* python file : who will write all the scp lines in a powershell file
___
### The glpi folder

This is what you have in the glpi folder
```
glpi/
├── css/
│   ├── includes/
│   │   └── logos.scss *
│   ├── palettes/
│   │   ├── previews/
│   │   │   └── custom_theme.png
│   │   └── custom_theme.scss *
├── pics/
│   ├── logos/
│   │   └── custom_logo.png
│   └── favicon.ico
└── templates/
    └── layout/
        └── parts/
            └── head.html.twig *
            
* files to edit with custom values
```

#### logos.scss
In the **logos.scss** file, you will have to change "*custom_logo.png*" to the name of your own file on the following lines :

```scss
$logo-light: "../pics/logos/custom_logo.png" !default;
$logo-light-reduced: "../pics/logos/custom_logo.png" !default;
$logo-dark: "../pics/logos/custom_logo.png" !default;
$logo-dark-reduced: "../pics/logos/custom_logo.png" !default;
$logo-dark-login: "../pics/logos/custom_logo.png" !default;
$logo-light-login: "../pics/logos/custom_logo.png" !default;
```

#### custom_theme.scss
In the **custom_theme.scss** file, you can change colors on the following lines :

```scss
$primary: #ff8811;
$primary-fg: #fff;
$link-color: #2b2b2b;
$mainmenu_bg: #e54a16;
$mainmenu_fg: #fff;
$accent-color: #ff3366;
```

You can also change the logo sizes on the following lines to make it fit as you want :

```scss
/*
*   NORMAL PAGE LOGO
*/

.page {
    .glpi-logo {
        background: url($logo) center no-repeat;
        background-size: contain;
        height: 100px;
        width: 100px;
    }
}

/*
*   LOGIN PAGE LOGO
*/

.page-anonymous {
    .glpi-logo {
        width: 150px;
        height: 150px;
    }
}
```

#### head.html.twig
In the **head.html.twig** file, you will have to change "*CUSTOM*" to the name you give to your GLPI on the following line :

```twig
<title>{{ title }} - CUSTOM</title>
```

___
### The python file

In the python file you have two lines to edit before using it :

```py
windows_path = r"" # Path to your custom files "C:\Users\%userprofile%\glpi"
destination = r"" # Your ssh login to your GLPI server "demo@ip"
```
