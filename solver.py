import sys
import itertools
import copy

# Node data structure for storing player position and state of current game
class Node(object):
    def __init__(self,ppos,gamestate,parentNode,move):
        self.ppos=ppos
        self.gamestate=gamestate
        self.parentNode=parentNode
        self.move=move

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

def printPath(currentNode,flag):
	oplist = []
	while not currentNode == None:
		if flag == True:
			oplist.append(str(currentNode.move))
		else:
			oplist.append(prpos(currentNode.ppos)+""+str(currentNode.move))
		# print prpos(currentNode.ppos),
		currentNode = currentNode.parentNode
	print oplist[::-1]

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

# startpos = Position(3,0)
# goalpos = Position(3,3)
# startAreaState = [
# 				[0,0,0,1],
# 				[0,0,1,0],
# 				[0,1,0,0],
# 				[0,1,0,0]
# 			]

startGameState = Node(startpos,startAreaState,None,None)
# print startState[startpos.v][startpos.h]

processedNodes = []

mainStack = []
mainStackHash = []
mainStack.append(startGameState)
mainStackHash.append(getStateHash(startGameState))

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
	mainStackHash.pop(0)

	#check if we have reached goal state
	if currentNode.ppos.v == goalpos.v and currentNode.ppos.h == goalpos.h:
		print "Found solution.."
		oplist = []
		while not currentNode == None:
			oplist.append(prpos(currentNode.ppos)+""+str(currentNode.move))
			# print prpos(currentNode.ppos),
			currentNode = currentNode.parentNode
		print oplist[::-1]
		sys.exit()

	#generate possible child nodes
	# 1. childMoveUp
	print prpos(currentNode.ppos)+" \t- Up -\t\t "+prpos(Position(currentNode.ppos.v-1,currentNode.ppos.h)),
	# check if that space is empty and hence can be moved into, and also check if we are still inside game area
	if currentNode.ppos.v-1 >= 0 and currentNode.gamestate[currentNode.ppos.v-1][currentNode.ppos.h] == 0:
		#MoveUp is possible
		#gameAreastate does not change, only player pos changes
		#add it to mainStack
		tempGameAreaState = copy.deepcopy(currentNode.gamestate)
		moveUpState = Node(Position(currentNode.ppos.v-1,currentNode.ppos.h),tempGameAreaState,currentNode,"MU")
		if not getStateHash(moveUpState) in processedNodes and not getStateHash(moveUpState) in mainStackHash:
			mainStack.append(moveUpState)
			mainStackHash.append(getStateHash(moveUpState))
			print " \t- Possible"
		else:
			print " \t- Already processed"
	else:
		print " \t- Not Possible \t",
		tempGameAreaState = copy.deepcopy(currentNode.gamestate)
		moveUpState = Node(Position(currentNode.ppos.v-1,currentNode.ppos.h),tempGameAreaState,currentNode,"MU")
		printPath(moveUpState,True)

	# 2. childMoveDown
	print prpos(currentNode.ppos)+" \t- Down -\t "+prpos(Position(currentNode.ppos.v+1,currentNode.ppos.h)),
	# check if that space is empty and hence can be moved into, and also check if we are still inside game area
	if currentNode.ppos.v+1 < gameAreaSizeV and currentNode.gamestate[currentNode.ppos.v+1][currentNode.ppos.h] == 0:
		#MoveUp is possible
		#gameAreastate does not change, only player pos changes
		#add it to mainStack
		tempGameAreaState = copy.deepcopy(currentNode.gamestate)
		moveDownState = Node(Position(currentNode.ppos.v+1,currentNode.ppos.h),tempGameAreaState,currentNode,"MD")
		if not getStateHash(moveDownState) in processedNodes and not getStateHash(moveDownState) in mainStackHash:
			print " \t- Possible"
			mainStack.append(moveDownState)
			mainStackHash.append(getStateHash(moveDownState))
		else:
			print " \t- Already Processed"
	else:
		print " \t- Not Possible \t",
		tempGameAreaState = copy.deepcopy(currentNode.gamestate)
		moveDownState = Node(Position(currentNode.ppos.v+1,currentNode.ppos.h),tempGameAreaState,currentNode,"MD")
		printPath(moveUpState,True)


	# 3. childMoveLeft
	print prpos(currentNode.ppos)+" \t- Left -\t "+prpos(Position(currentNode.ppos.v,currentNode.ppos.h-1)),
	# check if that space is empty and hence can be moved into, and also check if we are still inside game area
	if currentNode.ppos.h-1 >= 0 and currentNode.gamestate[currentNode.ppos.v][currentNode.ppos.h-1] == 0:
		#MoveUp is possible
		#gameAreastate does not change, only player pos changes
		#add it to mainStack
		tempGameAreaState = copy.deepcopy(currentNode.gamestate)
		moveLeftState = Node(Position(currentNode.ppos.v,currentNode.ppos.h-1),tempGameAreaState,currentNode,"ML")
		if not getStateHash(moveLeftState) in processedNodes and not getStateHash(moveLeftState) in mainStackHash:
			print " \t- Possible"
			mainStack.append(moveLeftState)
			mainStackHash.append(getStateHash(moveLeftState))
		else:
			print " \t- Already Processed"
	else:
		print " \t- Not Possible \t",
		tempGameAreaState = copy.deepcopy(currentNode.gamestate)
		moveLeftState = Node(Position(currentNode.ppos.v,currentNode.ppos.h-1),tempGameAreaState,currentNode,"ML")
		printPath(moveUpState,True)

	# 4. childMoveRight
	print prpos(currentNode.ppos)+" \t- Right -\t "+prpos(Position(currentNode.ppos.v,currentNode.ppos.h+1)),
	# check if that space is empty and hence can be moved into, and also check if we are still inside game area
	if currentNode.ppos.h+1 < gameAreaSizeH and currentNode.gamestate[currentNode.ppos.v][currentNode.ppos.h+1] == 0:
		#MoveUp is possible
		#gameAreastate does not change, only player pos changes
		#add it to mainStack
		tempGameAreaState = copy.deepcopy(currentNode.gamestate)
		moveRightState = Node(Position(currentNode.ppos.v,currentNode.ppos.h+1),tempGameAreaState,currentNode,"MR")
		if not getStateHash(moveRightState) in processedNodes and not getStateHash(moveRightState) in mainStackHash:
			print " \t- Possible"
			mainStack.append(moveRightState)
			mainStackHash.append(getStateHash(moveRightState))
		else:
			print " \t- Already Processed"
	else:
		print " \t- Not Possible \t",
		tempGameAreaState = copy.deepcopy(currentNode.gamestate)
		moveRightState = Node(Position(currentNode.ppos.v,currentNode.ppos.h+1),tempGameAreaState,currentNode,"MR")
		printPath(moveUpState,True)

	#push moves implementation
	curpos = currentNode.ppos

	# 1. Push up
	print prpos(currentNode.ppos)+" \t- Push Up -\t "+prpos(currentNode.ppos),
	# check if move possible
	# conditions
	# 	1. boulder present in direction of push
	# 	2. place where bolder will be pushed is inside the matrix
	# 	3. empty space where bolder will be pushed
	if (curpos.v-2) >= 0 and currentNode.gamestate[curpos.v-1][curpos.h] == 1 and currentNode.gamestate[curpos.v-2][curpos.h] == 0:
		tempGameAreaState = copy.deepcopy(currentNode.gamestate)
		tempGameAreaState[curpos.v-1][curpos.h] = 0
		tempGameAreaState[curpos.v-2][curpos.h] = 1
		pushUpState = Node(curpos,tempGameAreaState,currentNode,"PU")
		if not getStateHash(pushUpState) in processedNodes and not getStateHash(pushUpState) in mainStackHash:
			print " \t- Possible"
			mainStack.append(pushUpState)
			mainStackHash.append(getStateHash(pushUpState))
		else:
			print " \t- Already Processed"
	else:
		print " \t- Not Possible \t"
		# tempGameAreaState = copy.deepcopy(currentNode.gamestate)
		# tempGameAreaState[curpos.v-1][curpos.h] = 0
		# tempGameAreaState[curpos.v-2][curpos.h] = 1
		# pushUpState = Node(curpos,tempGameAreaState,currentNode,"PU")
		# printPath(pushUpState,True)

	curpos = currentNode.ppos
	# 2. Push down
	print prpos(currentNode.ppos)+" \t- Push Down -\t "+prpos(currentNode.ppos),
	# check if move possible
	if (curpos.v+2) < gameAreaSizeV and currentNode.gamestate[curpos.v+1][curpos.h] == 1 and currentNode.gamestate[curpos.v+2][curpos.h] == 0:
		tempGameAreaState = copy.deepcopy(currentNode.gamestate)
		tempGameAreaState[curpos.v+1][curpos.h] = 0
		tempGameAreaState[curpos.v+2][curpos.h] = 1
		pushDownState = Node(curpos,tempGameAreaState,currentNode,"PD")
		if not getStateHash(pushDownState) in processedNodes and not getStateHash(pushDownState) in mainStackHash:
			print " \t- Possible"
			mainStack.append(pushDownState)
			mainStackHash.append(getStateHash(pushDownState))
		else:
			print " \t- Already Processed"
	else:
		print " \t- Not Possible \t"
		# tempGameAreaState = copy.deepcopy(currentNode.gamestate)
		# tempGameAreaState[curpos.v+1][curpos.h] = 0
		# tempGameAreaState[curpos.v+2][curpos.h] = 1
		# pushDownState = Node(curpos,tempGameAreaState,currentNode,"PD")
		# printPath(pushDownState,True)

	curpos = currentNode.ppos
	# 3. Push left
	print prpos(currentNode.ppos)+" \t- Push Left -\t "+prpos(currentNode.ppos),
	# check if move possible
	if (curpos.h-2) >= 0 and currentNode.gamestate[curpos.v][curpos.h-1] == 1 and currentNode.gamestate[curpos.v][curpos.h-2] == 0:
		tempGameAreaState = copy.deepcopy(currentNode.gamestate)
		tempGameAreaState[curpos.v][curpos.h-1] = 0
		tempGameAreaState[curpos.v][curpos.h-2] = 1
		pushLeftState = Node(curpos,tempGameAreaState,currentNode,"PL")
		if not getStateHash(pushLeftState) in processedNodes and not getStateHash(pushLeftState) in mainStackHash:
			print " \t- Possible"
			mainStack.append(pushLeftState)
			mainStackHash.append(getStateHash(pushLeftState))
		else:
			print " \t- Already Processed"
	else:
		print " \t- Not Possible \t"
		# tempGameAreaState = copy.deepcopy(currentNode.gamestate)
		# tempGameAreaState[curpos.v][curpos.h-1] = 0
		# tempGameAreaState[curpos.v][curpos.h-2] = 1
		# pushLeftState = Node(curpos,tempGameAreaState,currentNode,"PL")
		# printPath(pushLeftState,True)


	curpos = currentNode.ppos
	# 4. Push Right
	print prpos(currentNode.ppos)+" \t- Push Right -\t "+prpos(currentNode.ppos),
	# check if move possible
	if (curpos.h+2) < gameAreaSizeH and currentNode.gamestate[curpos.v][curpos.h+1] == 1 and currentNode.gamestate[curpos.v][curpos.h+2] == 0:
		tempGameAreaState = copy.deepcopy(currentNode.gamestate)
		tempGameAreaState[curpos.v][curpos.h+1] = 0
		tempGameAreaState[curpos.v][curpos.h+2] = 1
		pushRightState = Node(curpos,tempGameAreaState,currentNode,"PR")
		if not getStateHash(pushRightState) in processedNodes and not getStateHash(pushRightState) in mainStackHash:
			print " \t- Possible"
			mainStack.append(pushRightState)
			mainStackHash.append(getStateHash(pushRightState))
		else:
			print " \t- Already Processed"
	else:
		print " \t- Not Possible \t"
		# tempGameAreaState = copy.deepcopy(currentNode.gamestate)
		# tempGameAreaState[curpos.v][curpos.h-1] = 0
		# tempGameAreaState[curpos.v][curpos.h-2] = 1
		# pushLeftState = Node(curpos,tempGameAreaState,currentNode,"PL")
		# printPath(pushLeftState,True)