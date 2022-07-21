#qu1. Is the Python Standard Library included with PyInputPlus?
Ans:No. PyInputPlus is a third-party module and doesn’t come with the Python Standard Library.

#Qu2. Why is PyInputPlus commonly imported with import pyinputplus as pypi?
Ans:This optionally makes your code shorter to type: you can type pyip.inputStr() instead of pyinputplus.inputStr().

#Qu3. How do you distinguish between inputInt() and inputFloat()?
Ans:The inputInt() function returns an int value, while the inputFloat() function returns a float value. This is the difference between returning 4 and 4.0.

#Qu4. Using PyInputPlus, how do you ensure that the user enters a whole number between 0 and 99?
Ans: Call pyip.inputint(min=0, max=99).

#Qu5. What is transferred to the keyword arguments allowRegexes and blockRegexes?
Ans: A list of regex strings that are either explicitly allowed or denied

#Qu6. If a blank input is entered three times, what does inputStr(limit=3) do?
Ans: A list of regex strings that are either explicitly allowed or denied

#Qu7. If blank input is entered three times, what does inputStr(limit=3, default='hello') do?
Ans: The function returns the value 'hello'.
