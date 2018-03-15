## Week 3

![Pikachu Runnng](../imgs/pika.gif)

### BACKGROUNDS & BASIC SPRITES
* We have already begun to use the **Pen()** class within the turtle module, but there are other classes. The **Screen()** class gives us a playground for the turtles to use.

```python
wn = turtle.Screen()
```
* Once we assign an instance of **Screen()**  to a variable, we can start to control more aspects of the area we use the turtles in. 
    * **bgcolor()** allows us to change the background color of the screen
    * **title()** allows us to change the name of the window.
    * **bgpic()** allows us to add a background image 

```python
wn.bgcolor("black")
wn.title("Shapes")
wn.bgpic("stars.gif")
```

### BASIC SPRITES 
* The default setting for the turtle's shape is an **arrow**, but this can be modified to be set as other shapes. To use one of the alternate shapes already registered in the turtle **Screen** shape dictionary. If it is a **registered shape**, use the **shape()** function to set it as one of the following shapes:

```python
t.shape("arrow")
t.shape("turtle")
t.shape("circle")
t.shape("square")
t.shape("triangle")
t.shape("classic")
```
* In order to add a new shape to this library, we will first need to make sure the image file sized correctly. If it is too big then it will take up too much of the screen and if it is too small we will not be able to see it. A good size to work with is **30 pixels.**
* The **image** should be placed in the same folder as the script. 
* Store the name of the image as a **string** variable.

```python
img = "pikachu.gif"
```

* We can then **register** the image as a turtle shape by using the following command:

```python
wn.register_shape(img)
```

* Then you can call the filename as a shape by using the **shape()** function, like we did before. 

```python
t.shape(pikaImg)
```



### KEYBINDING
* First we need to use turtle's **listen()** function to tell Python that we will be listening for an **event**, like a key press.
 
```python
t.listen()
```
* Next we are going us the **onkey()** to tell Python to listen for a specific key to be pressed. When the key is pressed it will call the function we specify. In this case we will create a **turnLeft()** function that will be called when the **“Left”** arrow key is pressed. 
 
```python
t.onkey(turnLeft, "left")
```
* The function **turnLeft()** will rotate the player turtle 30 degrees every time it is called using the left function. We can do the same for the turning the player right. 

```python
def turnLeft():
    player.left(30)
``` 
* You can also assign other functions when different keys are pressed. 

### In-class Exercises/Challenges: 
    * Create a “Player” class that allows a user to navigate the maze created last week.
    * Create a “Player” class that controls a spaceship on the screen. (beginning of alternative version of space invaders)
    * Use Player class to create a 2 player game that controls 2 different spaceships on the screen.
    * Limit the players movement to the viewable screen size/maze boundaries.


### VOCABULARY:
* event
* image
* sprite

### TURTLE KEYWORDS:
* listen
* onkey
* bgpic
* bgcolor
* register_shape
* shape

