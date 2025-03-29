# Life Path Numbers - Functional Decomposition

## Instructions

Complete each step of this plan _before_ you begin coding. 
You do not need to fix it later, if it does not match your final code.
In fact, if your plan exactly matches your code, I know you didn't write it before you started coding.

## Step 1: 

List out the highest level components of the algorithm (i.e., your `main` function). 
I've written the first one for you:
```
    1. Ask the user to enter their birth year.
        1a. CONVERT the year to 4 (individual digits) and SUM. | RETURN an output [A]
    2. Ask the user to enter their birth month.
        2a. CONVER the birth month from month to (individual) digits and SUM the digits. 
        [EXCEPT IF] the month == 11, then don't SUM. | RETURN an output [B]
    3. Ask the user to enter their birthday day. 
        3a. COVERT, the day to individual digits and SUM them.
        [EXECPT IF] the day == 11, 22 | RETURN an output [C]
    4. SUM [A] + [B] + [C] = [D]
        4a. Break this output [D] into individual digits and sum them.
        [EXEC[T IF] the output [D] is 11, 22, 33.
```
## Step 2: 

Look at each item above, and determine if you can implement it with code as it is written. 
If you answered No to any step, it needs further decomposed. 

Do that here, numbering them 
1.a., 2.a., 2.b. etc. I would expect the life path numbers algorithm I described in the 
Google Doc to appear somewhere in this section.

Repeat this process of breaking down subtasks into sub-subtasks, as deep as you feel 
is necessary to be able to implement all subtasks, sub-subtasks, etc. You may not 
need to break down the subtasks to this level on this assignment; future assignments you might!

**NOTE:** You may not need the sample ones below; they are to help you with formatting.
```
1. Ask the user to enter their birth year. 
[?] Can I implement this as code? | YES // NO.
    YES. 

1a. CONVERT the year to 4 (individual digits) and SUM those and | RETURN an output [A] 
to be used elsewhere.
[?] Can I implement this as code? | YES // NO.
    YES.

2. Ask the user to enter their birth month.
[?] Can I implement this as code? | YES // NO.
    YES.

2a. CONVERT the birth month from month to (individual) digits and SUM the digits. 
[EXCEPT IF] the month == 11, then don't SUM. | RETURN an output [B]
[?] Can I implement this as code? | YES // NO.
    YES.

3. Ask the user to enter their birthday day. 
[?] Can I implement this as code? | YES // NO.
    YES.

3a. COVERT, the day to individual digits and SUM them.
[EXECPT IF] the day == 11, 22 | RETURN an output [C]
[?] Can I implement this as code? | YES // NO.
    YES.

4. SUM [A] + [B] + [C] = [D]
[?] Can I implement this as code? | YES // NO.
    YES.


4a. Break this output [D] into individual digits and sum them.
[EXECPT IF] the output [D] is 11, 22, 33.
[?] Can I implement this as code? | YES // NO.
    YES.


######################TEMPLATE
    1. Ask the user to enter their birth year.
        1.a. ...
    
        1.b. ...
```
```
    2. ...
        2.a. ...
    
        2.b. ...
            2.b.i. ...
            
            2.b.ii. ...
```
## Step 3: 

Planning is complete; refer back to this document frequently while coding to remind yourself of the 
larger goal you are trying to solve. Edit the plan as you code, if it helps you keep tabs on what tasks remain. 

Commit and push your PLAN.md file to Github by **Friday's class!**