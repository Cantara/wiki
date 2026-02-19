# KVM

```
/usr/bin/kvm -M pc -m 128 -smp 1 -monitor pty -no-acpi -drive file=/home/username/ubuntu-vm-hardy-urverket/root.qcow2,if=ide,boot=on -net nic,macaddr=52:54:00:57:53:d9,vlan=0 -net tap,fd=11,script=,vlan=0 -usb -vnc 127.0.0.1:0
```
