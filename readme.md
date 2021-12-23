# STM32 for DOOM EMACS

This repository contains configurations for adding stm32 support to doom emacs.
This project is based on  Alexander Lutsai's work at https://github.com/SL-RU/stm32-emacs 
Keep in mind that build system and many other things are fundamentally different.

## Installation

Follow doom emacs documents and add C/C++ to supported languages, You can find my exact configuration in doom.d folder.

## How to setup?

Before anything please replace your .doom.d folder with doom.d in this repository (just its contents not its name), feel free to remove packages you don't like or need.
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
1. Open stm32cubeide and create a new project as usual and configure anything you might need:
![alt text](https://github.com/toorajtaraz/stm32-emacs/blob/master/images/1.jpg?raw=true)
![alt text](https://github.com/toorajtaraz/stm32-emacs/blob/master/images/6.jpg?raw=true)
2. Run and Build your project in both Debug and Release mode
3. Now you can close stm32cubeide, we won't need it anymore.
4. Open up emacs and use projectile-add-known-project to add your brand new project:
![alt text](https://github.com/toorajtaraz/stm32-emacs/blob/master/images/9.jpg?raw=true)
5. Now if you open up main.c you'll get lots of errors, that's because you haven't initialized your irony server:
![alt text](https://github.com/toorajtaraz/stm32-emacs/blob/master/images/10.jpg?raw=true)
6. All you need to do in order to start coding is to run these commands:
   1. stm32-init-project
   2. irony-cdb-json-add-compile-commands-path : Give project's root
   3. irony-cdb-json-select : select recently added CDB
   4. click on error count and wait (When Irony server encounters too many errors it goes into sleep mode and evaluate the file again unless it's forced to do so)
   5. No errors now, you'll also have access to function definitions (jump to definition) and ...
![alt text](https://github.com/toorajtaraz/stm32-emacs/blob/master/images/13.jpg?raw=true)
7. If you want to run and debug the code, here is what you'll need to do:
   1. stm32-start-gdb-debug: this will start st-link server and changes the layout to debug mode:
    ![alt text](https://github.com/toorajtaraz/stm32-emacs/blob/master/images/14.jpg?raw=true)
   2. The rest is classic gdb command, load, run, if you are interested in debugging your code refer to GDB documentations: 
    ![alt text](https://github.com/toorajtaraz/stm32-emacs/blob/master/images/15.jpg?raw=true)
    ![alt text](https://github.com/toorajtaraz/stm32-emacs/blob/master/images/16.jpg?raw=true)
    ![alt text](https://github.com/toorajtaraz/stm32-emacs/blob/master/images/17.jpg?raw=true)
8. For killing everything and releasing the st-link run:
   1. stm32-kill-gdb

There a few other commands in stm32.el, if you are interested in them you can take a look for yourself, that file is well documented.
