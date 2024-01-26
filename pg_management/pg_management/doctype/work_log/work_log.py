# Copyright (c) 2024, Ajay and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils.data import today

class WorkLog(Document):
	pass



def create_work_log():
	room_list=frappe.db.get_all("Room",{"docstatus":0},["name"])
	work_list=frappe.db.get_all("PG Work",{"docstatus":0},["name","schedulein_days"])
	for k in work_list:
		for j in room_list:
			
			employee=frappe.get_all("PG Employee",{"work",k.name},["name"])
			for k in employee:
				last_schedule=frappe.db.get_value("Work Log",{"room":j.name},["date"])
				work=frappe.db.get_all("Work Log",{"room":j.name,"pg_employee":k.name},["date"])
				if last_schedule:
					if len(work)<=int(len(room_list)/len(employee)):
						pass
					else:
						from datetime import datetime, timedelta
						today = datetime.now().date()
						next_day = today + timedelta(days=1)
						if next_day==today:
							doc=frappe.new_doc("Work Log")
							doc.pg_employee=k.name
							doc.work=k.name
							doc.date=next_day
							doc.room=j.name
							doc.save(ignore_permissions=True)
				else:
					doc=frappe.new_doc("Work Log")
					doc.pg_employee=k.name
					doc.work=k.name
					doc.date=today()
					doc.room=j.name
					doc.save(ignore_permissions=True)


					