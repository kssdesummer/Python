import execjs
import pymysql


# n = 0
# num1 = []
# for i in nums:
#     if tags-i in nums:
#         print(n,nums.index(tags-i))
#     n += 1
class Demo:
    def twoNum(self, nums, target):
        lens = len(nums)
        j = -1
        for i in range(lens):
            if (target - nums[i]) in nums:
                # if (nums.count(target - nums[i]) >= 2):
                #     for i in
                # 如果num2=num1,且nums中只出现了一次，说明找到是num1本身。
                #     continue
                # else:
                j = nums.index(target - nums[i], i + 1, lens)
                # index(x,i+1)是从num1后的序列后找num2,i+1是开始的索引值
                # break
                if j > 0:
                    return [i, j]
                else:
                    return []
            else:
                pass


nums = [2, 3, 4, 2, 2, 5]
print([i for i, x in enumerate(nums) if x == 2])
tags = 4
two = Demo()
answer = two.twoNum(nums, tags)
print(answer)

s = [1, 2, 3, 4, 5]
i = 0
i = s[i] = 3
print(i)
print(s)

a = execjs.eval("'red yellow blue'.split(' ')")
print(a)
ctx = execjs.compile(
    """
     function add(x, y) {
         return x + y;
     }
    """
)
b = ctx.call("add", 1, 2)
print(b)


db = pymysql.connect("localhost","root","mysql","python")
cursor = db.cursor()
sql = "select * from users"
cursor.execute(sql)
res = cursor.fetchall()
print(res)
db.close()


