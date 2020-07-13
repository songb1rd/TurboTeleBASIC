# TeleBASIC Compiler Toolchain (BCC)
## A handy toolchain for the telebasic power user.

## Index

 - [Brief](#Brief)
 - [Examples](#Examples)
 - [Installing](#Installing)

## Brief

BCC is a compiler toolchain for TeleBASIC users. It currently offers a:
preprocessor, renmumbering and templating support for typical TeleBASIC usage.

Additionaly, BCC provides documentation on the TeleBASIC dialect of BASIC.

## Examples

```basic
REM Save this as "hello.bas"

#define hello_world "Hello, World!"

PRINT {hello_world}
```

 - `python -m bcc hello.bas > hello.bcc.bas`

The contents of `hello.bcc.bas` should now look like:

```basic
0 PRINT "Hello, World!"
```

## Installing

 - Git clone `https://github.com/songb1rd/bcc`
 - Run `pip install .`
