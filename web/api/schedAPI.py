from db import Database
import web
import json
"""
Implements /getschedule from API
"""
class GetScheduleServlet:
	def GET(self):
		dbase=Database()

		user_data = web.input()
		if not dbase.verify_user(user_data.userid, user_data.token):
			return "Please authenticate when using the API"
		classes=dbase.getDayClasses(user_data.userid)
		dclass=[]
		for cls in classes:
			cls.timestamp=cls.timestamp.strftime("%H:%M %m/%d/%Y") # JSON friendly date formats.
			cls.timeend=cls.timeend.strftime("%H:%M %m/%d/%Y")
			dclass.append({"id":cls.id,"class_name":cls.class_name,"section":cls.section,"timestamp":cls.timestamp,"timeend":cls.timeend,"instructor":cls.instructor,"type":cls.type,"where":cls.where})
		web.header("Content-Type","application/json")
		return json.dumps(dclass)