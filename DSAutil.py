class StackManager:
	# Contains basic priority queue policy
	def __init__(self):
		self.list = []
		
	def push(self, item):
		k = 0
		print len(self.list)
		if len(self.list) > 0:
				for path in self.list:
					if path[1] > item[1]:
						k = k + 1
					else:
						self.list.insert(k, item)
						break
		else:
			self.list.append(item)
			
	def pop(self):
		self.list.pop()
		
	def isEmpty(self):
		return len(self.list) == 0
		
	def normalPush(self, item):
		self.list.append(item)
		
	

class FileManager:

	# Contains file handling methods
	def __init__(self):
		self.list = []
	
	def handler(self, item):
		j = 0
		while j < len(item):
			item[j] = item[j].split(" ")
			item[j] = [int(i) for i in item[j]]
			item[j] = [tuple([item[j][0],item[j][1]]), item[j][2]]
			j += 1
		for i in item:
			self.list.append(i)
			
