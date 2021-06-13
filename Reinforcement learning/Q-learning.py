import numpy as np
MATRIX_SIZE=6
M=np.matrix([
    [-1,-1,-1,-1,0,-1],
    [-1,-1,-1,0,-1,100],
    [-1,-1,-1,0,-1,-1],
    [-1,0,0,-1,0,-1],
    [0,-1,-1,0,-1,100],
    [-1,0,-1,-1,0,100]
    ])
gamma=0.80

Q=np.matrix(np.zeros([MATRIX_SIZE,MATRIX_SIZE]))

#learning parameter
initial_state=4 #set initial state as current state

#Determines the available actions for a given state
def available_actions(state):
    current_state_row=M[state,]
    available_action=np.where(current_state_row >=0)[1]
    return available_action

available_action=available_actions(initial_state)

#Chooses one of the available actions at random
def sample_next_action(available_actions_range):
    next_action=int(np.random.choice(available_action,1))
    return next_action

action=sample_next_action(available_action)

def update(current_state,action,gamma):
    print(action)
    max_index=np.where(Q[action,]==np.max(Q[action,]))[1]
    print(max_index)
    if max_index.shape[0]>1:
        max_index=int(np.random.choice(max_index,size=1))
        
    else:
        max_index=int(max_index)
    max_value=Q[action,max_index]
    Q[current_state,action]=M[current_state,action] + gamma +max_value
    if (np.max(Q) > 0):
        return(np.sum(Q / np.max(Q)*100))
    else:
        return(0)
    #Updates the Q Matrix according to the path chosen
    
update(initial_state,action,gamma)

scores=[]
for i in range(1000):
    current_state=np.random.randint(0,int(Q.shape[0]))
    available_action=available_actions(current_state)
    action=sample_next_action(available_action)
    score=update(current_state, action, gamma)
    scores.append(score)
    
print("Trained Q matrix")
print(Q / np.max(Q)*100)

#Testing
current_state=3
steps=[current_state]

while current_state !=5:
    
    next_step_index=np.where(Q[current_state, ] == np.max(Q[current_state, ]))
    if next_step_index.shape[0] >1:
        next_step_index=int(np.random.choice(next_step_index,size=1))
        
    else:
        next_step_index=int(next_step_index)
    steps.append(next_step_index)
    current_state=next_step_index
    
print("Most efficient path:")
print(steps)



