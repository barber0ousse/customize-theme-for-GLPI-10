# Customize your GLPI 10.0

Here is a small package who will permit you to customize your GLPI 10.0

## How it works

You have two things here :
* the [*glpi* folder](#-the-glpi-folder) : who contain the files you want to replace to customize your GLPI
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

#### custom_theme.png & custom_logo.png

* **custom_theme.png** is a preview of your theme, usually GLPI put a color pallet. It must be in "*.png*" and measure 60 pixels width by 20 pixels high.
* **custom_logo.png** is your logo, you can put the size you want and adjust it in your **custom_theme.scss** file.

### :warning: Your "custom_theme.scss" and "custom_theme.png" MUST have the same name before the extension. :warning:

___

### The python file

In the python file you have two lines to edit before using it :

```py
windows_path = r"" # Path to your custom files "C:\Users\%userprofile%\glpi"
destination = r"" # Your ssh login to your GLPI server "demo@ip"
```

Here is the output you will have in your **scp.ps1** file

```bash
scp C:\Users\%userprofile%\glpi\css\includes\_logos.scss demo@ip:/var/www/html/glpi/css/includes
scp C:\Users\%userprofile%\glpi\css\palettes\custom_theme.scss demo@ip:/var/www/html/glpi/css/palettes
scp C:\Users\%userprofile%\glpi\css\palettes\previews\custom_theme.png demo@ip:/var/www/html/glpi/css/palettes/previews
scp C:\Users\%userprofile%\glpi\pics\favicon.ico demo@ip:/var/www/html/glpi/pics
scp C:\Users\%userprofile%\glpi\pics\logos\custom_logo.png demo@ip:/var/www/html/glpi/pics/logos
scp C:\Users\%userprofile%\glpi\templates\layout\parts\head.html.twig demo@ip:/var/www/html/glpi/templates/layout/parts
```
