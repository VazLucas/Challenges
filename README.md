# Challenges


| Question   | Jump to it                                                              | Source |
|------------|-------------------------------------------------------------------------|--------|
| Question 1 | [Link](https://github.com/VazLucas/Challenge1_Compass#code-challenge-1) | Compass|
| Question 2 | [Link](https://github.com/VazLucas/Challenge1_Compass#code-challenge-2) | Compass|
| Question 3 | [Link](https://github.com/VazLucas/Challenge1_Compass#code-challenge-3) | Compass|

___
# Code challenge 1
___ 
> - Main language: JAVA

- Tasks
  - [x] folder creation
  - [x] branch creation
  - [x] start code production
  - [x] question done
  
#### About the challenge

> Must output the student name that failed in the class respecting the quantity of problems solved and the name ordered alphabetically

> **First tiebraker** => number of problems solved
>
> **Second tiebraker** => last name alphabetically sorted

#### How to solve it

- Create one **Array List** to store the students name and another one to store how many problems were solved;
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
        
---

# Code challenge 2
___
> - Main language: JAVA

- Tasks
  - [x] folder creation
  - [x] branch creation
  - [x] start code production
  - [x] question done
  
#### About the challenge

> Must output one of the next messages
> - **"Fun"** => if the amount happy faces is greater than the amount of sad faces
> - **"Neutral"** => if the amount of happy faces is equal than the amount of sad faces
> - **"Sad"** => if the amount of happy faces is lower than the amount of happy faces

#### How to solve it

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
___
# Code challenge 3
___
> - Main language: JAVA

- Tasks
  - [x] folder creation
  - [x] branch creation
  - [x] start code production
  - [x] question done
  
#### About the challenge

> Must output the result of an equation 

#### How to solve it

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
  

>   - State;
>   - Country
#### How to solve it

- Download Mongosh, you can find more about it [here](https://www.mongodb.com/docs/mongodb-shell/);
- Start the executable file in .zip folder;
- Connect to your MongoDB server;
- And then follow the written code.
