import re


def welcome_msg():
    print("Welcome to Madlib Game")


welcome_msg()

lst=[]
def user_input():
    
    lst_in=["Adjective","Adjective","A First Name","Past Tense Verb"
    ,"A First Name","Adjective","Adjective","Plural Noun"
    ,"Large Animal","Small Animal","A Girls Name","Adjective"
    ,"Plural Noun","Adjective","Plural Noun"
    ,"Number 1-50","First Names", "Number","Plural Noun","Number","Plural Noun"]

    for i in lst_in:
    
        ele= input(f"Plz Enter: {i}  ")
        
        lst.append(ele)

    

#     print(f"""Make Me A Video Game!
# I the {lst[0]} and {lst[1]}{lst[2]} have {lst[3]}{lst[4]}'s {lst[5]} sister and plan to steal her {lst[6]} {lst[7]}!
# What are a {lst[8]} and backpacking {lst[9]} to do? Before you can help{lst[10]}, you'll have to collect the {lst[11]}{lst[12]} and {lst[13]} {lst[14]} that
# open up the {lst[15]} worlds connected to A {lst[16]} Lair. There are {lst[17]} {lst[18]} and {lst[19]} {lst[20]} in the game, along with hundreds of other goodies for you to find.""")
        

user_input()


def read_template():
    try:

        with open('madlib_cli/assets/spam.txt') as file:
            read = (file.read().strip())
        # print(read)
        return read
    except FileNotFoundError:
        return 'FileNotFoundError'    

read =read_template()


# print(type(read))

def parse_template(read):
    
    y = re.sub("{[^}]+}", "{}", read)
    x = re.findall("{[^}]+}", read)
    x=lst
    
    return x,y

rege=parse_template(read)


string =rege[1]
arraay= rege[0]

# print(string)
print(type(arraay))





      
parse_template(read)


def merge():

    megedText=string.format(*arraay)
    print(megedText) 
        

    
    

merge()

# if __name__== "__main__":
#     print(read_template())

# def write_madlib(path, madlib):
#     with open(path,'w') as filled:
#         filled.write(madlib)


# def merge():
#     print(f"""Make Me A Video Game!
# # I the {rege[0]} and {rege[0]}{rege[0]} have {rege[3]}{rege[4]}'s {rege[5]} sister and plan to steal her {rege[6]} {rege[7]}!
# # What are a {rege[8]} and backpacking {rege[9]} to do? Before you can help{rege[10]}, you'll have to collect the {rege[11]}{rege[12]} and {rege[13]} {rege[14]} that
# # open up the {rege[15]} worlds connected to A {rege[16]} Lair. There are {rege[17]} {rege[18]} and {rege[19]} {rege[20]} in the game, along with hundreds of other goodies for you to find."""










