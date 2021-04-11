import turtle
import random
import quiz_questions
import sys
import math
import time

questions = 1
count = 0
colors = ['#585ee0', '#ec3d4b', '#56c05e', '#ffa300', '#60cad8', '#b576f0', '#f091e4']
shapes = ['square', 'rectangle', 'triangle']
triangles = ['equilateral', 'isosceles']
units = ['m', 'cm', 'mm', 'km']
font = ("Cambria", 27, 'normal')
answer_win = 'Answer'
answer_text = "What is perimeter of this shape? \nDon't forget the proper units!"
correct = 'That is correct!'
incorrect = 'Oops, your answer is incorrect.'
continue_text = '\nPress "OK" or "Cancel" to proceed, or type "exit" to quit.'
wait = False

green = "#43d15f"
red = '#fa3049'
button_width = 200
button_height = 100

win = turtle.Screen()
arrow = turtle.Turtle()
arrow.hideturtle()
arrow.pensize(5)
arrow.speed(0)

def draw_rect(width, height):
    for i in range(4):
        if i % 2 == 0:
            arrow.fd(width)
        else:
            arrow.fd(height)
        arrow.left(90)

def equal_triangle(side):
    for i in range(3):
        arrow.fd(side)
        arrow.left(120)
    arrow.setheading(0)

def iso_triangle(side1, side2):
    angle = math.degrees(math.acos((side1**2 + side1**2 - side2**2)/(2*side1*side1)))
    two_angles = (180 - angle) / 2

    for i in range(3):
        if i == 0:
            arrow.fd(side2)
            arrow.left(180-two_angles)
        else:
            arrow.fd(side1)
            arrow.left(180-angle)
    arrow.setheading(0)
    return two_angles

def scalene_triangle(side1, side2, side3):
    angle3 = math.degrees(math.acos((side1**2 + side2**2 - side3**2) / (2*side1*side2)))
    angle1 = angle3 * side1 / side3

    arrow.fd(side1)
    arrow.left(180-angle3)
    arrow.fd(side2)
    arrow.left(180-angle1)
    arrow.fd(side3)
    arrow.setheading(0)

def rect_units(width, height, unit, font, is_square):
    arrow.up()
    if is_square:
        x_correction = -35
        y_correction = -140
        y_goto = -180
    else:
        x_correction = -30
        y_correction = -140
        y_goto = -180

    arrow.goto(0, y_goto)
    arrow.write(f"{width} {unit}", align='center', font=font)
    arrow.goto(-width*15//2 + x_correction, height*15//2 + y_correction)
    arrow.write(f"{height} {unit}", align='right', font=font)

def triangle_units(side1, side2, side3, unit, font, left_angle, right_angle):
    arrow.up()
    arrow.goto(0, -190)
    arrow.write(f"{side1} {unit}", align='center', font=font)
    
    arrow.goto(-side1*16//2, -120)
    arrow.left(left_angle)
    arrow.fd(side3*16//2 - 30)
    arrow.left(90)
    arrow.fd(20)
    arrow.setheading(0)
    arrow.write(f"{side3} {unit}", align='right', font=font)
    
    arrow.goto(side1*16//2, -120)
    arrow.left(180-right_angle)
    arrow.fd(side2*16//2 - 30)
    arrow.right(90)
    arrow.fd(20)
    arrow.setheading(0)
    arrow.bk(9)
    arrow.write(f"{side2} {unit}", align='left', font=font)

def draw_buttons():
    arrow.up()
    arrow.goto(200, -350)
    arrow.down()
    arrow.fillcolor(green)
    arrow.begin_fill()
    draw_rect(button_width, button_height)
    arrow.end_fill()
    arrow.up()
    arrow.goto(200+button_width//2, -350+30)
    arrow.write("NEXT", align='center', font=font)

    arrow.goto(-400, -350)
    arrow.down()
    arrow.fillcolor(red)
    arrow.begin_fill()
    draw_rect(button_width, button_height)
    arrow.end_fill()
    arrow.up()
    arrow.goto(-400+button_width//2, -350+30)
    arrow.write("EXIT", align='center', font=font)

def draw_question(question, total):
    arrow.up()
    arrow.goto(0, 200)
    arrow.write(f"Question {question}/{total}", align='center', font=font)

def new_question(x,y):
    if x >= 200 and x <= 200+button_width and y>= -350 and y <= -350+button_height:
        print('pog')
        win.clear()
        win.reset()
        arrow.setheading(0)


for n in range(questions):
    if wait == False:
        arrow.setheading(0)
        shape = random.choice(shapes)
        color = random.choice(colors)
        unit = random.choice(units)
        arrow.up()

        draw_question(n+1, questions)

        if shape == 'square':
            sides = quiz_questions.dimensions_rect(5,20) # Range for random side lengths
            width = random.choice(sides)

            # Draw square
            arrow.goto(-width*15//2, -120)
            arrow.down()
            arrow.fillcolor(color)
            arrow.begin_fill()
            draw_rect(width*15, width*15)
            arrow.end_fill()
            
            # Draw units
            rect_units(width, width, unit, font, True)

            true_answer = str(4*width)

        elif shape == 'rectangle':
            sides = quiz_questions.dimensions_rect(5, 25) # Range for random side lengths
            while abs(sides[0] - sides[1]) <= 6: # So it doesn't look too much like a square
                sides = quiz_questions.dimensions_rect(5, 25)

            width = max(sides)
            height = min(sides)

            # Draw rect
            arrow.goto(-width*15//2, -120)
            arrow.down()
            arrow.fillcolor(color)
            arrow.begin_fill()
            draw_rect(width*15, height*15)
            arrow.end_fill()
            
            # Draw units
            rect_units(width, height, unit, font, False)

            true_answer = str(2*width + 2*height)
            
        elif shape == 'triangle':
            sides = quiz_questions.dimensions_triangle(10, 20)
            triangle = random.choice(triangles)

            if triangle == 'equilateral':
                side1 = random.choice(sides)
                text = f"{side1} {unit}"
            
                # Draw triangle
                arrow.goto(-side1*16//2, -120)
                arrow.down()
                arrow.fillcolor(color)
                arrow.begin_fill()
                equal_triangle(side1*15)
                arrow.end_fill()
                
                # Draw units
                triangle_units(side1, side1, side1, unit, font, 60, 60)

                true_answer = str(side1*3)

            elif triangle == 'isosceles':
                while abs(sides[0] - sides[1]) <= 4:
                    sides = quiz_questions.dimensions_triangle(5, 20)
                side1 = max(sides)
                side3 = min(sides)

                # Draw triangle
                arrow.goto(-side3*16//2, -120)
                arrow.down()
                arrow.fillcolor(color)
                arrow.begin_fill()
                iso_angle = iso_triangle(side1*16, side3*16)
                arrow.end_fill()

                # Draw units
                triangle_units(side3, side1, side1, unit, font, iso_angle, iso_angle)

                true_answer = str(2*side1 + side3)
        

        # Check if answer is right
        answer = win.textinput(answer_win, answer_text)
        if answer in (f"{true_answer} {unit}", f"{true_answer}{unit}"):
            next_question = win.textinput("Correct", correct)
            count += 1
        else:
            next_question = win.textinput("Incorrect", incorrect + f"\nThe correct answer is {true_answer} {unit}. ")
        
        if next_question in ("exit", "Exit", "EXIT"):
            sys.exit(0)
        
        draw_buttons()
        
        win.listen()
        win.onscreenclick(new_question)

arrow.goto(0, 100)
arrow.write(f"Your final score is: {count}/{questions} - {round(count/questions * 100, 1)}%", align='center', font=font)


turtle.done()