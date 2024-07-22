#!/bin/bash

xrandr --newmode "1368x768_60.00" 85.86 1368 1440 1584 1800 768 769 772 795 -HSync +Vsync
xrandr --addmode nxoutput0 "1368x768_60.00"
xrandr --output nxoutput0 --mode "1368x768_60.00"
