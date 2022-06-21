import turtle
import pandas

screen = turtle.Screen()
screen.title("Amerika Bölgeleri")
foto = "blank_states_img.gif"
screen.addshape(foto)
turtle.shape(foto)

veri = pandas.read_csv("50_states.csv")

all_bolge = veri.state.to_list()
tahminler = []
while len(tahminler) < 50:
    answer_state = screen.textinput(title=f"{len(tahminler)}/50 Doğrun Var.",
                                    prompt="Burası Neresi?:").title()
    if answer_state == "Exit":
        bilinmeyenler = [bolge for bolge in all_bolge if bolge not in tahminler]
        new_veri = pandas.DataFrame(bilinmeyenler)
        new_veri.to_csv("bilemediğin bölgeler")
        break
    elif answer_state in all_bolge:
        tahminler.append(answer_state)
        s = turtle.Turtle()
        s.hideturtle()
        s.penup()
        bolge_verisi = veri[veri.state == answer_state]
        s.goto(int(bolge_verisi.x), int(bolge_verisi.y))
        s.write(answer_state)






