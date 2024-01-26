# my_app/hooks.py

from __future__ import unicode_literals
import frappe

def after_install():
    create_custom_role()

def create_custom_role():
    roles=['PG Manager','PG Employee']
    for i in roles:
        role_name = i
        permissions = [
            
        ]

        # Check if the role already exists
        if not frappe.get_all('Role', filters={'role_name': role_name}):
            # Create a new Role document
            role = frappe.get_doc({
                'doctype': 'Role',
                'role_name': role_name,
                'desk_access': 1,  # Set desk access level as needed
                'permissions': permissions
            })

            # Save the document
            role.insert()
            frappe.db.commit()
