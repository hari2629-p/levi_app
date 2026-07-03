# Copyright (c) 2026, HGP and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class BookIssue(Document):
	def validate(self):
		# frappe.msgprint("Hello Harigovind! Validation is running.")
		existing = frappe.db.exists("Book Issue",{
			"book": self.book,
			"status": "Issued",
			"name": ["!=", self.name]
		})

		if existing:
			frappe.throw("This book is already issued by someone!")
