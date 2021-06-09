import re


def welcome_msg():
    print("Welcome to Madlib Game")




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

    



def read_template(path):
    try:
        # path='assets/spam.txt'
        with open(path) as file:
            read = (file.read().strip())
        # print(read)
        return read
    except FileNotFoundError:
        return 'FileNotFoundError'  
    except Exception as e:
        return "Something's Going Wrong : "+ e    

    return hhh    
          

read =read_template('assets/spam.txt')


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
# print(type(arraay))





      



def merge(string,arraay):

    megedText=string.format(*arraay)
    return megedText 
        

    




if __name__ == '__main__':  
    welcome_msg()
    user_input()
    parse_template(read)
    print(merge(string,arraay))









