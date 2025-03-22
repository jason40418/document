<!--
  @file
  QEMU documentation.

  @copyright
  Copyright (c) 2025, Jason Lin. All rights reserved.<BR>

  SPDX-License-Identifier: BSD-3-Clause

  @par Specification Reference:

-->

# QEMU

```{note}
Last Update: 2025-01-01 (Wed.)
```

# Boot from QEMU System

## Basic Command
```
qemu-system-x86_64 \
  -bios <BIOS_ROM_IMAGE> \
  -debugcon file:<DEBUG_LOG_PATH> \
  -global isa-debugcon.iobase=0x402 \
  -fw_cfg name=opt/org.tianocore/X-Cpuhp-Bugcheck-Override,string=yes \
  -display none \
  -vnc :0
```

## Simulate the USB Device

```{tip}
Refer the [QEMU USB Emulation](https://qemu-project.gitlab.io/qemu/system/devices/usb.html) document to see the usage.
```

```bash
  -drive if=none,id=stick,format=raw,file=USB.img \
  -device nec-usb-xhci,id=xhci \
  -device usb-storage,bus=xhci.0,drive=stick
```

```{figure-md}
:align: center

![](images/qemu/qemu_usb_setup.png)

Boot to setup option with USB device
```

```{figure-md}
:align: center

![](images/qemu/qemu_usb_uefi_shell.png)

Boot to UEFI shell with USB device
```

# Create USB Image (FAT32)

## Linux

```{tip}
Use the command ```losetup``` to see the whole loop device.
```

### Create the Blank Image

```
dd if=/dev/zero of=USB.img iflag=fullblock bs=1M count=100 && sync
```

### Format the Image as FAT

```
mkfs.vfat USB.img
```

### Mount the Image

```
sudo mkdir /mnt/VirtualImg
sudo mount -o loop USB.img /mnt/VirtualImg
sudo umount /mnt/VirtualImg
```
