# Copyright (c) 2022, niyaz@wahni.com and contributors
# For license information, please see license.txt

import frappe
import requests
from frappe.model.document import Document
from frappe.utils.password import get_decrypted_password


class VoxbaySettings(Document):
	@frappe.whitelist()
	def test_token(self, extension_number, source_number, destination_number):
		uid = get_decrypted_password(self.doctype, self.doctype, "uid")
		pin = get_decrypted_password(self.doctype, self.doctype, "pin")
		callerid = self.callerid
		api_base_url = "http://pbx.voxbaysolutions.com/api"
		endpoint = f"{api_base_url}/clicktocall.php"
		response_data = {
			"uid": uid,
			"pin": pin,
			"source": source_number,
			"destination": destination_number,
			"ext": extension_number,
			"callerid": callerid,
		}

		response = requests.post(
			endpoint,
			params=response_data,
		)

		if response.ok:
			return frappe.msgprint(str(response.text))
		else:
			frappe.msgprint(str(response.reason))


		# endpoint = f"{api_base_url}/clicktocall.php?uid={uid}&pin={pin}&source={source_number}&destination={destination_number}&ext={extension_number}&callerid={callerid}"