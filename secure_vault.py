import tracemalloc

class SecureVault:
    # 🌟 DAY 4: Slots Optimization (Mangled names ke sath)
    __slots__ = ['user_name', '_SecureVault__pin', '_SecureVault__balance']
    
    def __init__(self, user_name, pin, initial_deposit):
        self.user_name = user_name
        self.__pin = pin                       # 🌟 DAY 2: Private Variable
        self.__balance = initial_deposit       # 🌟 DAY 2: Private Variable
        
    # 🌟 DAY 3: Getter Property (Safe Read)
    @property
    def balance(self):
        return self.__balance
        
    # 🌟 DAY 3: Setter Property with Edge-Case Validation (Safe Write)
    @balance.setter
    def balance(self, amount):
        # Validation: Data number hona chahiye aur zero ya zero se bara hona chahiye
        if isinstance(amount, (int, float)) and amount >= 0:
            self.__balance = amount
            print(f"✅ Balance updated to: {self.__balance}")
        else:
            print("❌ Invalid Input! Amount must be a positive number.")

def run_test():
    # 1. Testing Memory Footprint
    tracemalloc.start()
    vaults = [SecureVault(f"User_{i}", 1122, 100.0) for i in range(100000)]
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"⚡ 100k Vaults RAM Size: {peak / (1024 * 1024):.2f} MB")
    
    # 2. Testing Security & Edge Cases
    my_vault = SecureVault("Adil", 7860, 5000.0)
    print(f"Initial Balance: {my_vault.balance}")
    
    my_vault.balance = 6500.0  # Sahi data
    my_vault.balance = -200    # Edge Case 1: Negative number check
    my_vault.balance = "cash"  # Edge Case 2: String validation check

# 🌟 DAY 4: Guard Clause (Chaukidar)
if __name__ == "__main__":
    run_test()
