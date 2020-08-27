package org.psawesome;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;

/**
 * @author ps [https://github.com/wiv33/learning-python]
 * @role
 * @responsibility
 * @cooperate {
 * input:
 * output:
 * }
 * @see
 * @since 20. 8. 27. Thursday
 */
public class Solution {

  public List<List<Integer>> threeSum(int[] nums) {
    var result = new ArrayList<List<Integer>>();
    var isContains = new HashSet<List<Integer>>();
    Arrays.sort(nums);

    for (int i = 0; i < nums.length - 2; i++) {
      int left_idx = i + 1, right_idx = nums.length - 1;

      while (left_idx < right_idx) {
        var sum = nums[i] + nums[left_idx] + nums[right_idx];
        if (sum < 0) {
          left_idx++;
        } else if (sum > 0) {
          right_idx--;
        } else {
          final List<Integer> anInt = List.of(nums[i], nums[left_idx], nums[right_idx]);
          if (!isContains.contains(anInt)) {
            result.add(anInt);
            isContains.add(anInt);
          }

          left_idx++;
          right_idx--;
        }
      }
    }
    return result;
  }
}
