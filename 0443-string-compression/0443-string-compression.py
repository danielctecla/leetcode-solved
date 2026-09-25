class Solution:
  def compress(self, chars: list[str]) -> int:
    
    # input array of elements letter, nums, ...
    # output the size of the compress str

    # 2 pointers : one is for creating the compress and other is for counting char equals
    # [a,a,b]
    #  ^
    #  ^
    #  while right < size of chars
    #     count = 1
    #     char = chars[right] 
    #     next_index = right + 1
    #     while next_index < size of chars and chars[next_index] == char
    #         count += 1
    #         next_index += 1
    #     right = next_index
    #     if count == 1:
    #         chars[left] = char
    #         left += 1
    #     else
    #         count_in_str = str(count)
    #         chars[left] = char
    #         left += 1
    #         for i in count_in_str:
    #             chars[left] = char
    #             left += 1
    #  return left
    #  0 1 2
    # [a,2,b] len 3
    # left = 3
    # right = 3
    # test            count = 1,char = b      next ind = 3
    left, right = 0, 0
    size_chars = len(chars)
    
    while right < size_chars:
      count = 1
      char = chars[right]
      next_index = right + 1
      
      while next_index < size_chars and chars[next_index] == char:
        count += 1
        next_index += 1
      
      right = next_index

      chars[left] = char
      left += 1
      if count != 1:
        count_str = str(count)
        for num in count_str:
          chars[left] = num
          left += 1

    return left