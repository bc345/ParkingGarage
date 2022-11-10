from flask import Flask, render_template, url_for
from jinja2 import Environment, FileSystemLoader


app = Flask(__name__, template_folder='templates', static_folder='static')


file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

template = env.get_template('MainSite.html')


def update():
    file = open('outputwork', 'r')

    Lines = file.readlines()   

    availSpots = {
    "general": [],
    "handicap": [],
    "electric": []

    }    

    for line in Lines:
            items = line.split("..........")
            processData = [spots.replace(".", "").strip() for spots in items]
            key = processData[-1]
            availSpots[key].append(f"{processData[0]}, {processData[1]}")
    
    return availSpots
    

@app.route("/general")
def general():
    availSpots = update()
    return template.render(variable1=availSpots['general'], title="General")
    
 
@app.route("/handicap")
def handicap():
    availSpots = update()
    return template.render(variable1=availSpots['handicap'], title="Handicap")

@app.route("/electric")
def electric():
    availSpots = update()
    return template.render(variable1=availSpots['electric'], title="Electric")

if __name__ == "__main__":

    app.run()
