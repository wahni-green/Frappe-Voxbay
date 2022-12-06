// Copyright (c) 2022, niyaz@wahni.com and contributors
// For license information, please see license.txt

frappe.ui.form.on('Voxbay Settings', {
	refresh: function (frm) {
		frm.add_custom_button(__('Verify Token'), () => {
			let d = new frappe.ui.Dialog({
				fields: [
					{
						label: __('Source Number'),
						fieldname: 'source_number',
						fieldtype: 'Data',
						reqd: 1
					},
					{
						label: __('Extension Number'),
						fieldname: 'extension_number',
						fieldtype: 'Data',
						reqd: 1
					},
					{
						label: __('Destination Number'),
						fieldname: 'destination_number',
						fieldtype: 'Data',
						reqd: 1
					},
				],
				primary_action_label: __("Test"),
				primary_action(values) {
					frm.call({
						doc: frm.doc,
						method: 'test_token',
						args: {
							'extension_number': values.source_number,
							'source_number': values.source_number,
							"destination_number": values.destination_number
						},
						callback: function (r) {
							d.hide();
						},
					});
				}
			})
			d.show();
		})
	}

});
