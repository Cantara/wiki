# LVM

#### What is and how to use LVM? 

RTFM; [LVM HOWTO](http://tldp.org/HOWTO/LVM-HOWTO/)

#### How to use lvm to use multiple disk as one logical file share? 

- Pv, vg and lv setup
```
pvcreate /dev/sda /dev/sdb /dev/sdc

vgcreate data1 /dev/sda /dev/sdb /dev/sdc

vgdisplay data1 | grep "Total PE"

lvcreate -l 155008 --name store data1

```

- Make filesystem: 
```
mkfs.ext3 -m 0 -O sparse_super /dev/lvm_ed/store 
```

#### How to add a disk to an existing lvm setup? 

- Initialize the disk for use with lvm 
```
pvcreate /dev/sde
```

- Extend vg		

```
vgextend data /dev/sde
```

- Extend lv

use vgdisplay to find available PEs and extend lv accordingly. 

```
vgdisplay data | grep "Free  PE"
lvextend -l +59618 /dev/data/media
```

- Extend file system 

```
umount /dev/data/media
e2fsck -f /dev/data/media
resize2fs /dev/data/media
```

- mount the device

#### How to remove a disk from an existing lvm setup? 

- unmount the lvm device

- make filesystem smaller	

```
e2fsck -f /dev/lvm_ed/store

resize2fs /dev/lvm_ed/store 350G 
```

- Reduce lv
```
lvreduce -L 350g /dev/lvm_ed/store

```

- Move data away from the physical disk 
```
pvmove  /dev/sde		

```

- Reduce vg

```
vgreduce lvm_ed /dev/sde

```

- mount

on /dev/lvm_ed/store to 91750400 (4k) blocks.

resize2fs device newSize
