from flask import Flask, render_template, url_for   # import flask libraries
from jinja2 import Environment, FileSystemLoader    # import jinja libraries


app = Flask(__name__, template_folder='templates', static_folder='static')  # map to html, have to have a folder named templates conatining the html files 
                                                                            # also have to have a folder names static containing the .css file


file_loader = FileSystemLoader('templates')     # loads the html when file_loader is called
env = Environment(loader=file_loader)           # sets up the connection to the template

template = env.get_template('MainSite.html')      


def update():                                   # update function to read the data from the text file
    file = open('outputwork', 'r')              # open the text file

    Lines = file.readlines()                    # set lines equal to the entire text document

    availSpots = {                              # create an empty dictionary
    "general": [],
    "handicap": [],
    "electric": []

    }    

    for line in Lines:                          # extract the data and sort based on the last value of each line
            items = line.split("..........")    # gets rid of the extra dots
            processData = [spots.replace(".", "").strip() for spots in items]   
            key = processData[-1]               # sets the key equal to the last value of the line  
            availSpots[key].append(f"{processData[0]}, {processData[1]}")       # save the other two values as the key values
    
    return availSpots
    

@app.route("/general")                          # on the general page
def general():
    availSpots = update()                       # call update to ensure values are up to date 
    return template.render(variable1=availSpots['general'], title="General")    # send the data to the webpage, also set the title 
    
 
@app.route("/handicap")                         # on the handicap page 
def handicap():
    availSpots = update()                       # update values
    return template.render(variable1=availSpots['handicap'], title="Handicap")  # send the data to the webpage, also set the title 

@app.route("/electric")                         # on the electric page
def electric():
    availSpots = update()                        # update values
    return template.render(variable1=availSpots['electric'], title="Electric")  # send the data to the webpage, also set the title 

if __name__ == "__main__":

    app.run()                       # run the app 
