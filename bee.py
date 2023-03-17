from lark import Lark

my_grammar = """
start: statement+          
entrance: "[Enter" name "]"
return: "[Exit" name "]"
name: WORD
?statement:  math | entrance | return | buzz | variable | talk
?math: add | sub | multi | divide | equal | saying
number: NUMBER
 
add: [","] ["and"] ["but"] name "also got" number ["more"]
    | [","] ["and"] ["but"] name "added" number ["more"]
 
sub:    name "-" number ["more"]
        | [","]["but"] name subverb number ["more"]
 
multi:   [","]["and"]["but"] name number "times" ["more"]
        | [","]["and"]["but"] name multiverb number "times" ["more"]
 
divide:   [","]["and"]["but"] name "/" number ["times"] 
            | [","]["and"]["but"] name divideverb number ["times"] 
 
equal:    name assign equalverb number WORD
        
saying:   name assign speechverb text ["!"]
text: WORD
 
?buzz: assign 
    | print
?assign:    "buzz in" ["and"]
        | "buzzed in" ["and"]
print:   ["Then"] name ["would"] "buzz out" 
        |  name ["then"] "buzzed out"
 
?variable: alloc | death
alloc:  ["Let"] name "bee" number
         | ["Let"] name "bee" WORD
         | name ["should"] "bee about" number
death: name deathverb
?talk: equal
 
?speechverb:    "saying" | "says" | "said" | "talked about"
?equalverb: "=" | "collected" | "had" | "having" | "collecting"
?subverb:    "minus" 
        |  "lost" ["it"]
        |  "removed"
        |  "subtracted" ["it"]
?multiverb: "multiplied" ["it"]
            | "repeated" ["it"]            
?divideverb: "segmented" ["it"]
            | "striped" ["it"]
            | "divided" ["it"]
?deathverb:    "dead" | "died" | "death" | "has died"
 
%import common.WORD   
%import common.NUMBER
%import common.WS
%ignore WS           
%ignore " "

"""

def run_tree(t, env):
    if t.data == 'start':    #DONE
        for child in t.children:
            run_tree(child, env)  
        #print(t.children[0])
    elif t.data == 'add':
        #DONE
        
        #print(env[t.children[0].children[0]], "<-lhs")
        #print(t.children[1].children[0], "<-rhs")
        env[t.children[0].children[0]] = (env[t.children[0].children[0]] + int(t.children[1].children[0]))

        #print("------add------")
    elif t.data == 'entrance':
        #DONE
        
        name=env[t.children[0].children[0]]=int(0)
        #print(t.children[0].children[0])
        #print(name, "<-variable")
        #print("-------entrance--------")
    elif t.data == 'death':
        exit()
    elif t.data == "saying":
        #DONE

        #print(env[t.children[0].children[0]], "lhs")
        
        

        env[t.children[0].children[0]] = str(t.children[3].children[0])
        #print(env[t.children[0].children[0]])
        #print("------saying-----")

    elif t.data == 'alloc':
        #DONE

        lhs = env[t.children[0].children[0]]
        rhs = t.children[1].children[0]
        env[t.children[0].children[0]] = env[t.children[0].children[0]]= int(t.children[1].children[0])     
        
        #print(env[t.children[0].children[0]], "<-answer")
        #print(t.children[1].children[0], "<-rhs")
        #print("--------alloc------")        
    elif t.data == 'equal':
        #DONE

        #print(t.children[0].children[0], "<-lhs")
        #print(t.children[3].children[0], "<-rhs")
        
        env[t.children[0].children[0]] = env[t.children[0].children[0]]= int(t.children[3].children[0])
        #print(env[t.children[0].children[0]], "<-equal")
        #print("-----equal-------")
    elif t.data == 'return':
        #DONE

        (env[t.children[0].children[0]])= int(0)
        #print(env[t.children[0].children[0]])
        #print("return")
    elif t.data == 'sub':
        #DONE


        #print(t.children[0].children[0], "<-lhs")
        #print(t.children[2].children[0], "<-rhs")
        
        env[t.children[0].children[0]] = (env[t.children[0].children[0]] - int(t.children[2].children[0]))
        #print(env[t.children[0].children[0]], "<-answer")
        #print("--------sub--------")
    elif t.data == 'multi':
        #DONE
        
        #print(t.children[0].children[0], "<-lhs")
        #print(t.children[2].children[0], "<-rhs")
        
        env[t.children[0].children[0]] = (env[t.children[0].children[0]] * int(t.children[2].children[0]))
        #print(env[t.children[0].children[0]], "<-answer")
        #print("-------multi--------")
    elif t.data == 'divide':
        #DONE

        #print(env[t.children[0].children[0]])
        #print(t.children[2].children[0])
        env[t.children[0].children[0]]= (env[t.children[0].children[0]] / int(t.children[2].children[0]))
        #print(env[t.children[0].children[0]])

        #print("-----divide-----")
    elif t.data == 'print':
        #DONE

        print("The program output is: ",env[t.children[0].children[0]])
        #print("----print------")

parser = Lark(my_grammar)
program = """
[Enter Barry]
Barry buzzed in and collected 3 books, but Barry also got 4 more
Barry buzzed out
[Exit Barry]
"""
env = {}
parse_tree = parser.parse(program)
#print(run_tree(parse_tree,env))
#print(parse_tree.pretty())
run_tree(parse_tree, env)











































