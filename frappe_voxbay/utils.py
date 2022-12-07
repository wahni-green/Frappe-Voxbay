import frappe
import requests
from frappe import _
from frappe.utils.password import get_decrypted_password


class VoxbayAPI:
	def __init__(self):
		self.uid = get_decrypted_password("Voxbay Settings", "Voxbay Settings", "uid")
		self.pin = get_decrypted_password("Voxbay Settings", "Voxbay Settings", "pin")
		self.callerid = frappe.db.get_single_value("Voxbay Settings", "callerid")
		self.api_base_url = "http://pbx.voxbaysolutions.com/api"
		self.extension_number = frappe.db.get_value("Voxbay Agent Settings User", {"user": frappe.session.user}, "extension_number")
		self.source_number = frappe.db.get_value("Voxbay Agent Settings User", {"user": frappe.session.user}, "source_number")


	def voxbaycall(self, destination_number, endpoint):
		url = f"{self.api_base_url}/{endpoint}.php"
		response_data = {
			"uid": self.uid,
			"pin": self.pin,
			"source": self.source_number,
			"destination": destination_number,
			"ext": self.extension_number,
			"callerid": self.callerid,
		}

		response = requests.post(
			url,
			params=response_data,
		)

		if response.ok:
			return frappe.msgprint(str(response.text))
		else:
			frappe.msgprint(str(response.reason))
