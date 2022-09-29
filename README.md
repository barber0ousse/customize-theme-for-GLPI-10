# Customize your GLPI 10.0

Here is a small package who will permit you to customize your GLPI 10.0

## How it works

___

### GLPI folder

This is what you have in the glpi folder

```
glpi/
├── css/
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

#### 1.Custom_theme.scss

In the **custom_theme.scss** file, you can change colors on the following lines :

```scss
$primary: #ff8811;
$primary-fg: #fff;
$link-color: #2b2b2b;
$mainmenu_bg: #e54a16;
$mainmenu_fg: #fff;
$accent-color: #ff3366;
```

You can also change logos by replacing "*custom_logo.png*" to the name of your own file on the following lines :

```scss
$logo-light: "../pics/logos/custom_logo.png" !default;
$logo-light-reduced: "../pics/logos/custom_logo.png" !default;
$logo-dark: "../pics/logos/custom_logo.png" !default;
$logo-dark-reduced: "../pics/logos/custom_logo.png" !default;
$logo-dark-login: "../pics/logos/custom_logo.png" !default;
$logo-light-login: "../pics/logos/custom_logo.png" !default;
$logo: $logo-light;
$logo_reduced: $logo-light-reduced;
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

#### 2.Custom_theme.png

**custom_theme.png** is a preview of your theme, usually GLPI put a color pallet. It must be in "*.png*" and measure 60 pixels width by 20 pixels high.

#### 3.Head.html.twig

In the **head.html.twig** file, you will have to change "*CUSTOM*" to the name you give to your GLPI on the following line :

```twig
<title>{{ title }} - CUSTOM</title>
```

#### 4.Custom_logo.png

**custom_logo.png** is your logo, you can put the size you want and adjust it in your **custom_theme.scss** file.

### :warning: Your "custom_theme.scss" and "custom_theme.png" MUST have the same name before the extension. :warning:
