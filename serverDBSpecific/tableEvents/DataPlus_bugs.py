import time

def onInsert(row):
	row.cell("Date added").rawData = int(time.time())
	row.save()
	
def onUpdate(row):
	pass
	
def onDelete(row):
	pass