nums = [ 1 , 3 , 5 , 7 , 9 ]
d = nums[1] - nums[0];
d = int(d);
print(d)
z = []
item = nums[-1]+d;
a = int(input("Enter the total number to be proceeded \n"))
for i in range(1,a):
     nums.append(item);
     z=[nums]
     i = i + 1;
     nums.extend(z);


print(nums)
