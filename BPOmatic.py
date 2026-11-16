import requests
from tkinter import *
import time

fenetre = Tk()
fenetre.attributes("-fullscreen", 1)
fenetre.bind('q', lambda event: fenetre.destroy())
fenetre.title("Beltpack O'matic")
c = Canvas(fenetre, bd=0, width = 1920, height = 1080)
fond = PhotoImage(file="image2.png")
c.create_image(959, 540, image=fond)



# Set the name of the XML file.
xml_file = "request.xml"
# header content
headers = {'Content-type' : 'text/xml'}


def boucle ():
# Open XML file.
    with open(xml_file) as xml:
        
    # Give the object requests.post.
        try:
            c.delete ('tag')
            start=time
            RRCSresponse = requests.post('http://RRCSaddressl&port', headers= headers, data= xml, timeout=2)
            filerequest = open("GetallportsRRCScontent.txt", "w") #write the content of the RRCS request on a text file
            filerequest.write(RRCSresponse.text)
            filerequest.close()

            cleanlongnamefile = open("longname.txt", "w")#erase the content of the longname text file
            cleanlongnamefile.close()
            for line in open("GetallportsRRCScontent.txt"):#search in the RRCS response file and write into a file only the long names.
             if "BP " in line:
                 text = line
                 left = 'BP'
                 right = '</string>'
                 Longnametuple = (text[text.index(left)+len(left):text.index(right)],"\n")
                 Longname= ''.join(Longnametuple)
                 filelongname = open("longname.txt", "a")
                 filelongname.write( Longname )
                 filelongname.close()
            a=43 #start dimension in pixel of row 1
            b=0 #BP ID counter
            d=43 #start dimension in pixel of row 2
            e=43 #start dimension in pixel of row 3
            f=43 #start dimension in pixel of row 4
            g=43 #start dimension in pixel of row 5
            h=1133
            i=1133
            j=1133
            k=1133
            l=1133
            input_file_path = 'longname.txt'    # Replace with the actual path to your input text file
            output_file_path = 'sorted_output.txt'     # Replace with the desired path for the sorted output text file

          
            with open(input_file_path, 'r') as file:
                lines = file.readlines()

            data = [line.strip().split(' ', 2) for line in lines]

            sorted_data = sorted(data, key=lambda x: int(x[0]))

            with open(output_file_path, 'w') as output_file:
                output_file.write('\n'.join([' '.join(item) for item in sorted_data]))
            
            
            openlongnamefile = open("sorted_output.txt", "r")
            line = openlongnamefile.readline()
            while b<48:

                if b<=4:#read and display first 5 BP names on row 1
                    c.create_text(a,45, anchor= NW, text= line, tag="tag", font= ('arial', '9', 'bold'), justify='left', width= 80,fill="white", )
                    line = openlongnamefile.readline()
                    print (line)
                    a=a+166
                    b=b+1
                    
                elif b>=5 and b<=9:#read and display first 10 BP names on row 1
                    c.create_text(h,45, anchor= NW, text= line, tag="tag", font= ('arial', '9', 'bold'), justify='left', width= 80,fill="white", )
                    line = openlongnamefile.readline()
                    h=h+166
                    b=b+1
                    
                elif b>=10 and b<=14:#read and display first 10 BP names on row 1
                    c.create_text(d,177, anchor= NW, text= line, tag="tag", font= ('arial', '9', 'bold'), justify='left', width= 80,fill="white", )
                    line = openlongnamefile.readline()
                    d=d+166
                    b=b+1
                    
                elif b>=15 and b<=19:#read and display first 10 BP names on row 1
                    c.create_text(i,177, anchor= NW, text= line, tag="tag", font= ('arial', '9', 'bold'), justify='left', width= 80,fill="white", )
                    line = openlongnamefile.readline()
                    i=i+166
                    b=b+1
                    
                elif b>=20 and b<=24:#read and display first 10 BP names on row 1
                    c.create_text(e,309, anchor= NW, text= line, tag="tag", font= ('arial', '9', 'bold'), justify='left', width= 80,fill="white", )
                    line = openlongnamefile.readline()
                    e=e+166
                    b=b+1
                    
                elif b>=25 and b<=29:#read and display first 10 BP names on row 1
                    c.create_text(j,309, anchor= NW, text= line, tag="tag", font= ('arial', '9', 'bold'), justify='left', width= 80,fill="white", )
                    line = openlongnamefile.readline()
                    j=j+166
                    b=b+1
                
                elif b>=30 and b<=34:#read and display first 10 BP names on row 1
                    c.create_text(f,441, anchor= NW, text= line, tag="tag", font= ('arial', '9', 'bold'), justify='left', width= 80,fill="white", )
                    line = openlongnamefile.readline()
                    f=f+166
                    b=b+1
                    
                elif b>=35 and b<=39:#read and display first 10 BP names on row 1
                    c.create_text(k,441, anchor= NW, text= line, tag="tag", font= ('arial', '9', 'bold'), justify='left', width= 80,fill="white", )
                    line = openlongnamefile.readline()
                    k=k+166
                    b=b+1
                    
                elif b>=40 and b<=44:#read and display first 10 BP names on row 1
                    c.create_text(g,573, anchor= NW, text= line, tag="tag", font= ('arial', '9', 'bold'), justify='left', width= 80,fill="white", )
                    line = openlongnamefile.readline()
                    g=g+166
                    b=b+1
                
                elif b>=45:#read and display first 10 BP names on row 1
                    c.create_text(l,573, anchor= NW, text= line, tag="tag", font= ('arial', '9', 'bold'), justify='left', width= 80,fill="white", )
                    line = openlongnamefile.readline()
                    l=l+166
                    b=b+1
                    
            c.after(60000,boucle)#loop'update' after 1min

            
        except requests.exceptions.ConnectionError:#if no connection to RRCS
            c.create_text(60,47, anchor= NW, tag="tag", text= "BELTPACK O'MATIC IS DOWN :( ", font= ('Didot', '9', 'bold'),fill="white", justify='center', width= 90, )
            c.after(60000, boucle) 

boucle()
c.pack()
fenetre.mainloop()

