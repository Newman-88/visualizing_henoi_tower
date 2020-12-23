import matplotlib.pyplot as plt
import numpy as np
import time

## defining the main function to solve tower of henoi problem
def henoi (disk,source,destiny,aux,instruct):
    '''Reccursive function calling itself twice within it. The instructions will be saved as a list of dictionary in the instruct global variable'''
    if disk == 1:
        instruct.append({'disk':disk,'move_from':source,'move_to':destiny})
    else: 
        henoi(disk-1,source, aux,destiny,instruct)
        instruct.append({'disk':disk,'move_from':source,'move_to':destiny})
        henoi(disk-1,aux, destiny,source,instruct)

        
## Asking the user for number of discs 
no_discs = int(input("Please enter number of discs: "))


##defining global variable instruct and calling the main function
instruct = []
henoi(no_discs,"source","destiny","aux",instruct)

#asking user for time gap between plotting each move
t = float(input("Enter the sleep time between moves in seconds: "))

### function for plotting each instruction step
def plot_steps(fg, no_discs,source_list,aux_list,destiny_list,step,mov_nkr):
    '''This function plots each step after getting the input of current state of each pillar'''
    
    fig = fg
    plt.clf()
    fig.add_subplot(111)
    plt.axis((0,4,0.5,no_discs+1))
    plt.title("Step " + str(step+1)+": "+mov_nkr)  
    
    y_list = np.arange(int(no_discs))+1
    if not len(source_list)==0:
        for i in range(len(source_list)):
            plt.scatter(1,i+1,c="b",alpha=0.3,s=(no_discs-source_list[i])*200)
            plt.scatter(1,i+1,c="b",marker = '$iiiiiiiiiiiiiiiiiiiiiiiiiii$',s=(no_discs-source_list[i])*200)
            plt.annotate(str(no_discs-source_list[i]),(1,i+1),size=12,weight = 'bold')
    if not len(aux_list)==0:
        for i in range(len(aux_list)):
            plt.scatter(2,i+1,c="b",alpha=0.3,s=(no_discs-aux_list[i])*200)
            plt.scatter(2,i+1,c="b",marker = '$iiiiiiiiiiiiiiiiiiiiiiiiiii$',s=(no_discs-aux_list[i])*200)
            plt.annotate(str(no_discs-aux_list[i]),(2,i+1),size=12,weight = 'bold')
    if not len(destiny_list)==0:
        for i in range(len(destiny_list)):
            plt.scatter(3,i+1,c="b",alpha=0.3,s=(no_discs-destiny_list[i])*200)
            plt.scatter(3,i+1,c="b",marker = '$iiiiiiiiiiiiiiiiiiiiiiiiii$',s=(no_discs-destiny_list[i])*200)
            plt.annotate(str(no_discs-destiny_list[i]),(3,i+1),size=12,weight = 'bold')
    plt.axvline(x=1,c="brown")
    plt.axvline(x=2,c="brown")
    plt.axvline(x=3,c="brown")
    plt.axhline(y=0.5, c="black")
    plt.xticks([1,2,3],["Source","Aux","Destiny"])
    plt.yticks(y_list,y_list[::-1])
    fig.show()


## Initializing the three pillars with all the discs in source pillar
source_list = [i for i in range(int(no_discs))]
aux_list=[]
destiny_list=[]


step = 0
mov_nkr = "Starting Position"


###Plotting initial position 
fig = plt.figure(figsize=(8,4))
plot_steps(fig, no_discs,source_list,aux_list,destiny_list,-1,mov_nkr)
fig.canvas.draw()

plot_steps(fig, no_discs,source_list,aux_list,destiny_list,-1,mov_nkr)
fig.canvas.draw()
time.sleep(2*t)


### altering the discs in each pillar based on the instructions from henoi function instruct list
for i in range(len(instruct)):
    
    step = step +1
    mov_nkr = "Moved disc no "+str(instruct[i]["disk"])+" from "+instruct[i]["move_from"]+" to "+instruct[i]["move_to"]
    
    nkr = no_discs - instruct[i]["disk"] 
    if instruct[i]["move_from"]=="source":
        source_list.remove(nkr)
        #print("source:",source_list)
    elif instruct[i]["move_from"]=="aux":
        aux_list.remove(nkr)
        #print("aux:",aux_list)
    else:
        destiny_list.remove(nkr)
        #print("destiny:",destiny_list)
        
    if instruct[i]["move_to"]=="source":
        source_list.append(nkr)
        #print("source:",source_list)
    elif instruct[i]["move_to"]=="aux":
        aux_list.append(nkr)
        #print("aux:",aux_list)
    else:
        destiny_list.append(nkr)
        #print("destiny:",destiny_list)

    ### Plotting each step in a canvas figure 
    
    plot_steps(fig, no_discs,source_list,aux_list,destiny_list,i,mov_nkr)

    fig.canvas.draw()

    time.sleep(t)
