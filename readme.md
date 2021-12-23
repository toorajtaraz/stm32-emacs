# STM32 for DOOM EMACS

This repository contains configs for adding stm32 support too doom emacs!

## Installation

Follow doom emacs documents and add C/C++ to supported languages, You can find my exact configuration in doom.d folder!

## How to setup?

Before anything please replace your .doom.d folder with doom.d in this repository (just its contents not its name).
We expect this tree:

```
.
├── config.el
├── custom.el
├── init.el
├── packages.el
└── stm32
    ├── correct_cdb.py
    ├── stm32.el
    └── stm32prj_init.sh
```

Now run:
``` bash
doom sync
```

All you need to do to start coding is to follow this procedure:
1. Open stm32cubeide and create a new project as usual and configer anything you might need:
![alt text](https://github.com/toorajtaraz/stm32-emacs/blob/master/images/10.jpg?raw=true)
