frappe.ui.form.on("Opportunity", {
    refresh: function (frm) {
        console.log("hiiiiiiiiiiiiiiiiiiiiiiiiiii");
        if (!frm.doc.__islocal) {
            frm.add_custom_button(__("Call"), () => {
                call_lead(frm);
            });
        }
    }
})

function call_lead(frm) {
    let d = new frappe.ui.Dialog({
        title: __("Call"),
        fields: [
            {
                label: __("To"),
                fieldtype: "Autocomplete",
                reqd: 1,
                fieldname: "recipient",
                default: frm.doc.mobile_no ? frm.doc.mobile_no : "",
                ignore_validation: true,
            },
        ],
        primary_action_label: __("Call"),
        primary_action(values) {
            voxbay.utils.clicktocall(values.recipient)
            d.hide();
        },
    });
    let numbers = [frm.doc.mobile_no]
    if (frm.doc.whatsapp_no) {
        numbers.push(frm.doc.whatsapp_no)
    }
    if (frm.doc.phone) {
        numbers.push(frm.doc.phone)
    }
    d.get_field("recipient").set_data(numbers);
    d.show();
}