import re


def welcome_msg():
    print("Welcome to Madlib Game")


# welcome_msg()

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

    
# user_input()


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





      
# parse_template(read)


def merge(string,arraay):

    megedText=string.format(*arraay)
    print(megedText) 
        

    

# merge(string,arraay)








