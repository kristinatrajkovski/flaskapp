from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def start():
    title = "The Embarassment"
    
    text = """You are going to attend a very important job interview. Although you had a rough night, ,you have it all ready: the suit, the attitude, the looks... everything... Try not to ruin it!!!"""
    image2 = "coffee"
    choices = [
        ('get_coffee',"Go get coffee"),
        ('interview',"Go to the interview with huge purple bags under your eyes")
    ]
    return render_template('adventure.html', title=title, text=text, choices=choices)



@app.route("/coffee")
def get_coffee():
    title = "You buy coffee from Starbucks..."
    
    text = """You ask for a cup of Pumpkin Spice Latte. The barista has been working a 10 hour shift and you are the 14905873th person to order that today. She gets angry, calls you a typical 'Chad' and throws a cup of coffee in your face."""

    choices = [
        ('home_change',"Go home and change"),
        ('interview',"Still go to the interview")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)

@app.route("/interview")
def interview():
    end = "interview"
    title = "You made it to your interview!"
    
    text = """You arrived to your future office looking like you went through a natural catastrophy. Although, your current boss saw it as 'True depiction of dedication' and gave you the job with fair salary. Congrats!"""

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices, end = end)



@app.route("/home")
def home_change():
    end = "dog"
    title = "You arrive home..."
    
    text = """Just as you were unlocking your front door, a stray dog with rabies grabs you by your behind and you end up going to the hospital and missing your meeting completely"""
    
    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices, end = end)
