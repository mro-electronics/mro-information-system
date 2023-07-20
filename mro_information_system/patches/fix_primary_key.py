import frappe

def execute():
    asset_list = frappe.get_list("MRO IT Asset",fields=["name","user_auth"])

    for a in asset_list:
        doc_auth = frappe.get_doc("MRO User Auth", a.get("user_auth"))
        frappe.db.set_value("MRO IT Asset", a.get("name"), "user_auth", doc_auth.get("auth_method"))

    auth_list = frappe.get_list("MRO User Auth", fields=["name","auth_method"])
    for a in auth_list:
        frappe.db.set_value("MRO User Auth", a.get("name"), "name", a.get("auth_method"))
