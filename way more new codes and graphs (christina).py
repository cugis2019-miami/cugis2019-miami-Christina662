
"""
Spyder Editor

This is a temporary script file.
"""

print("hello world")
print ("I am learning to code in python today")

print ("123")
print("hiiiiiii")
"hello world"
5*2
5/2
5-2
5**2
8/9*3
print("5 divided by 2")
5/2
#create function to sum any two numbers

def plus(a,b,c):
    plus= a + b + c
    print(plus)
    
plus(1,3,5)
print(1/2*3*5)
print(0/0)
"whats good"
print hola
print ("box")
       box=box+5 
       
       print(box)
       
#chocolate types 
       d="dark"
       m="milk"
       w="white"
       print (d/mw/w)
       print(d,m,w) 

"d"= dark 
print("hi kaelem, how are you?")

k= "kaelem"
print("how are you")
import math

dir(math)
math.pow(2,4)
math.pow(2,1/4)
math.pow(3,5/8)
def hi(c): 

    hi = c
    math.pow (c)1/3
print ("c=35")
 
def cubicroot(x):
    cubicroot =x**(1/3)
    print(cubicroot)
#Chocolate numeric form
m=(5)
w=(8)
d=(3)
print ( m, "milk chcolates", w, "white chocolates", d, "dark chocolates","is the different chocolates I have.")
#dict data structure
chocolate1= {"milk":5}
chocolate2= {"dark":3}
chocolate3= {"white":8}

chocolatebox={"milk":5,"dark":3,"white":8}

print (chocolatebox)
print ("there is",chocolate1,"bars",chocolate2,"and"chocolate3,"in the box of chocolates")

name1={"steve,male 32 years old"}
name2={"lia,female 28 years old"}
name3={"vin,male 45 years old"}
name4={"katie,female 38 years old"}

age={"28 years old"}
gender={"female"}

print ("Lia's age is",age,"and the gender is",gender)

#pandas
import pandas
dir (pandas)

chocolatebox = {"milk":5,"dark":3,"white":8}

chocolateinfo = pandas.Series(chocolatebox)
print (chocolateinfo)

#list
chocolatedata = [chocolatebox]
print(chocolatedata)

#dataframes
chocolatedf= pandas.DataFrame(chocolatedata,index=[quantity]) #convert to column

studentallinfo= [['steve',32,'male'],['lia',28,'female'],['Vin',45,'male'],['Katie',38,'female']]
print(studentallinfo)

df =pandas.DataFrame(studentallinfo)
print(df)
df2=pandas.DataFrame(studentallinfo,columns=["Name","Age","Gender"])
print (df2)

import pandas
import plotly
studentlist = [['steve',32,'male'],['lia',28,'female'],['Vin',45,'male'],['Katie',38,'female']]
print (studentlist)
studentlistdf = pandas.DataFrame(studentlist, columns= ["name", "age","gender"], index =[1,2,3,4])

print(studentlistdf)



#graph our data
dir (plotly)
from plotly.offline import plot
import plotly.graph_objs as go
import pandas as pd

agename = go.Bar(x=studentlistdf["name"],y=studentlistdf["age"])

plot ([agename])

from plotly.offline import plot
import plotly.graph_objs as go

df = pd.read_excel("GISdata.xlsx",sheet_name = "womenOccupation")
#source:Bureau of Labor Statistics

womenoccupation = go.Bar(x= df["occupation"], y=df["women"],
                         marker = {"color": df["women"],"colorscale":"Blues"}
                         )
plot([womenoccupation])

fig = go.Figure(data=[womenoccupation])

plot(fig)

#layout options
titles = go.Layout(title ="Percentage of Women Employed by occupation", 
                   xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(text="Occupation",
                                                                     )
    ),
    yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(text="Percentage",
                                                       )
    )
    )

    fig=go.Figure(data=[womenoccupation], layout = titles)
    
    plot(fig)
    
                                                       






















































































































































































































































































































































































































































































































































































































































































































































































































































































































































