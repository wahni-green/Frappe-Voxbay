import frappe
from frappe.custom.doctype.property_setter.property_setter import \
    make_property_setter


def add_status_option_call_log():
	options = (frappe.get_meta("Call Log").get_field("status").options).split("\n")
	status = ["ANSWERED", "BUSY", "NOANSWER", "CONGESTION", "CHANUNAVAIL", "CANCEL"]
	for row in status:
		if row not in options:
			options.append(row)
			make_property_setter(
				"Call Log",
				"status",
				"options",
				"\n".join(options),
				"Text",
				validate_fields_for_doctype=False
			)

def remove_status_option_call_log():
	options = (frappe.get_meta("Call Log").get_field("status").options).split("\n")
	status = ["ANSWERED", "BUSY", "NOANSWER", "CONGESTION", "CHANUNAVAIL", "CANCEL"]
	for row in status:
		if row in options:
			options.remove(row)
			make_property_setter(
				"Call Log",
				"status",
				"options",
				"\n".join(options),
				"Text",
				validate_fields_for_doctype=False
			)