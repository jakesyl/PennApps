import json
import MySQLdb as mdb
def dbquery(query):
	con = mdb.connect('127.0.0.1', 'root', "emerson1", 'Pennapps');
	cur = con.cursor(mdb.cursors.DictCursor)
	cur.execute(query)
	results =  cur.fetchall()
	con.close()
	return results
def dbinsert(query):
	con = mdb.connect('127.0.0.1', 'root', "emerson1", 'Pennapps');
	cur = con.cursor(mdb.cursors.DictCursor)
	cur.execute(query)
	results =  cur.fetchall()
	con.commit()
	con.close()

def helpget(input):
	#/help
	if input[:5] == "/help":
		ret = """
		/reply - Reply to a doctor's response.
		/list - Lists all of your chats
		/close - End a chat
		/ask - Ask a quetion
		/help - See this message again"""
		return ret
	else:
		pass
def txtlist(input, number):
	if input[:5] == "/list":
		query = "SELECT * FROM conversations WHERE texternumber = '"+number+"'"
		retval = dbquery(query)
		ret = ""
		c = 0;
		for chat in retval:
			query = "SELECT * FROM doctors WHERE ID = "+chat['doctorID']
			retval2 = dbquery(query)
			ret += "c) "+retval2[0]['name']+": "+chat['question']+"\n"
			c+=1
		return ret
@app.route("/doclist", methods=['GET', 'POST'])
def doclist():
	register_info = request.data
	Datadict = json.loads(register_info)
	start=Datadict['amount']
	specialty = Datadict['special']
	tot ="{"
	query="SELECT * FROM conversations WHERE ID > max(ID)-"+amount+" ORDER BY ID DESC"
	retval = dbquery(query)
	c=0
	for conv in retval:
		query= "SELECT * FROM messages WHERE conversationID = "+str(conv['ID'])
		retval2 = dbquery(query)
		if len(retval2) = 1:
			query = "SELECT * FROM texters WHERE phone = "+conv['texternumber']
			retval3 = dbquery(query)
			tot += '"'str(c)+'": { "question": "'+conv[question]+'", "sendername": "'+retval3[0]['name']+'"},'
	tot = tot[:-1]
	tot += "}"
	return tot