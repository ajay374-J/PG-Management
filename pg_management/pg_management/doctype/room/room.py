# Copyright (c) 2024, Ajay and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _
from frappe.utils.data import today


class Room(Document):
	pass




def get_status():
	room_list=frappe.db.get_all("Room",{"docstatus":0},["name","room_type"])
	for i in room_list:
		d=frappe.db.get_all("Room Booking Details",{"room_no":i.name,"posting_date":["<=",today()],"checkout_date":[">=",today()]},["name"])
		doc=frappe.get_doc("Room",i.name)

		if i.room_type=="Single":
			if len(d)==1:
				doc.availability_status="Booked"

		if i.room_type=="Double":
			if len(d)==1:
				doc.availability_status="Partially Booked"
			if len(d)>1:
				doc.availability_status="Booked"

		if i.room_type=="Triple":
			if len(d)<3 and len(d)!=0:
				doc.availability_status="Partially Booked"
			if len(d)==3:
				doc.availability_status="Booked"
		if i.room_type=="Multiple Sharing":
			if len(d)<5 and len(d)!=0:
				doc.availability_status="Partially Booked"
			if len(d)==5:
				doc.availability_status="Booked"

		doc.save(ignore_permissions=True)

			