package org.psawesome;

import org.junit.jupiter.api.*;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;

import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.fail;

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
            .setTotCount(ints.length)
            .threeSum(ints);
    List<List<Integer>> expected = Arrays.asList(Arrays.asList(-1, 0, 1), Arrays.asList(-1, -1, 2));
    Assertions.assertArrayEquals(new List[]{expected}, new List[]{actual});
  }

  @Test
  @Disabled("Not implemented yet")
  void testShouldBeLowerThenCountOfAllCheck() {
    assertEquals(1, 1);
    fail("not implemented");
  }

  @Test
  @DisplayName("should be my test")
  void shouldBeMyTest() {
    Assumptions.assumeTrue(true);
    fail("Not implemented");
  }

  @ParameterizedTest(name = "{0} {0}")
  @DisplayName("Test description")
  @ValueSource(strings = {"alpha", "bravo", "clip"})
  void testDescription(String myName) {
    System.out.println("s = " + myName);
    fail("Not implemented");
  }


  @Test
  @DisplayName("test should be")
  void testShouldBe() {
    
    org.junit.jupiter.api.Assertions.fail("Not implemented");
  }
}
