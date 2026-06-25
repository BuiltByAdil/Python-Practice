class BaseNotification:
	def send(self):
		print("📡 Sending core baseline system alert.")
		
class SMSNotification(BaseNotification):
	def send(self):
		print("📱 [SMS] Sending text message to user phone.")
		
class EmailNotification(BaseNotification):
	def send(self):
		print("📧 [Email] Sending HTML email to user inbox.")
		
class MarketingCampaign(SMSNotification, EmailNotification):
	pass
	
	
if __name__ == "__main__":
	campaign = MarketingCampaign()
	print(campaign.send())

	for index, cls in enumerate(MarketingCampaign.__mro__, 1):
		print(f"Level {index}: {cls.__name__}")