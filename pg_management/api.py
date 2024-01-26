import frappe
from frappe.utils.data import getdate

@frappe.whitelist(allow_guest=True)
def get_data(check_in,check_out,room):
    if room=="single":
        room_no=frappe.db.get_all("Room",{"room_type":"Single","availability_status":"Available"},["name"])
        return room_no
    if room=="double":
        room_no=frappe.db.get_all("Room",{"room_type":"Double","availability_status":["in",["Available","Partially Book"]]},["name"])
        for k in room_no:
            erp=frappe.db.get_all("Room Booking Details",{"room_no":k.name,"status":"Open"},["name"])
            k.update({"available":str(len(erp))+"/"+"2"})
        return room_no
    if room=="triple":
        room_no=frappe.db.get_all("Room",{"room_type":"Triple","availability_status":["in",["Available","Partially Book"]]},["name"])
        for k in room_no:
            erp=frappe.db.get_all("Room Booking Details",{"room_no":k.name,"status":"Open"},["name"])
            k.update({"available":str(len(erp))+"/"+"3"})
        return room_no
    if room_no=="multiple":
        room_no=frappe.db.get_all("Room",{"room_type":"Multiple Sharing","availability_status":["in",["Available","Partially Book"]]},["name"])
        for k in room_no:
            erp=frappe.db.get_all("Room Booking Details",{"room_no":k.name,"status":"Open"},["name"])
            k.update({"available":str(len(erp))+"/"+"5"})
        return room_no
        

        
@frappe.whitelist(allow_guest=True)
def create_guest(check_in,check_out,room,r_no,f_name,age,gender,m_no,address):
    doc=frappe.new_doc("Customer")
    doc.guest_name=f_name
    doc.age=age
    doc.mobile_no=m_no
    doc.gender=gender
    doc.address=address
    doc.save(ignore_permissions=True)

    room_book=frappe.new_doc("Room Booking Details")
    room_book.guest=doc.name
    room_book.room_no=r_no
    room_book.booking_date=getdate(check_in)
    room_book.save(ignore_permissions=True)
