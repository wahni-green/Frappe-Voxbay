# Copyright (c) 2022, niyaz@wahni.com and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document

from frappe_voxbay.api import call, clicktocall


class VoxbayCall(Document):
	@frappe.whitelist()
	def call_destination(self):
		self.validate_agent()
		if self.type == "Mobile to Mobile":
			clicktocall(self.destination_number)
		elif self.type == "Extension to Mobile":
			call(self.destination_number)


	def validate_agent(self):
		source_number = frappe.db.get_value("Voxbay Agent Settings User", {"user": frappe.session.user}, "source_number")
		if not source_number:
			frappe.throw(_(f"Please Set Agent Mobile Number > <b>Voxbay Agent Settings</b>"))
		extension_number = frappe.db.get_value("Voxbay Agent Settings User", {"user": frappe.session.user}, "extension_number")
		if not extension_number:
			frappe.throw(_(f"Please Set Agent Extension Number > <b>Voxbay Agent Settings</b>"))

