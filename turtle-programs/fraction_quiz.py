import quiz_questions
import turtle
import sys
import random

questions = 5 # Number of questions
bottom = 1 # This is the bottom of the range of random numbers
top = 8 # This is the top, inclusive of the range

count = 0 # Score
font = ('Cambria Math', 46, 'normal')
text_font = ('Cambria Math', 30, 'normal')
left_divisionx = -350
right_divisionx = 350
division_height = 0
answer_win = 'Answer'
answer_text = 'What is the result?: '
correct = 'That is correct! '
wrong = 'Oops, your answer is incorrect. '
continue_text = '\nPress "OK" or "Cancel" to proceed, or type "exit" to quit.'

win = turtle.Screen()
arrow = turtle.Turtle()
arrow.hideturtle()
arrow.color('black')
arrow.pensize(5)
arrow.speed(0)

def multiply(x, y):
    # At (x,y) draw 'X'
    arrow.goto(x,y)
    arrow.down()
    arrow.left(45)
    arrow.fd(25)
    arrow.bk(50)
    arrow.up()
    arrow.goto(x,y)
    arrow.down()
    arrow.left(90)
    arrow.fd(25)
    arrow.bk(50)

def divide(x, y):
    # At (x, y) draw division sign
    arrow.goto(x+1,y+20)
    arrow.down()
    arrow.circle(2)
    arrow.up()
    arrow.sety(y-25)
    arrow.down()
    arrow.circle(2)
    arrow.up()
    arrow.goto(x,y)
    arrow.down()
    arrow.fd(25)
    arrow.bk(50)

for n in range(questions):
    operation = random.randint(0,1)
    if n != 0:
        arrow.up()
        arrow.goto(-1000, -100)
        arrow.down()
        arrow.fd(2000)

    arrow.up()
    arrow.goto(0,170)
    arrow.write(f"Question {n+1}", move=False, align='center', font=text_font)
    
    arrow.goto(left_divisionx, division_height)
    arrow.down()
    arrow.fd(200)
    arrow.up()
    arrow.setx(right_divisionx)
    arrow.down()
    arrow.bk(200)
    arrow.up()
    
    if operation == 0:
        multiply(0,division_height)
    else:
        divide(0, division_height)
    arrow.up()

    terms = quiz_questions.two_fractions(bottom, top)
    a = terms[0][0]
    b = terms[0][1]
    c = terms[1][0]
    d = terms[1][1]
    
    arrow.goto(left_divisionx + 100, division_height - 100)
    arrow.write(str(a), move=False, align='center', font=font)
    arrow.sety(division_height - 250)
    arrow.write(str(b), move=False, align='center', font=font)

    arrow.goto(right_divisionx - 100, division_height - 100)
    arrow.write(str(c), move=False, align='center', font=font)
    arrow.sety(division_height - 250)
    arrow.write(str(d), move=False, align='center', font=font)

    if operation == 0:
        numerator = str(a*c)
        denominator = str(b*d)
    else:
        numerator = str(a*d)
        denominator = str(b*c)

    true_answer = f'{numerator}/{denominator}'
    answer = str(win.textinput(answer_win, answer_text))
    arrow.goto(0, -300)

    if answer == true_answer:
        next_question = win.textinput("Correct!", correct + continue_text)
        count += 1
    else:
        next_question = win.textinput("Incorrect", wrong + f'\nThe correct answer is {true_answer}.' + continue_text)
    if next_question == 'exit':
        sys.exit(0)
    
    win.clear()
    win.reset()
    arrow.setheading(0)
    arrow.down()
        
final_score = f"Your final score is: {count}/{questions} - {round(count/questions*100, 1)}%"
arrow.up()
arrow.goto(0,0)
arrow.write(final_score, move=False, align='center', font=text_font)
        


turtle.done()