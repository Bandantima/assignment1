#Qu1.What does an empty dictionarys code look like?
Ans:Two curly bracket with no elements {}

#Qu2.What is the value of a dictionary value with the kry 'foo' and the value 42?
Ans:{'foo':42}

#Qu3.What is the most significant distinction between a dictionary and a list ?
Ans:The item stored in a dictionary are unordered ,while the items in a list are ordered.

#Qu4.What happens if you try to access spam['foo'] if spam is {bar:100}?
Ans:  spam{'bar':100}
      spam['foo']
      we get a key error.

#Qu5.If a dictionary is stored in a spam ,what is the difference between the expressions 'cat' in spam and 'cat' in
    spam.keys()?
Ans:There is no difference at all between both because the 'in' operator checks whether a value exists as a key in
    dictionary or not.

#Qu6.If a dictionary is stored in spam,what is the difference between the expressions 'cat' in spam and 'cat' in
      spam.values()?
Ans:'cat' in spam checks whether there is a 'cat' key in the dictionary available while 'cat' in spam.values() checks
      whether there is a value'cat' for one of the keys ib spam.

#Qu7. What is a shortcut for the following code?
      if 'color' not in spam['color'] ='black'
Ans:spam.setdefault('color','black')

#Qu8.How do you "pretty print" dictionary valuesusing which module function?
Ans: pprint.pprint() 