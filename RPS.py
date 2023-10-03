import random as ran
def play(x,y):
    u_p=x
    c_p=y
    user=input("'r'for rock,'p'for paper,'s' for scissor ")
    comp=ran.choice(['r','p','s'])
    print(user)
    print(comp)
    if user==comp:
        print("tie")
    if is_win(user,comp):
        u_p+=1
        print(f"You won +{u_p}")
    c_p+=1
    print(f"You Lost C_P +{c_p}")
#r>s,p>r,s>p

def is_win(u,c):
    if (u=='r' and c=='s') or (u=='s' and c=='p') or (u=='p' and c=='r'):
        return True
    elif (u=='r' and c=='p') or (u=='s' and c=='r') or (u=='p' and c=='s'):
        return False
play(0,0)
