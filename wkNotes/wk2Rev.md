## Week 2 
![children](../imgs/darth.gif)

### CHILDREN & PARENTS
* If a class is part of another class it’s a **child** of that class, and the other class is it’s **parent**. 
![parent](../imgs/parent.png)
* To tell Python that a class is a **child** of another class we add the name of the **parent** in parenthesis after the name of our new class. 
```python
class InAnimate(Things):
    pass
class Animate(Things):
    pass
```

### INHERITED FUNCTIONS
* Each class can use the functions of its parent (and their parents), so the class at the lowest level actually has the least amount of functions because it can use its parent’s functions, and its parent’s parent’s function.
![Inherit](../imgs/inherit.png)

### OBJECTS AND CLASSES IN PICTURES
* When we use **turtle.Pen()** the turtle module uses the Pen class. 
```python
import turtle
donatello = turtle.Pen()
rafael = turtle.Pen()
```
* Now that the objects are created, they become powerful… we can call functions on each and they will move independently (without effecting any of the others)!
```python
donatello.forward(50)
donatello.right(90)
donatello.forward(20)
rafael.left(90)
rafael.forward(100)
```
* Every time we call **turtle.Pen()**, we create a new independent **object**. Since they area all objects of the **Pen** class, we can use the same functions on each **object**… but because they are objects we can move each independently. 
* What happens when we create an object with the same variable name as the one we have already used?

### In-class Exercises/Challenges: 
    * Create a class that can be used for all the drivers used in Mario Kart
    * Create a class that can be used for all the karts used in Mario Kart
    * Using the turtle class create a generative/fractal design
    * Create a class that provides methods for drawing the following shapes: Square, Circle, Octagon, Pentagon.
    * Modify the shapes class to allow for the options of changing the fill color, border, size, etc.
    * Create a class to build a Maze.

### VOCABULARY:
* child 
* parent 