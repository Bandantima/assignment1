#qu1.What are the escape characters ,and how do you use them?
Ans:Escape character represent characters in string values that would otherwise be difficult or impossible to type into
    code.In  Python strings,the backslash '\' is a special character also called 'escape' character.It is used in
    representing certain whitespace characters;"\t" is a tab,"\n" is a newline and "\c" is a carriage return.

#Qu2.What do escape characters n and t stand for?
Ans:\n is a newline and \t is a tab.

#Qu3.What is the way to include backslash characters in a string ?
Ans:The / escape character will represent a backslash character.

#Qu4.The string "Howl's Moving Castle" is a correct value.Why isn't the single quote character in the word Howl's not
      escaped a problem?
Ans: The single quote in Howl's doesnot escape a problem because we had used double quotes to mark the beginning and
     ending of the string.

#Qu5.How do you write a string of newliness if you don't want to use the n character?
Ans: Multiline strings allow you to use newlines in strings without the \n escape character.

#Qu6.What are the values of the given expressions?
    'Hello,world'[1]   'Hello,world'[0:5] 'Hello,world''[:5] 'Hello,world'[3:]
Ans: 'e'
      'Hello'
      'Hello'
      'lo,world!'

#Qu7.What are the values of the following expressions?
   'Hello.upper()'  'Hello.upper().isupper()'  'Hello.upper().lower()'
Ans: 'HELLO'
      True
      'hello'

#Qu8.What are the values of the following expressions?
    'Remember',remember,the fifth of July.'.split()'-'.join('There can only one.'.split())
Ans:
  'Remember, remember, the fifth of July.'.split()
['Remember,', 'remember,', 'the', 'fifth', 'of', 'July.']
'-'.join('There can only one.'.split())
'There-can-only-one.'

#Qu9.What are the methods for right-justifying ,left-justifying,and centering a string?
Ans:The rjust(),ljust() and center() string methods respectively .

#Qu10.What is the best way to remove whitespace characters from the start or end?
Ans:The lstrip() and rstrip() methods remove whitespace from the left and right ends of  a string.