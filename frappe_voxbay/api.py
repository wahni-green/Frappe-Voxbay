
import frappe
from frappe import _
from frappe_voxbay.utils import VoxbayAPI

@frappe.whitelist()
def clicktocall(destination_number=None):
    """Type: Mobile to Mobile"""
    extension_number, source_number = frappe.db.get_value("Voxbay Agent Settings User", {"user": frappe.session.user}, ["extension_number", "source_number"])
    if not source_number:
        frappe.throw(_(f"Please Set Agent Mobile Number ><b>Voxbay Agent Settings</b>"))
    if not extension_number:
        frappe.throw(_(f"Please Set Agent Extension Number ><b>Voxbay Agent Settings</b>"))

    VoxbayAPI().voxbaycall(
        endpoint="clicktocall",
        destination_number=destination_number
	)

@frappe.whitelist()
def call(destination_number):
    """Type: Extension to Mobile"""

    VoxbayAPI().voxbaycall(
        endpoint="call",
        destination_number=destination_number
	)