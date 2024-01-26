# Copyright (c) 2024, Ajay and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils.data import getdate, today

class RoomBookingDetails(Document):
	def before_save(self):
		self.get_amount()
		
	def after_save(self):
		#Update Room Status
		d=frappe.db.get_all("Room Booking Details",{"room_no":self.room_no,"posting_date":["<=",today()],"checkout_date":[">=",today()]},["name"])
		doc=frappe.get_doc("Room",self.room_no)
		if doc.room_type=="Single":
			if len(d)==1:
				doc.availability_status="Booked"
		if doc.room_type=="Double":
			if len(d)==1:
				doc.availability_status="Partially Booked"
			if len(d)>1:
				doc.availability_status="Booked"

		if doc.room_type=="Triple":
			if len(d)<3 and len(d)!=0:
				doc.availability_status="Partially Booked"
			if len(d)==3:
				doc.availability_status="Booked"
		if doc.room_type=="Multiple Sharing":
			if len(d)<5 and len(d)!=0:
				doc.availability_status="Partially Booked"
			if len(d)==5:
				doc.availability_status="Booked"

		doc.save(ignore_permissions=True)


	def get_amount(self):
		
		diff=getdate(self.checkout_date)-getdate(self.booking_date)
		room=frappe.get_doc("Room",self.room_no)
		room.amount=diff.days*room.rent

		

