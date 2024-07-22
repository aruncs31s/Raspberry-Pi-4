# Raspberry Pi 4

### Remote connection

I used [No machine] for remote access

##### Resizing The display

My monitor or laptop display has a `1366x768` display

```bash
gtf 1366 768 60
xrandr --newmode "1368x768_60.00"  85.86  1368 1440 1584 1800  768 769 772 795  -HSync +Vsync
xrandr --addmode nxoutput0 "1368x768_60.00"
xrandr --output nxoutput0 --mode "1368x768_60.00"
```

### Rsync

1. Notes

```bash
rsync -arhP --progress  aruncs@10.42.1.1:/home/aruncs/Notes/ Notes/ --rsync-path=/bin/rsync
```

2. Projects

```bash
rsync -arhP --progress  aruncs@10.42.1.1:/home/aruncs/Projects/ Projects/ --rsync-path=/bin/rsync
```

3. Git

```bash
rsync -arhP --progress  aruncs@10.42.1.1:/home/aruncs/Projects/Git/ Projects/Git/ --rsync-path=/bin/rsync
```

> > > > > > > 2a22c95 (Initial Commit)
