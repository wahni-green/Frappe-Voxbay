frappe.provide("voxbay");
frappe.provide("voxbay.utils");

voxbay.utils.clicktocall = function (destination_number) {
    frappe.call({
        method: "frappe_voxbay.api.clicktocall",
        args: {
            "destination_number": destination_number
        },
        callback: function (r) {
            if(r.message){
                return true
            }
        }
    });
}

voxbay.utils.call = function (destination_number) {
    frappe.call({
        method: "frappe_voxbay.api.call",
        args: {
            "destination_number": destination_number
        },
        callback: function (r) {
            if(r.message){
                return true
            }
        }
    });
}
