# Square Number
Calculation of the difference of the square numbers.

## Basic idea
If you look at the difference between 2 consecutive square numbers, you notice that they only increase by 2. 
This script was created to show this. 

## Example
```Log
(2,1)^2 --> (4,1) : 4 - 1  =  3
(3,2)^2 --> (9,4) : 9 - 4  =  5
(4,3)^2 --> (16,9) : 16 - 9  =  7
(5,4)^2 --> (25,16) : 25 - 16  =  9
(6,5)^2 --> (36,25) : 36 - 25  =  11
(7,6)^2 --> (49,36) : 49 - 36  =  13
(8,7)^2 --> (64,49) : 64 - 49  =  15
(9,8)^2 --> (81,64) : 81 - 64  =  17
(10,9)^2 --> (100,81) : 100 - 81  =  19
```
A complete list up to 1000 can be found here: [Example up to 1000](square_example.txt)

In the log you can imagine it better.

``` Log
3 + 2 = 5 
5 + 2 = 7 
```
And so on. 

## Usage

```PowerShell
python diff_square.py <<START_VALUE>> <<END_VALUE>>
```

Example:
```PowerShell
python diff_square.py 1 3
```

If no configuration is made by the user, the following start values are used. 

```Log
    start = 1
    end = 1001
```
So a configuration is mandatory.

## Python
```Python
for i in range(0,101):
    
    # The tuple consists of the entered numbers.
    tuple_figure = "(" + str(i) + "," + str(i - 1) + ")"+symbol+" -->"
    tuple_square = "(" + str(i**2) + "," + str((i - 1)**2) + ") :"

    # Generates the output for the console
    diff = square[i-1] - square[i-2]
    tuple_ausgabe = str(square[i-1])+" - "+str(square[i-2])

    # Output
    if diff > 0:
        print(tuple_figure, tuple_square, tuple_ausgabe, " = ", diff)
```
Source Code [diff_square.py](diff_square.py)