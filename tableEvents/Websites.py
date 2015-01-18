import random

def onInsert(row):
	row.cell("Process changes").rawData = "1"
	row.cell("Full build").rawData = "1"
	row.cell("Port number").rawData = random.randint(20000, 21000)
	row.save(False)

def onUpdate(row):
	row.cell("Process changes").rawData = "1"
	if not row.cell("Port number").rawData:
		row.cell("Port number").rawData = random.randint(20000, 21000)
	row.save(False)