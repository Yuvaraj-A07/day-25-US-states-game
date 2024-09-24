import turtle
import pandas as pd
screen = turtle.Screen()

screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pd.read_csv("50_states.csv")
state_list =[]
all_states = data.state.to_list()
while len(state_list) <= 50:
    answer_state = screen.textinput(title=f"{len(state_list)}/{len(all_states)} the states correct",
                                    prompt="What is the next state?").title()

    if answer_state == "Exit":
        break

    if answer_state in all_states and answer_state not in state_list:
        location = data[data["state"] == answer_state]
        all_states.remove(answer_state)
        state_list.append(answer_state)
        t = turtle.Turtle()
        # cor = all_states.index(answer_state)
        # x = location["x"][cor]
        # y = location["y"][cor]
        t.penup()
        t.hideturtle()
        t.goto(int(location.x), int(location.y))
        t.write(answer_state)
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
rem_states = {"the states you missed ":all_states}
df = pd.DataFrame(rem_states)
df.to_csv("stats_to_learn.csv")
screen.exitonclick()
