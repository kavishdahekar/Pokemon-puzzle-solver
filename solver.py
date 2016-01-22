import sys
import itertools

# Node data structure for storing player position and state of current game
class Node(object):
    def __init__(self,ppos,gamestate,parentNode):
        self.ppos=ppos
        self.gamestate=gamestate
        self.parentNode=parentNode

class Position(object):
    def __init__(self,v,h):
        self.v=v #vertical index
        self.h=h #horizontal index

def showNode(node):
	print "("+str(node.ppos.v)+","+str(node.ppos.h)+")"
	print node.gamestate

def prpos(ppos):
	return "("+str(ppos.v)+","+str(ppos.h)+")"

def getStateHash(stateNode):
	return int(str(stateNode.ppos.v)+""+str(stateNode.ppos.h)+""+str(int(''.join(map(str,list(itertools.chain(*stateNode.gamestate)))),2)))

gameAreaSizeV = 3
gameAreaSizeH = 3
# defining start state and goal state

# startpos = Position(5,2)
# goalpos = Position(0,2)
# startAreaState = [
# 				[1,0,0,0,1],
# 				[1,1,0,1,1],
# 				[0,1,1,1,0],
# 				[1,0,0,0,1],
# 				[0,1,1,1,0],
# 				[0,0,0,0,0],
# 			]

startpos = Position(2,0)
goalpos = Position(0,0)
startAreaState = [
				[0,0,0],
				[1,1,0],
				[0,0,0]
			]

startGameState = Node(startpos,startAreaState,None)
# print startState[startpos.v][startpos.h]

processedNodes = []

mainStack = []
mainStack.append(startGameState)

while 1:
	# if stack empty, exit
	if len(mainStack) == 0:
		print "No solution found..."
		sys.exit()

	#Get current node as the top node from stack
	currentNode = mainStack[0]
	#Add to processed states
	processedNodes.append(getStateHash(currentNode))
	#Remove that node from stack
	mainStack.pop(0)

	#check if we have reached goal state
	if currentNode.ppos.v == goalpos.v and currentNode.ppos.h == goalpos.h:
		print "Found solution.."
		oplist = []
		while not currentNode == None:
			oplist.append(prpos(currentNode.ppos))
			# print prpos(currentNode.ppos),
			currentNode = currentNode.parentNode
		print oplist[::-1]
		sys.exit()

	#generate possible child nodes
	# 1. childMoveUp
	print prpos(currentNode.ppos)+" - Up - "+prpos(Position(currentNode.ppos.v-1,currentNode.ppos.h)),
	# check if that space is empty and hence can be moved into, and also check if we are still inside game area
	if currentNode.ppos.v-1 >= 0 and currentNode.gamestate[currentNode.ppos.v-1][currentNode.ppos.h] == 0:
		#MoveUp is possible
		#gameAreastate does not change, only player pos changes
		#add it to mainStack
		tempGameAreaState = currentNode.gamestate[:]
		moveUpState = Node(Position(currentNode.ppos.v-1,currentNode.ppos.h),tempGameAreaState,currentNode)
		if not getStateHash(moveUpState) in processedNodes:
			mainStack.append(moveUpState)
			print " - Possible"
		else:
			print " - Already processed"
	else:
		print "- Not Possible"

	# 2. childMoveDown
	print prpos(currentNode.ppos)+" - Down - "+prpos(Position(currentNode.ppos.v+1,currentNode.ppos.h)),
	# check if that space is empty and hence can be moved into, and also check if we are still inside game area
	if currentNode.ppos.v+1 < gameAreaSizeV and currentNode.gamestate[currentNode.ppos.v+1][currentNode.ppos.h] == 0:
		#MoveUp is possible
		#gameAreastate does not change, only player pos changes
		#add it to mainStack
		tempGameAreaState = currentNode.gamestate[:]
		moveDownState = Node(Position(currentNode.ppos.v+1,currentNode.ppos.h),tempGameAreaState,currentNode)
		if not getStateHash(moveDownState) in processedNodes:
			print " - Possible"
			mainStack.append(moveDownState)
		else:
			print " - Already Processed"
	else:
		print "- Not Possible"


	# 3. childMoveLeft
	print prpos(currentNode.ppos)+" - Left - "+prpos(Position(currentNode.ppos.v,currentNode.ppos.h-1)),
	# check if that space is empty and hence can be moved into, and also check if we are still inside game area
	if currentNode.ppos.h-1 >= 0 and currentNode.gamestate[currentNode.ppos.v][currentNode.ppos.h-1] == 0:
		#MoveUp is possible
		#gameAreastate does not change, only player pos changes
		#add it to mainStack
		tempGameAreaState = currentNode.gamestate[:]
		moveLeftState = Node(Position(currentNode.ppos.v,currentNode.ppos.h-1),tempGameAreaState,currentNode)
		if not getStateHash(moveLeftState) in processedNodes:
			print " - Possible"
			mainStack.append(moveLeftState)
		else:
			print " - Already Processed"
	else:
		print "- Not Possible"

	# 4. childMoveRight
	print prpos(currentNode.ppos)+" - Right - "+prpos(Position(currentNode.ppos.v,currentNode.ppos.h+1)),
	# check if that space is empty and hence can be moved into, and also check if we are still inside game area
	if currentNode.ppos.h+1 < gameAreaSizeH and currentNode.gamestate[currentNode.ppos.v][currentNode.ppos.h+1] == 0:
		#MoveUp is possible
		#gameAreastate does not change, only player pos changes
		#add it to mainStack
		tempGameAreaState = currentNode.gamestate[:]
		moveRightState = Node(Position(currentNode.ppos.v,currentNode.ppos.h+1),tempGameAreaState,currentNode)
		if not getStateHash(moveRightState) in processedNodes:
			print " - Possible"
			mainStack.append(moveRightState)
		else:
			print " - Already Processed"
	else:
		print "- Not Possible"