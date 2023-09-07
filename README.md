# Challenges


| Question   | Jump to it                                                              | Source |
|------------|-------------------------------------------------------------------------|--------|
|Question 1-3| [Link](https://github.com/VazLucas/leetcode-challenges#compass)         | Compass|
|Question 1-4| [Link](https://github.com/VazLucas/leetcode-challenges#uninter)         | Uninter|


___
# Compass

<details> <summary> Question 1 </summary>
  
> Main language: JAVA
> Must output the student name that failed in the class respecting the number of problems solved and the name ordered alphabetically

> **First tiebraker** => number of problems solved
>
> **Second tiebraker** => last name alphabetically sorted

<details> <summary> How to solve it </summary>

- Create one **Array List** to store the students' name and another one to store how many problems were solved;
  - With an Array List will be easier <u> remove data</u>, <u> add data</u> and <u>comparing it</u>. The methods most used in the code.
  ~~~java
  ArrayList<Integer> problemSolved = new ArrayList<Integer>();
  ArrayList<String> studentsName = new ArrayList<String>();
  ~~~
- Instantiate a **Scanner Class** to receive the data input;
  ~~~java
   Scanner source = new Scanner(System.in);
  ~~~
  - With a loop that could be a **for** because we already know the number of students, each of them will be inserted in a different line, we will add:
    - Every single integer with the method <u>.nextInt()</u> (of the Scanner Class) to the problems Array List;
    - Every single string with the method <u>.next()</u> (of the Scanner Class)  to the students name Array List;
    ~~~java
    for (int i = 0; i < studentsQuantity; i++) {
    studentsName.add(source.next());
    problemSolved.add(source.nextInt());
    }
    ~~~
    - HERE COMES THE MAGIC, respecting the tiebreakers:
      - Using the **j** and **i** variables, the code will compare the values in the indexes that **j** and **i** points to
      ~~~java
      for (int j = problemSolved.size() - 1, i = 0; j > 0; j--)
      ~~~
      - The first if statement will remove from students name Array List and from the problems solved Array List the value in the **i** index if it is greater than the value in the **j** index 
      ~~~java
      if (problemSolved.get(i) > problemSolved.get(j)) {
      problemSolved.remove(i);
      studentsName.remove(i);
      }
      ~~~
      - In line 22, if the value in the **i** index is lower than the value in the **j** index, the values in the **j** index will be removed from both Array Lists.
      ~~~java
      else if (problemSolved.get(i) < problemSolved.get(j)) {
      problemSolved.remove(j);
      studentsName.remove(j);
      }
      ~~~
      - The last and most important, the piece of code below checks if both values (i and j) are equal to each other.
      ~~~java
      else if (Objects.equals(problemSolved.get(i), problemSolved.get(j)))
      ~~~
      - If so, it means that both students got the same number of problems solved, and we will go for the second tiebraker; 
      - The method str1.compareTo(str2) can return 3 distinct values, which can be:
        - An int value of 0 if the string is equal to the other string. 
          - A case which will not happen because there are no homonyms
        ~~~java
        else {
        System.out.println("Both students have the same name");
        break;
        }
        ~~~
        - An int value lower than 0 if the string is lexicographically less than the other string
        ~~~java
        else if (studentsName.get(i).compareTo(studentsName.get(j)) < 0) {
        studentsName.remove(i);
        problemSolved.remove(i);
        }
        ~~~
        - An int value greater than 0 if the string is lexicographically greater than the other string (more characters)
        ~~~java
        else if (studentsName.get(i).compareTo(studentsName.get(j)) < 0) {
        studentsName.remove(i);
        problemSolved.remove(i);
        }
        ~~~
        - At the end, the student with the least number os problems solved and with the last name alphabetically sorted will be printed out
        ~~~java
        System.out.println(studentsName.get(0));
        ~~~
  
</details> 
        
</details>
<details><summary> Question 2 </summary>


> Main language: JAVA
> Must output one of the next messages
> - **"Fun"** => if the amount happy faces is greater than the amount of sad faces
> - **"Neutral"** => if the amount of happy faces is equal than the amount of sad faces
> - **"Sad"** => if the amount of happy faces is lower than the amount of happy faces

<details> <summary>How to solve it </summary>
  
- Create an **array** (_elements_) to store each element from the **string** (_line_) separated by whitespaces using the method **.split( )**;
- Instatiate a Scanner Class to read the input;
- With a **string** (_line_) store each .nextLine( )
- With two **int** variables
  ~~~java
  Scanner source = new Scanner(System.in);
  String line = source.nextLine();
  String[] elements = line.split(" ");
  int upsetCount = 0, funCount = 0;
  ~~~
- A **for each loop** is used to count how many `":-("` and `":-)"` are on the **array** (_elements_)
  ~~~ java
  for (String word : elements) {
      if (word.equals(":-(")){
          upsetCount++ ;
      } else if (word.equals(":-)")){
          funCount++;
      }
  }
  ~~~
- Finally, an **if statement** to check the numeric values of `upsetCount` and `funCount`;
  ~~~java
  if (upsetCount==funCount){
      System.out.println("Neutral");
  } else if (upsetCount > funCount) {
      System.out.println("Upset");
  } else {
      System.out.println("Fun");
  }
  ~~~
</details>
  
 
</details>

<details><summary> Question 3 </summary>

 

> Must output the result of an equation
> Main language: JAVA

<details> <summary> How to solve it </summary>

- Instantiate a **Scanner** Class to read the input;
- Create an **array**(_results_) to store each equation's result and then print it out 
~~~ java
Scanner source = new Scanner(System.in);
int result = 0;
List<Integer> results = new ArrayList<>();
int k = 1;;
~~~ 
- A **while** loop to run through every line
~~~ java
while (source.hasNext())
~~~ 
- Some **if statement** to check how many number are on the input and if it respects the constraints
~~~java
if (operandsQuantity < 1 || operandsQuantity > 100) {
break;
}
if (operandsQuantity != 0) {
String equation = source.next();
~~~~
- This particular for loop was made to store the signs presented in the equationOperator.
~~~java
for (int i = 0; i < equationFormatted.length(); i++) {
      equationOperator.add(equationFormatted.charAt(i));
      }
~~~
- Another if statement to check other constraints related to the numbers of operands and how many of them were inserted
~~~java
if (operandsQuantity < equationCounter.size()) {
System.out.println("Exceeded number of operands, you must have inserted " + operandsQuantity + " operands");

} else if (operandsQuantity > equationCounter.size()) {
System.out.println("You must have inserted " + operandsQuantity + " operands");
~~~
- The last part of the code was developed to add or to subtract the value of the result
- Then this value is stored in the array(results)
~~~java
} else{
for(int j=0;j<equationCounter.size();j++){
if(equationOperator.get(j).hashCode()=="-".hashCode()){

result=result-Integer.parseInt((String)equationCounter.get(j));

}else{
result=Integer.parseInt((String)equationCounter.get(j))+result;
}

}
results.add(result);
}
~~~

- A **for each loop** to print each result stored in the **array**(_results_)
~~~java
for (int i : results) {
System.out.println("Test: " + k);
System.out.println(i);
k++;
~~~
</details> 

    
</details>
    
# Uninter

<details> <summary> Question 1 </summary>

> Main language: python
> 
> Receive a string and age, the program must output which institution the person should be studying at

<details> <summary> How to solve it </summary>

1. Variables to receive inputs
```python
name = str(input('Please, type a name:'))
age = int(input('Please, type students age: '))
institution = ''
```
2. If conditional to modify institution variable
```python
if age >= 1 and age <= 5:
    institution = 'kindergarten'
elif age >= 6 and age <= 10:
    institution = 'elementary school'
elif age > 10 and age < 15:
    institution = 'middle school'
elif age > 15 and age < 18:
    institution = 'high school
elif age > 18:
    institution = 'college'
```
3. A print method
```python
   print('The student {} is {} years and is in {}' .format(name, age, institution))
```
5. A simple ``if`` conditional to restart the admissions functions or to stop it
```python
end = int(
    input('Type 0 to continue and another value to stop'))
if end != 0:
    print('End of program')
elif end == 0:
    admissions()
```
</details>

</details>  

<details> <summary> Question 2 </summary>
  
> Main language: python
> 
> Receive a string and convert each vowel into a symbol and make every consonant upper case

<details> <summary> How to solve it</summary>
  
1. A for loop is all we need to solve it, but first, we must receive an input as a string:
  
```python
name = str(input('Type a name:'))
```

2. Then each element in that string will be compared within an ``if`` statement:

```python
for i in name:
  if (i == 'a' or i == 'A'):
      convertedName += '@'
  elif (i == 'e' or i == 'E'):
      convertedName += '&'
  elif (i == 'o' or i == 'O'):
      convertedName += '#'
  elif (i == 'i' or i == 'I'):
      convertedName += '!'
  elif (i == 'u' or i == 'U'):
      convertedName += '*'
  else:
      convertedName += i
```

3. As you can see, if the letter is not a vowel it will be added to the variable ``y``. Then just print it:

```python
print(convertedName.upper())
```

</details>
</details>
 
<details> <summary> Question 3 </summary>
  
> Main language: python
> 
> Create an Animal's Hotels game


<details> <summary> How to solve it</summary>

1. Instructions and the first stage
```python
print("Welcome to Animal's Hotels game")
print('Your mission to allocate the guests:')
print('Dog can not be next to a cat')
print('Dog can not be next to a bone!)
print('Cat can not be next to a rat.')
print('Rat can not be next to a cheese.')
print('Unavaible room already have a guest')
print('G – cat')
print('C – dog')
print('R – rat')
print('O – bone')
print('Q – cheese')
print('* - unavailable room')
print('- - available room')
print('           ----------------(First stage)--------------       ')
print('           ----------------Good luck--------------       ')
print('first, allocate the cat and the rat')

print('[ * | * | - | G ]')
print('[ R | - | * | * ]')

rat = int(input('in what room you want to put the rat? '))
cat = int(input('in what room you want to put  cat? '))
```

2. If the player matched his input with the correct answer, the next stage shows up
```python
if (rat == 6 and cat == 3):

  print('congrats, you made it!')

  print('            ----------------(stage 2)--------------       ')

  print('In this stage you must alocate a dog, a bone and another dog')

  print('[ - | * | * | * ]')
  print('[ * | C | - | - ]')

  dog1 = int(input('in what room you want to put the first dog? '))
  bone = int(input('in what room you want to put the bone? '))
  dog2 = int(input('in what room you want to put the second dog? '))
```
3. Then the third stage comes in the same strategy
```python
if ((bone == 1 and dog1 == 7 and dog2 == 8) or (bone == 1 and dog1 == 8 and dog2 == 7)):
  print('congrats, you made it!')
  print('            ----------------(stage 3)--------------       ')
  print('Now your missions is to put a cat, a bone and a rat. ')

  print('[ - | * | * | * ]')
  print('[ - | G | - | * ]')

  cat = int(input('where do you want to put  cat? '))
  bone = int(input('where do you want to put bone? '))
  rat = int(input('and the rat? '))
```
4. The next stages are always confirming the previous round's answers. The last and final stage!
```python
if (rat == 1 and bone == 5 and cat == 7):
  print('                    congrats, you made it!            ')
  print('            ----------------(stage 4)--------------       ')

  print('Now your mission is to alocate two cheeses and a bone')
  print('[ - | - | - | * ]')
  print('[ * | R | * | * ]')

  cheese = int(input('where do you want to put the  first cheese? '))
  bone = int(input('where do you want to put the bone? '))
  cheese2 = int(input('And the last cheese? '))

  if ((bone == 2 and cheese == 3 and cheese2 == 1) or (bone == 2 and cheese == 1 and cheese2 == 3)):
      print('------congrats, you won!------')
```

5. The previous rounds end with these ``else's``
```python
            else:
                print('GAME OVER!!')
        else:
            print('GAME OVER!!')
    else:
        print('GAME OVER!!')
else:
    print('GAME OVER!!')
````
</details>  
  
</details>
<details> <summary> Question 4 </summary>

> Main language: python
> 
> Receive a subscription and show it

<details> <summary> How to solve it</summary>

1. Function to define a voucher number and receive some person's parameters
```python
def subscription():
    number = randint(100, 400)
    person['Voucher'] = number
    voucherlist.append(number)
    if len(set(voucherlist)) == len(voucherlist):
        print('This is your voucher: {}' .format(number))
        person['Name'] = input('What is your name?')
        person['Phone'] = input('What is your phone?')
        person['Email'] = input('What is your email?')
        person['Course'] = input('What course?')
        detail()

        subscribed.append(person.copy())
        del mysub[:]
        mysub.append(person)
    else:
        detail()
        print("Voucher invalid, restart")
        detail()
        start()
```
2. Function to start the application as a menu

```python
def start():

    print('choose 1 to make a new subscription')
    print('choose 2 to show the subscription list')
    print('choose 3 to show your subscription')
    print('choose 0 to end the program')
    choose = input('Type your choice')
    detail()
    if choose == '1':
        subscription()
        start()

    elif choose == '2':
        if not subscribed:

            print('No subscriptions')
            detail()
            start()
        else:
            print(*subscribed, sep='\n')
            detail()
            start()
    elif choose == '0':
        print('Program closed')

    elif choose == '3':
        if not mysub:
            print('Subscription not made')
            detail()
            start()
        else:
            print(mysub)
        detail()
        start()
    else:
        print('Invalid option. Please, select 1, 2 or 0')
        detail()
        start()
```

</details>  
  
</details>
