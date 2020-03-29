from collections import deque




class Node:
    def __init__(self, state, action=-1, cost=0, parent=None):
        self.State = state
        self.Action = action
        self.Cost = cost
        self.Parent = parent

    def __repr__(self):
        return f"<Node {self.State}>"

def goal_test(node, goal, states):
    for index in range(len(states)):
        if goal == states[index]:
            if node.State == index:
                return True
            else:
                return False

MNT = str(input("enter header"))
MNT = MNT.split()
M = int(MNT[0])
N = int(MNT[1])
T = int(MNT[2])
states = []
Actions = []
transition_model = []
print("Enter States")
for i in range(M):
    states.append(input())
print("Actions")
for i in range(N):
    Actions.append(input())

print("Transition table")
for i in range(M):
    row = []
    row = input().split()
    row = [int(z) for z in row]
    transition_model.append(row)
def search_problem(problem):
     for index in range(len(states)):
        if problem[0] == states[index]:
            FirstNode = Node(index)
            frontier = deque([FirstNode])
            explored = set()
            exploredNode = set()
    sol = []
    while True:
        if frontier is not None:
            node = frontier.popleft()
            explored.add(node.State)
            if goal_test(node, problem[1], states):
                print("ahtesham")
                return sol
            else:
                state_of_current_node = node.State
                children = transition_model[state_of_current_node]
                for child in range(len(children)):
                    new_child_node = Node(int(children[child]), child, node.Cost + 1, node)
                    if new_child_node.State not in explored and new_child_node not in frontier:
                        sol.append(Actions[child])
                        if goal_test(new_child_node, problem[1], states):
                            return sol
                        frontier.append(new_child_node)
                        break

        else:
            return None


def main():
    print("Enter Test case")
    for x in range(T):
        start_goal = input().split("\t")
        solution = search_problem(start_goal)
        for i in range(len(solution)):
            print(solution[i], end="")
            if i is not len(solution) - 1:
                print("->", end="")
        print("")
main()