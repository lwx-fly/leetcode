from typing import List

class Solution:

    def singleNumber(self, nums: List[int]) -> List[int]:
        a = 0
        for i in nums:
            a = a ^ i
        # 计算a最低的非0位。从右到左第一个非0位
        """
-a在二进制中的表示是补码(2's complement code)形式，即先按位取反再加1

取反得 1111 0101(即1's complement code，反码)
加1得 1111 0110(即2's complement code，补码)
原码(0000 1010) 与 补码(1111 0110) 做与运算(&)，得 0000 0010，即原码 0000 1010的LSB

### 更详细的解释： 我们从右向左看发生了什么：

原码最低非0位右边所有的0，经由取反后全部变为1，反码+1会导致这些1逐位发生进位并变为0，最终进位记到最低非0位
原最低非0位是1，取反后是0，进位到这一位0变成1，不再向左进位
原最低非0位左边的每一位经由取反后 和 原码 进行与运算必为0
        """
        a = a & (-a)
        b = c = 0
        for i in nums:
            if i & a:
                b = b ^ i
            else:
                c = c ^ i
        return [b, c]
