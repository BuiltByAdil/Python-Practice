import tracemalloc

class Regular_User:
	def __init__(self, user_name, email):
		self.user_name = user_name
		self.email = email
		
class Optimize_User:
		__slots__ = ['user_name','email']
		def __init__(self, user_name, email):
			self.user_name = user_name
			self.email = email
			
def memory_size():
		tracemalloc.start()
		regular_user_objects = [Regular_User("Adil", "adil@gmail.com") for _ in range(100000)]	
		current, peak = tracemalloc.get_traced_memory()
		tracemalloc.stop()
		regular_size = peak/(1024*1024)
		print(f"100k Regular Users take Size in Memory: {regular_size: .2f}MB")
		
		tracemalloc.start()
		optimize_user_objects = [Optimize_User("Ali", "ali@gmail.com") for _ in range(100000)]
		current,peak = tracemalloc.get_traced_memory()
		optimize_size = peak/(1024*1024)
		print(f"100k Optimize Users take Size in Memory: {optimize_size: .2f}MB")
		
		saving_memory = (regular_size - optimize_size)/regular_size * 100
		print(f"Saving Memory Optimize Object in Ram: {saving_memory: .2f}%")
	
	
user1 = Regular_User("Adil", "adil@gmail.com")
user1.age = 25
print("Bahir se varible obj __dict__ mein add ho gaya")

user2 = Optimize_User("Ali", "Ali@gmail.com")
try:
	user2.age = 30
except AttributeError:
	print("You cannot add Variable from outside class")



if __name__ == "__main__":
	memory_size()