# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def dfs_stack(problem):
    from util import Stack
    st = Stack()
    startPos = problem.getStartState()
    st.push([startPos, 'start', 0])

    visited = dict()
    path = []
    while not st.isEmpty():
        curPos, direction, status = st.pop()
        if status == 1:
            if curPos != startPos:
                path.pop()
        
        elif status == 0 and curPos not in visited:
            if direction != 'start':
                path.append(direction)
            
            if problem.isGoalState(curPos):
                break

            visited[curPos] = 1
            st.push([curPos, direction, 1])
            neighbors = problem.getSuccessors(curPos)

            for neighbor in neighbors:
                nextPos, nextDir, _ = neighbor
                st.push([nextPos, nextDir, 0])
    return path

def dfs_stack2(problem):
    from util import Stack
    st = Stack()
    st.push([problem.getStartState(), []])
    visited = dict()

    while not st.isEmpty():
        curPos, path = st.pop()
        if problem.isGoalState(curPos):
            return path

        if curPos not in visited:
            visited[curPos] = 1
            for nextPos, direction, _ in problem.getSuccessors(curPos):
                st.push([nextPos, list(path + [direction])])
    return []

def dfs_recursion(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    """ Initialization of the static variables """ 
    if not hasattr(dfs_recursion, 'curPosition'):
        dfs_recursion.curPosition = problem.getStartState()
        dfs_recursion.curPath = []
        dfs_recursion.foundPath = []
        dfs_recursion.visited = dict()

    """ Mark the visited position """
    curPos = dfs_recursion.curPosition
    dfs_recursion.visited[curPos] = 1
    
    """ Check if it reaches the destination """
    if problem.isGoalState(curPos):
        dfs_recursion.foundPath = dfs_recursion.curPath[::1]
        return

    """ DFS Body """ 
    neighbors = problem.getSuccessors(curPos)
    for neighbor in neighbors:
        # Pruning (if found a path, just break)
        if len(dfs_recursion.foundPath) != 0:
            break
            
        nextPos, direction, valid = neighbor
        if valid and nextPos not in dfs_recursion.visited: # valid
            dfs_recursion.curPath.append(direction)
            dfs_recursion.curPosition = nextPos
            dfs_recursion(problem)
            dfs_recursion.curPath.pop()
            dfs_recursion.curPosition = curPos

    if curPos == problem.getStartState():
        result = dfs_recursion.foundPath[::1]
        del dfs_recursion.curPosition
        del dfs_recursion.curPath
        del dfs_recursion.foundPath
        del dfs_recursion.visited
        return result
    else:
        return

def bfs_sol1(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from util import Queue
    queue = Queue()
    queue.push(problem.getStartState())

    visited = {problem.getStartState(): 1}
    parent = {problem.getStartState(): problem.getStartState()}
    directions = dict()

    while not queue.isEmpty():
        curPos = queue.pop()
        if problem.isGoalState(curPos):
            path = []
            while curPos != problem.getStartState(): 
                path.append(directions[curPos])
                curPos = parent[curPos]
            return path[::-1]

        for nextPos, nextDir, _ in problem.getSuccessors(curPos):
            if nextPos not in visited:
                parent[nextPos] = curPos
                directions[nextPos] = nextDir
                visited[nextPos] = 1
                queue.push(nextPos)
    return []

def bfs_sol2(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from util import Queue
    queue = Queue()
    queue.push([problem.getStartState(), []])
    visited = {problem.getStartState(): 1}
    
    while not queue.isEmpty():
        curPos, path = queue.pop()
        if problem.isGoalState(curPos):
            return path

        for nextPos, direction, _ in problem.getSuccessors(curPos):
            if nextPos not in visited:
                visited[nextPos] = 1
                queue.push([nextPos, list(path + [direction])])
    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    # Items in priority queue
    # item: [position, distance, parent, action], priority: distance
    from util import PriorityQueue
    pq = PriorityQueue()
    start_pos = problem.getStartState()
    pq.push([start_pos, 0, start_pos, "Start"], 0)

    shortest, parents, actions = dict(), dict(), dict()
    visited = dict()

    while not pq.isEmpty():
        pos, d, parent, action = pq.pop()
        if pos not in visited:
            visited[pos] = 1
            parents[pos] = parent
            actions[pos] = action
            shortest[pos] = d

            if problem.isGoalState(pos):
                path = []
                while parents[pos] != pos:
                    path.append(actions[pos])
                    pos = parents[pos]
                return path[::-1]
            else:
                neighbors = problem.getSuccessors(pos)
                for nextPos, direction, cost in neighbors:
                    if nextPos not in visited:
                        updated_d = shortest[pos] + cost
                        pq.push([nextPos, updated_d, pos, direction], updated_d)
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    from searchAgents import manhattanHeuristic
    from util import PriorityQueue
    
    start_pos = problem.getStartState()

    # Items in Priority Queue
    # item: [pos, g_score, f_score, parent, direction], priority: f_score
    pq = PriorityQueue()
    g_score = 0
    f_score = heuristic(start_pos, problem) + g_score
    pq.push([start_pos, g_score, f_score, start_pos, "Start"], f_score)

    visited, f_scores = dict(), dict()
    parents, directions = dict(), dict()

    while not pq.isEmpty():
        pos, g_score, f_score, parent, action = pq.pop()

        if pos not in visited:
            visited[pos] = 1
            parents[pos] = parent
            directions[pos] = action
            f_scores[pos] = f_score 
            
            if problem.isGoalState(pos):
                path = []
                while pos != parents[pos]:
                    path.append(directions[pos])
                    pos = parents[pos]
                return path[::-1]
            else:
                neighbors = problem.getSuccessors(pos)
                for nextPos, direction, cost in neighbors:
                    if nextPos not in visited:
                        h_score = heuristic(nextPos, problem)
                        new_g_score = g_score + cost
                        new_f_score = new_g_score + h_score
                        pq.push([nextPos, new_g_score, new_f_score, pos, direction], new_f_score)
    return []

# Abbreviations
depthFirstSearch = dfs_stack2
breadthFirstSearch = bfs_sol1

dfs = depthFirstSearch
bfs = breadthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch


