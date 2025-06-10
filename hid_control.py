#!/usr/bin/env python3

NULL = chr(0)

HID = {
    **{c: i for i, c in enumerate("abcdefghijklmnopqrstuvwxyz", 4)},
    **{c.upper(): i for i, c in enumerate("abcdefghijklmnopqrstuvwxyz", 4)},
    **{n: i for i, n in zip("1234567890", range(30, 40))},
    "\n": 40  # Enter key
}

def write(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())

def press(char, shift=False):
    mod = chr(32) if shift else NULL  # Shift modifier
    code = HID.get(char, None)
    if code:
        write(mod + NULL + chr(code) + NULL*5)
        write(NULL * 8)

def send_password(text):
    for c in text:
        shift = c.isupper() or c in "!@#$%^&*()_+{}|:\"<>?"
        press(c, shift)
    press("\n")  # Enter key

# 🔧 Terminal Control
def open_terminal():
    # Ctrl (0x01) + Alt (0x04) + T (0x17)
    write(chr(0x05) + NULL + chr(0x17) + NULL*5)
    write(NULL * 8)

def send_enter():
    press("\n")
