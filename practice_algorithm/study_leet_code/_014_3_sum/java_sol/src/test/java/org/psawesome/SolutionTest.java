package org.psawesome;

import org.junit.jupiter.api.*;

import java.util.Arrays;
import java.util.List;
import java.util.Set;

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
  @DisplayName("최종 결과")
  void testFinal() {
    final int[] ints = {-1, 0, 1, 2, -1, -4};
    List<List<Integer>> actual = solution
            .threeSum(ints);
    List<List<Integer>> expected = Arrays.asList(Arrays.asList(-1, 0, 1), Arrays.asList(-1, -1, 2));
    Assertions.assertArrayEquals(new List[]{expected}, new List[]{actual});
  }

  @Test
  @DisplayName("should be duplicate array not equals true")
  void shouldBeMyTest() {
    Assertions.assertArrayEquals(new List[]{List.of(0, 1, -1)}, new List[]{List.of(-1, 0, 1)});
  }

  @Test
  @DisplayName("test should be set duplication equals true")
  void testShouldBeSetDuplicationEqualsTrue() {
    Assertions.assertArrayEquals(new Set[]{Set.of(0, 1, -1)}, new Set[]{Set.of(-1, 0, 1)});
  }

}
