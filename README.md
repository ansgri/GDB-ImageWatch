# GDB Image Watch

This is a simple python extension script to visualize interactively OpenCV
images while debugging with gdb.

This is a modification that actually works on `gdb 7.7` on python3, though only implements non-interactive "save_image" functionality.

## INSTALL

 You need to have gdb (version 7.7 or newer).

 You can try to use the `save_image` command by sourcing it first from within a gdb
 session with the command

```
 gdb> source save_image.py
```

 (insert the path to the `save_image.py` file on your machine, if it is not in the
 gdb current working directory). You can also add the command to your `.gbdinit`
 file if you do not want to source it at each session.

## USAGE

 Usage is extremely simple, once you have sourced the file. If the variable you
 want to inspect (i.e., show) is a `cv::Mat` or an `IplImage` or MinImg or mximg::PImage with name 'image',
 all you need to do is

```
 gdb> save_image image [path/to/image.png=/tmp/gdb.png]
```

 from within your gdb session.


## DEMO

 To use the demo

 ```
 $ cd gdb-imshow
 $ mkdir Debug
 $ cd Debug
 $ cmake -DCMAKE_BUILD_TYPE=Debug ..
 $ make
 $ gdb ./main
 ```

