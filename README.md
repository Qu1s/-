# Py3_Stuff
Hi, GitHub, it's my repository for Python3 small scripts 

Generators:
    - Markov's chain generating the chain of different words from book.txt
    To test with your own text, change book.txt
    After start the programm you should wait while console will write "Done"
    It means, that you can type "w" if you want generate some text
    Max lenght of sentence is 20 words.


Polynom:
    - Generating polynom with two different ways(Pascal's triangle, method of unknown coefficients)
    Example - F(01001011):
    1)
     x y z   F     Треугольник Паскаля 
    -----------------------------------
     0 0 0   0       0 1 0 0 1 0 1 1 
     0 0 1   1        1 1 0 1 1 1 0 
     0 1 0   0         0 1 1 0 0 1 
     0 1 1   0          1 0 1 0 1 
     1 0 0   1           1 1 1 1 
     1 0 1   0            0 0 0 
     1 1 0   1             0 0 
     1 1 1   1              0 

     F = z + yz + x

     2)
     F(0,0,0) = a0 = 0
     F(0,0,1) = a0 + a3 = 1
     F(0,1,0) = a0 + a2 = 0
     F(0,1,1) = a0 + a2 + a3 + a6 = 0
     F(1,0,0) = a0 + a1 = 1
     F(1,0,1) = a0 + a1 + a3 + a5 = 0
     F(1,1,0) = a0 + a1 + a2 + a4 = 1
     F(1,1,1) = a0 + a1 + a2 + a3 + a4 + a5 + a6 + a7 = 1

     a0 = 0, a1 = 1, a2 = 0, a3 = 1, a4 = 1, a5 = 0, a6 = 0, a7 = 0, 
     F = z + yz + x


Recurrence sequence:
    - You can calculate n-number of different sequence. You must enter coefficients of variable, first numbers of sequence and number
    Example - Fibonacci sequence:
        F(n) = F(n-1) + F(n-2)  (coefficients are 1 and 1)
        F(0) = 0, F(1) = 1      (first numbers are 0 and 1)
        F(1000)                 (n-number = 1000) 