import json
import sys

with open('Automa2.json', 'r') as f:
  fsm = json.load(f)

print(fsm)

# s = "01001"
s = sys.argv[1]

current_state = fsm["q0"]

for i in s:
    print("current_input: {}".format(i))
    
    delta = [x for x in fsm["delta"] if x["q"] == current_state and x["i"] == i]
    if(len(delta) == 0):
        print("{} not a valid string".format(s) )
        break
    delta = delta[0]
    current_state = delta["o"]
    
    print("next_delta: {} ".format(delta))
    
if current_state in fsm["F"]:
    print("{} is a valid string".format(s))
else:
    print("{} not recognized from the FSM".format(s))
    
    