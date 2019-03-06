import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# define your draw functions

def green_hill():
    arcade.draw_ellipse_filled(10, 100, 250, 200, arcade.color.GREEN)
    arcade.draw_ellipse_filled(400, 10, 250, 200, arcade.color.GREEN)
    arcade.draw_ellipse_filled(800, 70, 250, 200, arcade.color.GREEN)

def clouds(x, y):
    arcade.draw_circle_filled(200 + x, 500 + y, 20, arcade.color.WHITE)
    arcade.draw_circle_filled(220 + x, 500 + y, 20, arcade.color.WHITE)
    arcade.draw_circle_filled(200+ x, 520 + y, 20, arcade.color.WHITE)

def draw_pine_tree(x, y):
    arcade.draw_triangle_filled(x + 40, y, x, y - 100,x + 80, y - 100,arcade.color.DARK_GREEN)
    arcade.draw_triangle_filled(x + 40, y+20, x, y - 50, x + 80, y - 50, arcade.color.DARK_GREEN)
    arcade.draw_lrtb_rectangle_filled(x + 30, x + 50, y - 100,y - 140,arcade.color.DARK_BROWN)

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.BABY_BLUE)
    arcade.start_render()

    # call your draw functions
    green_hill()
    clouds(20,30)
    clouds(-100,-110)
    clouds(50,-80)
    draw_pine_tree(50, 250)
    draw_pine_tree(350, 320)
    draw_pine_tree(520,260)

    # Finish and run
    arcade.finish_render()
    arcade.run()




# Call the main function to get the program started.
main()