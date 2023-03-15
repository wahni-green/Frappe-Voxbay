# Copyright (c) 2023, Wahni IT Solutions and contributors
# For license information, please see license.txt

import json

import frappe
from frappe import _
from frappe.integrations.utils import create_request_log

from frappe_voxbay.utils import VoxbayAPI


@frappe.whitelist()
def clicktocall(destination_number):
	"""Type: Mobile to Mobile"""

	source_number = frappe.db.get_value("Voxbay Agent Settings User", {"user": frappe.session.user}, "source_number")
	if not source_number:
		frappe.throw(_("Please Set Agent Mobile Number ><b>Voxbay Agent Settings</b>"))
	extension_number = frappe.db.get_value("Voxbay Agent Settings User", {"user": frappe.session.user}, "extension_number")
	if not extension_number:
		frappe.throw(_("Please Set Agent Extension Number ><b>Voxbay Agent Settings</b>"))

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


@frappe.whitelist(allow_guest=True, methods=["POST"])
def cdr_voxbay_log():
	if not is_integration_enabled():
		return "Disabled"

	request_log = create_request_log(
		str(frappe.request.data),
		request_description="Voxbay Call",
		service_name="Voxbay",
		request_headers=frappe.request.headers,
	)

	try:
		call_payload = json.loads(frappe.request.data)
		create_call_log(
			extension=call_payload["extension"],
			destination=call_payload["destination"],
			callerid = call_payload["callerid"],
			duration = call_payload["duration"],
			date = call_payload["date"],
			status = call_payload["status"],
			recording_URL = call_payload["recording_URL"],
			type = call_payload["type"],
		)
		request_log.status = "Completed"
		request_log.save(ignore_permissions=True)
		return "Success"
	except Exception as e:
		request_log.status = "Failed"
		request_log.error = frappe.get_traceback()
		frappe.log_error(
			title="Error while creating voxbay call record",
			message=str(request_log.error)
		)
		request_log.save(ignore_permissions=True)
		frappe.local.response["status_code"] = 400
		frappe.local.response["message"] = str(e)


def create_call_log(
	extension,
	destination,
	callerid,
	duration,
	date,
	status,
	recording_URL=None,
	type="Outgoing"
):
	call_log = frappe.new_doc("Call Log")
	call_log.id = frappe.generate_hash(length=10)
	call_log.to = destination
	call_log.status = status
	call_log.medium = callerid
	call_log.start_time = date
	call_log.type = type
	call_log.duration = duration
	call_log.recording_url = recording_URL
	setattr(call_log, "from", extension)
	call_log.save(ignore_permissions=True)
	frappe.db.commit()
	return call_log


def is_integration_enabled():
	return frappe.db.get_single_value("Voxbay Settings", "enabled", True)
