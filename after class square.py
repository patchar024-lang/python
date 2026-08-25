import turtle

def draw_square(side_length):
    """
    Draws a square using the turtle library.
    Each side will be the given side_length.
    """
    # Loop 4 times because a square has 4 sides and 4 corners
    for _ in range(4):
        turtle.forward(side_length)  # Move forward by the specified length
        turtle.right(90)             # Turn right by 90 degrees

if __name__ == "__main__":
    # Set up the screen and turtle appearance
    turtle.title("Turtle Drawing a Square")
    turtle.shape("turtle")
    turtle.speed(2)  # 1 is slow, 10 is fast, 0 is the fastest
    
    # Call the function to draw a square with a side length of 100 pixels
    draw_square(100)
    
    # Keeps the window open until you click on it
    turtle.exitonclick()