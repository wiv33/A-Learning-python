package org.psawesome;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.Arrays;
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
class SolutionTest {
  Solution solution;

  @BeforeEach
  void setUp() {
    solution = new Solution();
  }

  @AfterEach
  void tearDown() {
    solution = null;
  }

  @Test
  void testFirstLoop() {
    final int[] ints = {-1, 0, 1, 2, -1, -4};
    List<List<Integer>> actual = solution.threeSum(ints);
    List<List<Integer>> expected = Arrays.asList(Arrays.asList(-1, 0, 1), Arrays.asList(-1, -1, 2));
    Assertions.assertArrayEquals(new List[]{expected}, new List[]{actual});
  }
}
