// Copyright (c) 2026, HGP and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Book Issue", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('Book Issue', {
    issue_date(frm) {
        if (frm.doc.issue_date) {
            let due = frappe.utils.add_days(frm.doc.issue_date, 14);
            frm.set_value('due_date', due);
        }
    }
});