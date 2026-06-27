from typing import Protocol
from abc import ABC, abstractmethod

class NotificationProtocol(Protocol):
	def send_notification(self, message: str) -> None:
		...

class BaseLoger(ABC):
	@abstractmethod
	def get_source(self) -> str:
		pass
	
	def log_status(self, msg: str):
		print(f"📝 [LOG FROM {self.get_source()}]: {msg}")
		
class SMSNotifier(BaseLoger):
	def get_source(self):
		return "SMS_Gateway"
	def send_notification(self, message: str) -> None:
		print(f"📱 SMS Sent: {message}")
		
class WhatsAppNotifier:
	def send_notification(self, message: str) -> None:
		print(f"📱 SMS Sent: {message}")
		
class BrokenNotifier:
		def push_message(self, message: str) -> None:
			print(f"💥 Wrong method: {message}")
			

def send_bulk_alert(notifier: NotificationProtocol, text: str):
		notifier.send_notification(text)
		
def dirct_duck_run(any_object, text:str):
		any_object.send_notification(text)
		
sms = SMSNotifier()
whatsapp = WhatsAppNotifier()
broken = BrokenNotifier()

send_bulk_alert(sms, "All alert are delevired")
dirct_duck_run(whatsapp, "Alert Send Via Whatsapp")
dirct_duck_run(broken, "Testing Crash")
		