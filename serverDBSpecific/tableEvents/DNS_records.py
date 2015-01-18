import os
import dataModel

DNSConfFile = "/etc/dnsmasq.d/DNSrecords"

def onInsert(row):
	rebuildDNS(row.table)
	
def onUpdate(row):
	rebuildDNS(row.table)
	
def onDelete(row):
	rebuildDNS(row.table)
	
def rebuildDNS(table):
	confStr = ""
	for row in table.dataset.rows:
		if row.cell("Is custom record").rawData == "0":
			#handle website link
			cell = row.cell("Website")
			table = dataModel.Table(cell.column.metadata['fkTable'], "DP_TableID")
			row = table.getRow(cell.rawData)
			domain = str(row.cellByColumnName("Domain"))
			
			
			ipAddr = "192.168.1.50"
		else:
			domain = str(row.cell("Domain"))
			ipAddr = str(row.cell("IP address"))
		
		confStr += "address=/" + domain +"/" + ipAddr + "\n"
	
	with open(DNSConfFile, "wt") as file:
		file.write(confStr)
	
	os.system("sudo service dnsmasq restart")