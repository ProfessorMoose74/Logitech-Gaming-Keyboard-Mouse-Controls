---
name: Device support request
about: Request support for a new Logitech device
title: '[DEVICE] '
labels: device-support
assignees: ''
---

**Device Information**
 - Device model: [e.g. Logitech G815]
 - Device type: [Keyboard/Mouse/Other]

**USB Information**
Output of `lsusb | grep Logitech`:
```
paste output here
```

**Current Status**
- [ ] Device is detected by LogiLight but doesn't work
- [ ] Device is not detected at all
- [ ] Device partially works (specify what works/doesn't work)

**Testing**
Have you tested with the underlying tools?

For keyboards:
```bash
sudo g810-led -a ff0000
```

For mice:
```bash
ratbagctl list
```

**Output/Results:**
```
paste results here
```

**Additional Information**
Any other details about the device or testing you've done.
