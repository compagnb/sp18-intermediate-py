## Week 1: OBJECTS & CLASSES
* **Objects** are a way of organizing code in a program and breaking things down to make it easier to think about complex ideas.
* **Classes** define classes (types of objects, groups) 

### BREAKING THINGS INTO CLASSES
* Objects are defined by classes - a to do this is to classify objects into groups
* Use classes to organize bits of code
* An object is like a “member” of a class
```python
class Things:
    pass
```
* We define classes by using the **class** keyword followed by a name. When we create classes we start with the broadest class first. In this case, we use the keyword **pass** to let Python know we do not have any more information for this class at this time. 

### CHILDREN & PARENTS
* If a class is part of another class it’s a **child** of that class, and the other class is it’s **parent**. 
```python
class InAnimate(Things):
    pass
class Animate(Things):
    pass
```
* To tell Python that a class is a **child** of another class we add the name of the **parent** in parenthesis after the name of our new class. 

### ADDING OBJECTS TO CLASSES
* An object of a class is also referred to as an instance of a class
```python
geoffrey = Giraffes()
```
* This code tells Python to create an object in the Giraffes class and assign it to the variable **geoffrey**.
* Like a function there are parenthesis after the class name. This is so we can use parameters when we create new objects.

### FUNCTIONS OF CLASSES
* We define a function in a class the same way we call one normally, but the indentation is beneath the class function.
```python
class SillyClass:
    def functionOne():
        print('this is function 1')
    def functionTwo():
        print('this is function 2')
```
* We can add **characteristics** to each class to say what it can and cannot do. A characteristic is a trait that all of the members of the class (and its children) share.

* These characteristics can be thought of as actions or functions - things an object of that class can do. The self parameter is a way for one function to call another function in the class (and in the parent class).

* We often created classes with functions that do nothing (using pass) as a way to figure out what the class should do, before getting into the details of the individual functions. 
* Each class can use the characteristics (functions) of its parent, so we don’t have to make really complicated class – we put the functions at the highest parent where the characteristic applies.

### WHY USE OBJECTS & CLASSES
* After we create an object, we can call and run functions provided by its class (and its parents class). We call the function by using the dot operator and the name of the function like this:
* We can create more objects, and because we are using objects and classes we tell Python exactly which object to do what. 


### OBJECTS AND CLASSES IN PICTURES
* When we use turtle.pen() the turtle module uses the Pen class. 
* Now that the objects are created, they become powerful… we can call functions on each and they will move independently (without effecting any of the others)!
* Every time we call turtle.pen(), we create a new independent object. Since they area all objects of the pen class, we can use the same functions on each object… but because they are objects we can move each independently. 
* What happens when we create an object with the same variable name as the one we have already used?


### INHERITED FUNCTIONS
* Each class can use the functions of its parent (and their parents), so the class at the lowest level actually has the least amount of functions because it can use its parent’s functions, and its parent’s parent’s function.


### FUNCTIONS CALLING OTHER FUNCTIONS
* To have a function called in a class we use the self parameter to allow us to call another function. Here is an example:


* Often we will write functions that will do something useful, which we can then use inside another function. 
* By calling functions in this way we can call a single function that does more then just one thing. 


### INITIALIZING AN OBJECT
* Sometimes when we create an object we want to set some values (also called properties) for later use. When we initialize the object, we are really just getting it ready for use. 
* __init__ is a special type of function in Python classes and must have this name. It sets the properties for an object when it is first created. It is automatic (we don’t have to call it as a function!)


* Just like the other functions we created within the class, the __init__ function needs the first parameter to be self. Next, we set the parameter to the object variable. Just as we call the object functions using self, variables in the class are also accessed using self. 


* When we create an object of a class with an __init__ function, it has the same effect as actually calling the function, so we need to include a parameter to pass.
* When we create an object of a class, we can refer to its variables or functions using the dot operator and the name of the variable or function we want to use. 


* In-class Exercises/Challenges: 
    * Create a class that can be used for all the drivers used in Mario Kart
    * Create a class that can be used for all the karts used in Mario Kart
    * Using the turtle class create a generative/fractal design
    * Create a class that provides methods for drawing the following shapes: Square, Circle, Octagon, Pentagon.
    * Modify the shapes class to allow for the options of changing the fill color, border, size, etc.
    * Create a class to build a Maze.