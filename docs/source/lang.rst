TeleBASIC
=========


1. Variables and Data Types
---------------------------
You can store either text or numerical values in variables. 
Variable names can contain letters and digits, but they have to start with a letter. 
You cannot use reserved keywords (e.g. ``FOR``, ``IF``) as variable names.
Variable names can be suffixed with a type-definition character:
 - ``$`` represents a text (string) value
 - ``%`` represents a numeric (integer) value
 - ``!`` represents a numeric (single-precision) value
Numerical variables and strings cannot be used interchangeably.
For example::

	10 NAME$ = "some name"

would represent a string variable, but::

	10 NAME% = "some name"

would throw a ``TYPE MISMATCH ERROR`` as you can't assign a string to a numeric variable.

2. Arrays
------------------
An array is basically a list of values. These can be accessed by specifying an index number.
For example, we define a string array of size 10::
	10 DIM MYLIST$(10)

Now we can modify the 5th entry (note that the array index usually starts at 0, and can be also negative)
::
	20 MYLIST$(4) = "some text"

3. Overview of Commands
-----------------------

``abs``
~~~~~~~
Returns the absolute value of the specified value

``arg$``
~~~~~~~~
Variable containing argumnets passed to program on command line

``asc``
~~~~~~~
Returns the ASCII-Code for its equivalent character

``atn``
~~~~~~~
Returns the arctangent of the specified value

``beep``
~~~~~~~~
Sends a bell

``brk``
~~~~~~~
Sets and returns status of BREAK key

``chr$``
~~~~~~~~
Convert an ASCII-Code to its equivalent character

``cint``
~~~~~~~~
Returns the nearest integer of the specified value (9.5 becomes 10)

``clear``
~~~~~~~~~
Clears all variables and closes all open files

``close``
~~~~~~~~~
Close the file and save it/create if it doesn't exist

``cls``
~~~~~~~
Clears the screen

``color``
~~~~~~~~~
Changes the background and/or foreground colour of the terminal

``cos``
~~~~~~~
Returns the cosine of a specified value

``csng``
~~~~~~~~
Convert a specified value to a single precision number

``data``
~~~~~~~~
Store the numeric and string constants that are accessed by the program READ statements

``date$``
~~~~~~~~~
Returns the current date

``def fn``
~~~~~~~~~~
Defines a function

``defdbl``
~~~~~~~~~~
Declare a variable as double precision number

``defint``
~~~~~~~~~~
Declare a variable as integer number

``defsng``
~~~~~~~~~~
Declare a variable as single precision number 

``defstr``
~~~~~~~~~~
Declare a variable as string

``dim``
~~~~~~~
Define an array of a fixed size

``dir$``
~~~~~~~~
Returns the filenames in your local directory, separated by spaces

``end``
~~~~~~~
Ends the current program

``exp``
~~~~~~~
Returns the base of natural logarithms to the power of the specified value

``for``
~~~~~~~
Execute a series of instructions a specified number of times in a loop

``gosub``
~~~~~~~~~
Branch to a subroutine and return

``goto``
~~~~~~~~
Branch unconditionally out of the normal program sequence to the specified line number

``height``
~~~~~~~~~~
Returns your terminal height

``hex$``
~~~~~~~~
Returns a string which represents the hexadecimal value of the specified value

``home``
~~~~~~~~
Sets the cursor to the top left position of the screen

``if``
~~~~~~
Make a decision regarding program flow based on the result of a returned expression

``inkey$``
~~~~~~~~~~
Returns one character read from the terminal. it will wait till any character is being typed

``input``
~~~~~~~~~
Shows Prompt and reads input from the users terminal and save it into a Variable

``instr``
~~~~~~~~~
Returns the position of a substring in a string

``int``
~~~~~~~
Truncate an value to a whole number

``itm``
~~~~~~~
Returns the data item number in the current record

``left$``
~~~~~~~~~
Returns a string that comprises the left-most specified number characters of a specified string

``len``
~~~~~~~
Returns the number of characters in the specified string

``let``
~~~~~~~
Assigns a value to a variable

``lin``
~~~~~~~
Returns one or more line feeds

``locate``
~~~~~~~~~~
Change the cursors position

``log``
~~~~~~~
Returns the natural logarithm of the specified value

``log10``
~~~~~~~~~
Returns the natural logarithm of the specified value (Base 10)

``mid$``
~~~~~~~~
Returns a string of l characters from String beginning with the n Character

``new``
~~~~~~~
Creates a new basic program

``next``
~~~~~~~~
Used within for. execute a series of instructions a specified number of times in a loop

``nint``
~~~~~~~~
Returns the nearest integer of the specified value (9.5 becomes 9)

``num``
~~~~~~~
Returns the ASCII-Code for its equivalent character

``oct$``
~~~~~~~~
Returns a octal value of a specific value

``open``
~~~~~~~~
Opens a file

``pclear0``
~~~~~~~~~~~
Reserves one page of memory (no effect)

``pclear1``
~~~~~~~~~~~
Reserves two pages of memory (no effect)

``peek``
~~~~~~~~
Read a value from the specified memory location

``pmode0``
~~~~~~~~~~
Selects a resolution and first memory page of a low resolution graphic screen. (0 - 128 x 96, 2 colour) (no effect)

``poke``
~~~~~~~~
Write a byte of data into the specified memory location

``polkey$``
~~~~~~~~~~~
Returns one character read from the terminal. when no key is hit within one second, it returns an empty string

``pos``
~~~~~~~
Returns the character position in string 1, where the first occurrence of string 2 was found

``print``
~~~~~~~~~
Prints a expression on the screen

``r2d``
~~~~~~~
Converts radians to degrees

``randomize``
~~~~~~~~~~~~~
Reseed the random number generator

``read``
~~~~~~~~
Read a value from DATA and assign them to variables

``rec``       
~~~~~~~
Returns the current record number (line number) in the specified file

``rem``
~~~~~~~
Explanatory remark. does not get executed by the interpreter

``renumber``
~~~~~~~~~~~~
Renumbers a basic program

``restore``
~~~~~~~~~~~
Allow DATA statements to be reread

``return``
~~~~~~~~~~
Return from a subroutine

``right$``
~~~~~~~~~~
Returns the rightmost Number(n) characters of the specified String

``rnd``
~~~~~~~
Returns a random number between 0 and 1

``run``
~~~~~~~
Execute the program in memory

``sgn``
~~~~~~~
Returns the sign of the specified value

``sin``
~~~~~~~
Returns the trigonometric sine of the specified value

``sleep``
~~~~~~~~~
Pauses the program for a specified amount of seconds

``space$``
~~~~~~~~~~
Returns a string of specified Number value of spaces

``spa``
~~~~~~~
Returns a string of specified Number value of spaces

``spc$``
~~~~~~~~
Returns a string of specified Number value of spaces

``spa``
~~~~~~~
Returns a string of specified Number value of spaces

``sqr``
~~~~~~~
Returns the square root of the specified value

``sqrt``
~~~~~~~~
Returns the square root of the specified value

``stop``
~~~~~~~~
Ralts the program and returns to the basic interpreter

``str$``
~~~~~~~~
Returns a string representation of the specified value

``sys``
~~~~~~~
Returns various system values

``string$``
~~~~~~~~~~~
Repeats a string n times

``tab``
~~~~~~~
Returns the specified amount of spaces

``tab$``
~~~~~~~~
Returns the specified amount of spaces

``tan``
~~~~~~~
Returns the trigonometric tangent of the specified value

``tim``
~~~~~~~
Returns the current second, minute, hour, day or year depending on the numerical value passed

``time$``
~~~~~~~~~
Returns the local system time

``timer``
~~~~~~~~~
Returns the number of seconds since midnight

``typ``
~~~~~~~
Returns the type of the next record in a file

``troff``
~~~~~~~~~
Stops tracing of program statements

``tron``
~~~~~~~~
Starts tracing of program statements

``ups$``
~~~~~~~~
Returns the uppercase value of the given string

``user$``
~~~~~~~~~
Returns the current logged in user

``width``
~~~~~~~~~
Returns your terminal width

``val``
~~~~~~~
Returns the numerical value of the specified string value


4. Detailed overview of Commands
--------------------------------

``ABS(n)``
~~~~~~~~~~
Returns the absolute value of the specified value n::

	PRINT ABS(-40)
	 40


``ASC(character)``, ``NUM(character)``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Returns the ASCII-Code for its equivalent character::

	10 PRINT ASC(" ")
	 32

``ARG$``
~~~~~~~~

A string variable this is populated with a string containing the command line arguments
when a BASIC program is run from the shell command prompt::

	@program foo bar
 	 PRINT ARG$
	  foo bar

``ATN(n)``
~~~~~~~~~~
Returns the arctangent of the specified value n::

	PRINT ATN(40)
	 1.546


``BRK(n)``
~~~~~~~~~~
Enables and disables the break key::

	Y=BRK(0):REM break is disabled


``CHR$(n)``
~~~~~~~~~~~
Convert an ASCII-Code (n) to its equivalent character::

	PRINT CHR$(66)
	 B


``CINT(n)``
~~~~~~~~~~~
Returns the nearest integer of the specified value (9.5 becomes 10)::

	PRINT CINT(5.7)
	 6


``COLOR(a, b)``
~~~~~~~~~~~~~~~
Changes the background(b) and/or foreground(a) color of the terminal::

	COLOR 3, 4
	PRINT "Hello"
	 (prints Hello with blue(b) background and yellow(a) foreground text)
     (a List of possible Colors can be found with the command "show colors")
<underwood remember to put something about ansi escape sequences here!>

``COS(n)``
~~~~~~~~~~
Returns the cosinus of a specified value (n) in radians::

	PRINT COS(67)
	 -0.517769799789505

``CSNG(n)``
~~~~~~~~~~~
Convert a specified value(n) to a single precision number::

	PRINT CSNG("3.45")
	 3.450


``DATA n...``
~~~~~~~~~~~~~
Store the numeric and string constants that are accessed by the program ``READ`` statements::

	DATA 4.1, 5.6, 9.98
	READ A, B, C
	PRINT A, B, C
	 4.100          5.600          9.980


``DEF FNname(Argument) = Expression``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Define a function with the Name 'FNname' which accept an 'Argument' and returns the defined expression. Function name
must always begin with FN::

	10 DEF FN square(x)=x^2
	20 DEF FNcube(x) = x^3
	30 PRINT FNsquare(5),FNcube(5)
	RUN
	 25       125


``DEFDBL (variable)``
~~~~~~~~~~~~~~~~~~~~~
Declare a variable as double precision number::

	DEFDBL Variable


``DEFINT (Variable)``
~~~~~~~~~~~~~~~~~~~~~
Declare a variable as integer number::

	DEFINT Variable


``DEFSNG (Variable)``
~~~~~~~~~~~~~~~~~~~~~
Declare a variable as single precision number::

	DEFSNG Variable


``DEFSTR (Variable)``
~~~~~~~~~~~~~~~~~~~~~
Declare a variable as string::

	DEFSTR Variable


``DIM (Variable)``
~~~~~~~~~~~~~~~~~~
Define an array of a fixed size::

	DIM Variable(n)

This would define an array called ``Variable`` with a maximum size of ``n``.


``DIR$``
~~~~~~~~
Returns the filenames in your local directory, separated by spaces::

	PRINT DIR$


``EXP(n)``
~~~~~~~~~~
Return the base of natural logarithms to the power of ``n``::

	PRINT EXP(13)
	 442413.392


``FOR (variable) = (startValue) TO (maxValue) [STEP n]``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Execute a series of instructions a specified number of times in a loop::

	10 FOR I = 1 TO 40
	20  PRINT I
	30 NEXT I
This would run 40 times and output every time the current counter. It would increase ``I`` everytime by 1.
::
	10 FOR I = 1 TO 40 STEP 2
	20  PRINT I
	30 NEXT I
This would run 40 times and output every time the current counter. It would increase ``I`` everytime by 2.


``GOSUB (LineNumber)``
~~~~~~~~~~~~~~~~~~~~~~
Branch to a subroutine and return::

	10 GOSUB 100
	20 PRINT "Now im back from the Subroutine"
	30 END
	100 REM Subroutine starts here
	110 PRINT "Iam now in the Subroutine"
	120 RETURN
	 Iam now in the Subroutine
	 Now im back from the Subroutine


``GOTO (LineNumber)``
~~~~~~~~~~~~~~~~~~~~~
Branch unconditionally out of the normal program sequence to a specified line number::

	10 PRINT "Hello World!";
	20 GOTO 10


``HEIGHT``
~~~~~~~~~~
Returns your terminal height::

	10 PRINT height
	 42


``HEX$ (n)``
~~~~~~~~~~~~~
Returns a string which represents the hexadecimal value of ``n`` value::

	10 PRINT HEX$(127)
	 7F


``IF expression THEN statements``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Make a decision regarding program flow based on the result of a returned expression::

	10 K = 3
	20 J = 10
	30 IF J > K THEN PRINT "J is bigger than K"
	 J is bigger than K


``INKEY$``
~~~~~~~~~~
Returns one character read from the terminal. It will wait till any character is being typed::

	10 A$ = INKEY$
	20 PRINT A$


``INPUT Prompt, Variable`` / ``INPUT FileNo, Variable``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Shows prompt and reads input from the user's terminal and saves it into a variable::

	10 INPUT "Enter something>", A$
	20 PRINT A$

Reads a Line from an open File and saves it into variable::

	10 INPUT# 1, A$
	20 PRINT A$


``INSTR(string$, searchFor$, startPos)``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Returns the position (starting with 0) of a substring in a string::

	10 TEXT$ = "Hello World"
	20 SEARCHFOR$ = "W"
	30 PRINT INSTR(TEXT$, SEARCHFOR$, 0)
	 6


``INT (n)``
~~~~~~~~~~~
Truncate an value to a whole number::

	10 PRINT INT(5.6)
	 5


``ITM(fileNumber)``
~~~~~~~~~~~~~~~~~~~
Returns the number of the data item currently pointed to in the current record of file ``fileNumber``.
In Telehack BASIC this will almost always be 1.
::

	10 PRINT #1;A,B,C
	20 READ #1,1;A
	30 PRINT REC(1),ITM(1)
	 1            2


``LEFT$(string$, Number)``
~~~~~~~~~~~~~~~~~~~~~~~~~~
Returns a string that comprises the left-most specified number characters of a specified string::

	10 A$ = "Hello World"
	20 B$ = LEFT$(A$, 5)
	30 PRINT B$
	 Hello


``LEN(String$)``
~~~~~~~~~~~~~~~~
Returns the number of characters in the specified string::

	10 A$ = "Hello World"
	20 PRINT LEN(A$)
	 11


``LET Variable = Value``
~~~~~~~~~~~~~~~~~~~~~~~~
Assigns a value to a variable::

	10 LET A = 12345
	20 PRINT A
	 12345


``LIN(number)``
~~~~~~~~~~~~~~~
Returns number of new lines::

	10 PRINT "A" LIN(2) "B"
	 A

	 B


``LOCATE y, x``
~~~~~~~~~~~~~~~
Change the cursors position to ``y``, ``x``::

	10 LOCATE 5, 5


``LOG(n)``
~~~~~~~~~~
Returns the natural logarithm of ``n``::

	10 PRINT LOG(6)
	 1.792


``LOG10(n)``
~~~~~~~~~~~~
Returns the natural logarithm of ``n`` (Base 10)::

	10 PRINT LOG10(6)
	 0.778


``MID$(String$, n, [l])``
~~~~~~~~~~~~~~~~~~~~~~~~~
Returns a string of ``l`` characters from ``String$`` beginning with the ``n`` character::

	10 A$ = "Hello World"
	20 PRINT MID$(A$,3,3)
	 llo


``NINT(n)``
~~~~~~~~~~~
Returns the nearest integer of the specified value (9.5 becomes 9)::

	10 PRINT NINT(5.6)
	 6


``NUM(string$)``
~~~~~~~~~~~~~~~~
Returns the ASCII value of the first character in a string::

	10 PRINT NUM("A")
	 65


``OCT$(n)``
~~~~~~~~~~~
Returns a octal value of ``n``::

	10 PRINT OCT$(66)
	 102


``OPEN filename, AS fileNumber``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Opens a file::

	 10 OPEN "filename.txt", AS #1


``PEEK(n)``
~~~~~~~~~~~
Read a value from the specified memory location ``n``::
 
	10 PRINT PEEK(1300)
	 83


``POKE n, m``
~~~~~~~~~~~~~
Write a byte of data ``m`` into the specified memory location ``n``::

	10 POKE 1300, 255


``POLKEY$``
~~~~~~~~~~~
Returns one character read from the terminal. when no key is hit within one second, it returns an empty string::

	10 A$ = POLKEY$
	20 PRINT A$


``POS(string1$,string2$)``
~~~~~~~~~~~~~~~~~~~~~~~~~~
Returns the position of ``string2$`` in ``string1$`` indexed from 1 or 0 if not found::

	10 A$="ABCDE"
	20 PRINT POS(A$,"CD")
	 3


``PRINT expression``
~~~~~~~~~~~~~~~~~~~~
Prints an expression on the screen

``PRINT# fileNumber, expression``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Prints an expression to an open file

``PRINT #fileNumber[,recordNumber]; expression``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Prints an expression to an open file at the specified record

``PRINT #fileNumber[,recordNumber];END``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Prints an ``EOF`` mark to a file, truncating the file at that record::

	10 A = 5
	20 B = 10
	30 PRINT A + B
	 15

	10 A$ = "Hello "
	20 B$ = "World"
	30 PRINT A$;
	40 PRINT B$
	 Hello World
(Adding a ``;`` at the end of ``PRINT`` does not create a newline)
::
	10 PRINT# 1, "Iam writing into a file"

	10 PRINT #1;A$
	20 PRINT #1,1;"Overwriting A$ in record 1"
	30 PRINT #1,1;END : REM Truncates file at record 1
(notice the position of the ``#`` and the space in the different forms of file access)
 
 
``R2D(n)``
~~~~~~~~~~
Converts radians ``n`` to degrees::

	10 PRINT R2D(1.2)
	 68.755


``READ #fileNumber[,recordNumber];variables``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Read a value from ``DATA`` or a file and assign them to variables::

	10 DATA 4.1, 5.6, 9.98
	20 READ A, B, C
	30 PRINT A, B, C
	 4.100          5.600          9.980

	10 READ #1;A$
	20 READ #1,4;B$

``REC(n)``
~~~~~~~~~~
Returns the current record number (line number) in the specified file. (starts with 1)::

	10 OPEN "telehack.txt", AS #1
	20 INPUT# 1, DUMP$
	30 INPUT# 1, DUMP$
	40 INPUT# 1, DUMP$
	50 PRINT REC(1)
	60 CLOSE #1
	 3


``RENUMBER [start,[inc]]``
~~~~~~~~~~~~~~~~~~~~~~~~~~
Renumbers the statements of the current program in memory. When optional parameters are not specified number starts at 10 and increments by 10 for each line. Can be abbrieviated to ``REN`` or ``RENUM``. Useful if you want to add more lines between existing statements::

	1 GOTO 2
	2 END
	RENUMBER
	LIST
	10 GOTO 20
	20 END

``RESTORE``
~~~~~~~~~~~
Allow ``DATA`` statements to be reread::

	10 DATA 4.1, 5.6, 9.98
	20 READ A, B, C
	30 PRINT A, B, C
	 4.100          5.600          9.980
	40 RESTORE
	50 READ A, B, C
	60 PRINT A, B, C
	 4.100          5.600          9.980


``RIGHT$(String$, n)``
~~~~~~~~~~~~~~~~~~~~~~
Returns the rightmost number ``n`` characters of the specified ``String$``::

	10 A$ = "Hello World"
	20 PRINT RIGHT$(A$, 5)
	 World


``RND(n)``
~~~~~~~~~~
If ``n < 0``, returns a random number in the interval ``[0, 1]`` seeded by ``INT(n)``. If ``n = 0``, returns a random number in the interval ``[0, 1]``. If ``n > 0``, returns a random number in the interval ``[0, INT(n)]``::

	10 PRINT RND(-5)
	20 PRINT RND(0)
	30 PRINT RND(5)
	 0.249
	 0.912
	 2.376


``SGN(n)``
~~~~~~~~~~
Returns the sign of ``n``::

	10 PRINT SGN(5)
	20 PRINT SGN(0)
	30 PRINT SGN(-7)
	 1
	 0
	 -1


``SIN(n)``
~~~~~~~~~~
Returns the trigonometric sine of ``n`` in radians::

	10 PRINT SIN(36)
	 -0.991778853443116


``SLEEP n``
~~~~~~~~~~~
Pauses the program for ``n`` seconds::

	10 SLEEP 5


``SPACE$(n)``, ``SPC$(n)``, ``SPA(n)``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Returns ``n`` spaces::

	10 PRINT "ABC" SPACE$(10) "ABC"
	 abc          abc


``SQR(n)``
~~~~~~~~~~
Returns the square root of ``n``::

	10 PRINT SQR(36)
	 6


``STOP``
~~~~~~~~
Halts the program and returns to the basic interpreter. Useful for debugging programs.


``STR$(n)``
~~~~~~~~~~~
Returns a string representation of ``n``::

	10 PRINT STR$(12345)
	 12345


``STRING$(n, string)``
~~~~~~~~~~~~~~~~~~~~~~
Repeats a string ``n`` times::

	10 PRINT STRING$(10, "A")
	 AAAAAAAAAA


``TAB(n), TAB$(n)``
~~~~~~~~~~~~~~~~~~~
Returns ``n`` spaces::

	10 PRINT "ABC" TAB$(10) "ABC"
	 abc          abc


``TAN(n)``
~~~~~~~~~~
Returns the trigonometric tangent of ``n`` in radians::

	10 PRINT TAN(38)
	 0.310


``TIM(n)``
~~~~~~~~~~
Returns values of time and date depending on ``n``

- ``0`` - current minute (0-59)
- ``1`` - current hour (0-23)
- ``2`` - current day (1-366)
- ``3`` - current year (0-99)
- ``4`` - current second (0-59)

Example::

	10 PRINT TIM(0)
	 29


``TIME$``
~~~~~~~~~
Returns the local system time::

	10 PRINT TIME$
	 07:49:38


``TIMER``
~~~~~~~~~
Returns the number of seconds since midnight::

	10 PRINT TIMER
	 28210


``TYP(n)``
~~~~~~~~~~
Returns the type of the next record in a file.

- ``1`` - numeric data (not currently working)
- ``2`` - string data
- ``3`` - end of file/data

Example::

	10  REM CREATE A FILE FOR TESTING
	20  FILENAME$ = "TEST" + STR$(INT(RND(1)*128*2)) + ".TXT"
	30  OPEN FILENAME$, AS #1
	40  REM POPULATE FILE WITH TEST DATA
	50  PRINT# 1, "some text"
	60  REM SAVE FILE
	70  CLOSE #1
	80  REM TEST TYP() COMMAND
	90  OPEN FILENAME$, AS #1
	100  PRINT TYP(1)
 	 2
	110  REM ADVANCE ONE RECORD
	120  INPUT# 1, DUMP$
	130  PRINT TYP(1)
	 3
	140  CLOSE #1


``TROFF``
~~~~~~~~~
Stops tracing of program statements. Useful for debugging.


``TRON``
~~~~~~~~
Starts tracing of program statements. Useful for debugging.


``UPS$(string$)``
~~~~~~~~~~~~~~~~~
Returns the uppercase value of the given ``string$``::

	10 PRINT UPS$("hello")
	 HELLO


``USER$``
~~~~~~~~~
Returns the current logged in user::

	10 PRINT USER$
	 archer


``WIDTH``
~~~~~~~~~
Returns your terminal width::

	10 PRINT width
	 141


``VAL(String$)``
~~~~~~~~~~~~~~~~
Returns the numerical value of the specified String$::

	10 PRINT VAL("12345")
	 12345

