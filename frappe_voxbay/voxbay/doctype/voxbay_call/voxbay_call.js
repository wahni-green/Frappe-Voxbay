// Copyright (c) 2022, niyaz@wahni.com and contributors
// For license information, please see license.txt

frappe.ui.form.on('Voxbay Call', {
	refresh: function (frm) {
		frm.disable_save();
		frm.add_custom_button(__('Call'), () =>
			frm.trigger("call")
		);
	},
	call: function (frm) {
		frm.call("call_destination");
	}
});
