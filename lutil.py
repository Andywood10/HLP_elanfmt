#-------------------------------
# lutil.py
# @version: 1.0
# @updated: 8/5/2010
#-------------------------------
# @author: Andrew Wood
# @contact: andywood@vt.edu
#
# HLP/Jaeger Lab
# University of Rochester
# Rochester, NY
#-------------------------------

def listify(*item):
	"""
	Simple wrapper function to convert a list of arguments into an actual list
	"""
	return list(item)

def flatten(lst):
	"""
	String utility function to flatten an arbitrary nesting of lists into a single list
	-Arguments: lst -- compound list or list of items to convert to a flattened list
	-Return: buildlist -- flattened list
	"""	
	buildlist = []
	for i in lst:
		if type(i) is list:
			buildlist += flatten(i)
		else:
			buildlist.append(i)
	return buildlist

def lflatten(*lst):
	"""
	Utility function to convert a list of parameters into a flattened list
	"""
	return flatten(list(lst))

def multisplit(splittables, targets, keepSplitters=False):
	outlist = []
	
	#convert non list parameters to one-entry lists for consistency
	if type(splittables) is not list:
		splittables = [splittables]
	if type(targets) is not list:
		targets = [targets]
	
	#for each item to be split
	for splittable in splittables:
		tmplist = []
		
		#method for lists
		if type(splittable) is list:
			builder = []
			for i in splittable:
				if i in targets: 
					tmplist.append(builder)
					if keepSplitters: tmplist.append(i)
					builder = []
				else:
					builder.append(i)
			if builder is not "": tmplist.append(builder);
		#method for strings
		elif type(splittable) is str:
			builder = ""
			for c in splittable:
				if c in targets:
					tmplist.append(builder)
					if keepSplitters: tmplist.append(c)
					builder = ""
				else:
					builder += c
			if builder is not "": tmplist.append(builder);
		#only strings and lists are supported
		else:
			print "Error: type ", type(splittable)
		outlist.append(tmplist)
	
	#if result is a one item list, just return the item
	if len(outlist) is 1:
		return outlist[0]
	else:
		return outlist

def removeall(string, targets):
	return "".join(str(multisplit(string, targets)))

def filldict(lst, padvalue):
	return dict(zip(lst,[padvalue for i in range(len(lst))]))