import sys
class Member:
    def get_discount(self):
        return 1.0
class VIPMember(Member):
    def get_discount(self):
        return 0.8
class GoldMember(Member):
    def get_discount(self):
        return 0.7
def create_member(level):
    if level == "VIP":
        return VIPMember()
    elif level == "Gold":
        return GoldMember()
    else:
        return Member()
n = int(sys.stdin.readline().strip())
for _ in range(n):
    level, amount = sys.stdin.readline().split()
    amount = int(amount)
    member = create_member(level)
    final_price = int(amount * member.get_discount())
    print(final_price)