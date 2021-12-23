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
![alt text](https://github.com/toorajtaraz/stm32-emacs/blob/master/images/1.jpg?raw=true)
![alt text](https://github.com/toorajtaraz/stm32-emacs/blob/master/images/6.jpg?raw=true)
2. Run and Build your project in both Debug and Release mode
3. Now you can close stm32cubeide, we won't need it anymore!
4. Open up emacs and use projectile-add-known-project to add your brand new project:
![alt text](https://github.com/toorajtaraz/stm32-emacs/blob/master/images/9.jpg?raw=true)
5. For now if you open up main.c you'll get lots of errors, because you haven't initialized your irony server:
![alt text](https://github.com/toorajtaraz/stm32-emacs/blob/master/images/10.jpg?raw=true)
6. All you need to do to take care of this is to run these commands:
   1. test
![alt text](https://github.com/toorajtaraz/stm32-emacs/blob/master/images/6.jpg?raw=true)
