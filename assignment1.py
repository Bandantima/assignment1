import code

Qu.1- In the below elements which of them are values or an expression? eg. values can be integer or string and
      expressions will be mathematical operators.
Ans-  Values-        'hello',-87.8,6
      Expression-     *,-,/,+


Qu.2- What is the difference between string and variable.
Ans-             String                                            Variable
    1.A string is a type of information you would        1.A variable is a symbolic name that is a pointer or reference
      store in a variable.                                 to an object.
        eg.     'ineuron'                                     eg. x
    2.A string is a word inclosed with "   "             2.A variable is a store of information.
    3.Value of string may change using operators.        3.Value of a variable may not change within the content of
                                                           mathematical problem or experiment .

Qu.3-Describe three different data types.
Ans-   1.Integer-  A integer is a whole number that can be positive ,negative or zero.Example of integers are 1,2,3,-7,
                    7,etc. Example of number that are not integers are 4/5,9/7,-56.49 etc.The set of integers is defined
                    as      x={.......,-3,-2,-1,0,1,2,3,........}
                    In mathematical equations , unknown or unspecified integers are represented by lower case.Integers
                    can be binary, octal and hexadecimal values eg. 0121, O0121,OX121.
       2.Float-    In python, floating points are positive and negative numbers with a fractional part denoted by the
                   decimal symbol or scientific notation E or e .
                   eg. 1234.56,-1.554
                   We csan use float() to convert string into float eg.  float('5.6')
                                                                           5.6
                   Floats has maximum size depends on your system .The float beyonds its maximum size referred as 'inf'
       3. Boolean-  Boolean data type is one of the builtin data type in python.It is used to represent the truth value
                   of expression .In binary, 1 corresponds to true, while 0 corresponds to false.These values can be
                   manipulated by the use of boolean operators which include AND,OR and NOT.


Qu.4- What is an expression made up of ?What do all expressions do?
Ans-  An expression is a combination of operators and operands that is interpreted to produce some other value and it is
      constructed according to the syntax of the language.
                                          Expressions are representations of value .They are different from statement
      in the fact that statements do something while expressions are representations of value.


Qu.5- This assignment statements ,like spam=10. What is the difference between an expression and a statement ?
Ans-       Expression                                              Statement
    1. It is a combination of values,variables,      1.An instruction that a python interpretor can execute is called
       operations and functions that always             a statement.
       produces a result value.                             eg.    x=3
       eg.x=5                                                      Print(x)
          y=3                                                       3
          z=x+y                                         The first line is an assignment statement that gives a value
       here,x=5 is an expression as same y=5            to x .The second line is a print statement that displays the
       ,z=x+y is also It simply means to                value of x.
       calculate the values of something.               Some other kinds of statement in python are if statement,else
                                                        statement,while statement,for statement,import statement
    2. The execution of a expression doesnot         2.Execution of a statement changes state and sometimes may not
       changes state and returns a value.               produce or display result value.


Qu.6- After running the following code ,what does the variable bacon contain?
      bacon=22
      bacon+1
Ans-  It gives 23 as an execution code.


Qu.7- What should values of the following two terms be ?
      'spam'+'spamspam'
      'spam'*3
Ans-  Both terms give 'spamspamspam'


Qu.8- Why is eggs a valid variable name while 100 ia invalid?
Ans- Because we cannot give a variable an integer name .If we should begin with a string like alphabet name then integer
     e100 or eggs100 is valid.


Qu.9- What three funtions can be used to get the integer ,floating point number or string version of a value?
Ans-  int(),float(),str() functions can be used to get the integer,floating point number or string version of a value.


Qu.10-Why does this expression cause a error ?How can you fix it?
     'I have eaten' + 66 +'burritos'
Ans-  Because 99 ia a integer it cannot be concatenated with strings , if we have to concetenate it we need to do
      typecasting.


