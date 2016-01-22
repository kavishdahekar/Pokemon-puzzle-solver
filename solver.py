# Node data structure for storing player position and state of current game
class Node(object):
    def __init__(self,ppos,gamestate):
        self.ppos=ppos
        self.gamestate=gamestate

class Position(object):
    def __init__(self,v,h):
        self.v=v #vertical index
        self.h=h #horizontal index

def showNode(node):
	print "("+str(node.ppos.v)+","+str(node.ppos.h)+")"
	print node.gamestate


gameAreaSizeV = 6
gameAreaSizeH = 5
# defining start state and goal state
startpos = Position(5,2)
goalpos = Position(0,2)
startAreaState = [
				[1,0,0,0,1],
				[1,1,0,1,1],
				[0,1,1,1,0],
				[1,0,0,0,1],
				[0,1,1,1,0],
				[0,0,0,0,0],
			]
startGameState = Node(startpos,startAreaState)
# print startState[startpos.v][startpos.h]

mainStack = []
mainStack.append(startGameState)

while 1:
	# if stack empty, exit
	if len(mainStack) == 0:
		print "No solution found..."
		sys.exit()

	#Get current node as the top node from stack
	currentNode = mainStack[0]
	#Remove that node from stack
	mainStack.pop(0)

	#check if we have reached goal state
	if currentNode.ppos == goalpos:
		print "Found solution.."
		sys.exit()

	#generate possible child nodes
	# 1. childMoveUp
	# check if that space is empty and hence can be moved into, and also check if we are still inside game area
	if currentNode.ppos.v-1 >= 0 and currentNode.gamestate[currentNode.ppos.v-1][currentNode.ppos.h] == 0:
		print "childMoveUp"
		#MoveUp is possible
		#gameAreastate does not change, only player pos changes
		#add it to mainStack
		tempGameAreaState = currentNode.gamestate[:]
		mainStack.append(Node(Position(currentNode.ppos.v-1,currentNode.ppos.h),tempGameAreaState))

	# 2. childMoveDown
	# check if that space is empty and hence can be moved into, and also check if we are still inside game area
	if currentNode.ppos.v+1 < gameAreaSizeV and currentNode.gamestate[currentNode.ppos.v+1][currentNode.ppos.h] == 0:
		print "childMoveDown"
		#MoveUp is possible
		#gameAreastate does not change, only player pos changes
		#add it to mainStack
		tempGameAreaState = currentNode.gamestate[:]
		mainStack.append(Node(Position(currentNode.ppos.v+1,currentNode.ppos.h),tempGameAreaState))

	# 3. childMoveLeft
	# check if that space is empty and hence can be moved into, and also check if we are still inside game area
	if currentNode.ppos.h-1 >= 0 and currentNode.gamestate[currentNode.ppos.v][currentNode.ppos.h-1] == 0:
		print "childMoveLeft"
		#MoveUp is possible
		#gameAreastate does not change, only player pos changes
		#add it to mainStack
		tempGameAreaState = currentNode.gamestate[:]
		mainStack.append(Node(Position(currentNode.ppos.v,currentNode.ppos.h-1),tempGameAreaState))

	# 4. childMoveLeft
	# check if that space is empty and hence can be moved into, and also check if we are still inside game area
	if currentNode.ppos.h+1 < gameAreaSizeH and currentNode.gamestate[currentNode.ppos.v][currentNode.ppos.h+1] == 0:
		print "childMoveLeft"
		#MoveUp is possible
		#gameAreastate does not change, only player pos changes
		#add it to mainStack
		tempGameAreaState = currentNode.gamestate[:]
		mainStack.append(Node(Position(currentNode.ppos.v,currentNode.ppos.h+1),tempGameAreaState))