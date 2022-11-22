# -*- coding: utf-8 -*-
"""
This is for stepping through the text file containing the 0's and 1's to see where the available spaces are
and send that to the webpage
"""

    
#Open processed text file 
file = open('ForTesting.txt', 'r')
while 1:
        char = file.read(1) #read the value of each characts 
        if not char:
            break
        if char == '1':
        #prints the position of the 1 in the text file.
           print(file.tell())
           #set variable1 equal to the location of the ones
           variable1 = file.tell()
           #send data to html page.
           index = open("testin.html").read().format(veriable1=variable1)
        
#return render_template('MainSite.html', variable1=file.tell())
        
file.close()







