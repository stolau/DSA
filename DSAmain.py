
def legal(item, location):
	legit = []
	for path in item:
		if path[0][0] == location:
			if path not in legit:
				legit.append(path)
		if path[0][1] == location:
			if path not in legit:
				legit.append(path)
	return legit
			
def uniformCostSearch(coords, dest, location):
	
	from DSAutil import StackManager
	stack = StackManager()
	black = StackManager()
	route = StackManager()
	
	# Sets up the list for looping
	currentState = legal(coords.list, location)
	for path in currentState:
		stack.push(path)
	while stack.list:
		currentState = stack.list.pop()
		if currentState[0] not in black.list:
			black.normalPush(currentState[0])
			route.normalPush(currentState)
			location = currentState[0][1]
			if currentState[0][1] == dest:
				print route.list
				print "yo maan"
			# print location
			paths = legal(coords.list, location)
			for path in paths:
				# print path
				stack.push(path)
			# print "stack puskennan jalkeen"
			# print stack.list

def main():
	location = input("Give starting location: ")
	file = raw_input("Give me the file: ")
	try:
		myFile = open(file, "r")
		sFile = myFile.readlines()
	except IOError, NameError:
		sys.stderr.write( "Error: Could not open %s\n" % (inputFn) )
		sys.exit(-1)
		
	from DSAutil import FileManager
	coords = FileManager()
	
	# Let's handle file to correct form
	# Destination, citycount and pathcount is out
	dest = int(sFile.pop(len(sFile) - 1))
	sFile.pop(0)
	
	coords.handler(sFile)
	
	uniformCostSearch(coords, dest, location)



main()