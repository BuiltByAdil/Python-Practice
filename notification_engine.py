from abc import ABC, abstractmethod
class NotificationVendor(ABC):
	@abstractmethod
	def send_notification(self, recipient: str, message: str) -> bool:
		pass
		
	@abstractmethod
	def check_delivery_status(self, message_id: str) -> str:
		pass
		
	def log_transaction(self, vendor_name: str):
		print(f"📝 [LOG]: Security & Audit payload saved for vendor: {vendor_name}.")
		
class TwilioSMS(NotificationVendor):
	def send_notification(self, recipient: str, message: str) -> bool:
		print("Your Alert Message has been deliverd")
		return True
		
class SendGridEmail(NotificationVendor):
	def send_notification(self, recipient: str, message: str) -> bool:
		print("Your Alert Message has been deliverd")
		return True
		
	def check_delivery_status(self, message_id: str) -> str:
		print("Checked Message Alert Status")
		return "Delivered"
		
if __name__ == "__main__":
#	v1 = TwilioSMS()
#	v1.send_notification()
#	
	v2 = SendGridEmail()
	print(v2.send_notification("adil","Go to Lahore"))
	print(v2.check_delivery_status("m12"))
	v2.log_transaction("Ali")