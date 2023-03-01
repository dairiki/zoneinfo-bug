# sussing out a zoneinfo-bug

Iff `tzdata` is installed,

```py
from zoneinfo import ZoneInfo
ZoneInfo("*")
```

will elicit an `OSError: [Errno 22] Invalid argument` when running on Windows.

It turns out this is because the asterisk is not a valid character for use in filenames on Windows.
There are a number of other similarly banned characters, including `<`, `>`, `:`, `"`, `?` and the control characters "\x01" through "\x1f".

This is closely related to python/cpython#96463.
