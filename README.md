# TurboTeleBASIC
## A handy toolchain for the telebasic power user.

## Index

 - [Brief](#Brief)
 - [Examples](#Examples)
 - [Installing](#Installing)

## Brief

TurboTeleBASIC is a developer toolchain designed for TeleBASIC users in mind.
It offers a TeleBASIC standalone runtime and compiler suitable for usage as
a typical TeleBASIC intepreter or as the compiler expands to support TeleBASIC
as a target output, allowing languages to compile into TeleBASIC. or TeleBASIC
as a target input for other output forms i.e. WASM or x86_64 elf.

TurboTeleBASIC aims to provide full and complete documentation on the TeleBASIC
dialect of BASIC.

## Installing

### With Git and pip

 - `git clone https://github.com/songb1rd/TurboTeleBASIC`
 - `cd TurboTeleBASIC`
 - `pip install --user .`

### Via pip directly

 - `pip install --user https://github.com/songb1rd/TurboTeleBASIC#egg=turbotelebasic`

## Examples

> Note:
> Make sure you've installed TurboTeleBASIC with the instructions
> under [Installing](#Installing)

### Interpreted *"Hello, World!"*

```basic
00 REM Save this as "hello.bas"
10 PRINT "Hello, World!"
```

 - `python -m turbotelebasic -i hello.bs`
