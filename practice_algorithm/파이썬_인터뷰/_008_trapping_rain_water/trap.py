# https://leetcode.com/problems/trapping-rain-water

class Solution:
    def trap(self, height: [int]) -> int:
        if not height:
            return 0

        volume = 0
        left_idx, right_idx = 0, len(height) - 1
        # 양 끝으로 시작
        left_max, right_max = height[left_idx], height[right_idx]

        # 포인터가 교차되지 않은 경우
        while left_idx < right_idx:
            # 현재 가장 높은 높이와 포인터가 이동한 높이 중 큰 값으로 업데이트
            left_max, right_max = max(height[left_idx], left_max), max(height[right_idx], right_max)

            # 왼쪽 높이 <= 오른쪽 높이인 경우
            if left_max <= right_max:
                # 왼쪽을 증가시키며 최대 높이 - 현재 높이만큼 볼륨을 증가시킨다.
                volume += left_max - height[left_idx]
                left_idx += 1
            else:
                # 오른쪽을 감소시키며 볼륨 증가시킨다.
                volume += right_max - height[right_idx]
                right_idx -= 1

        return volume

    def trap_stack(self, height: [int]) -> int:
        """
        현재 높이가 이전 높이보다 높을 때, 격차만큼 볼륨을 증가시킨다.
        변곡점을 만날 때마다 스택에서 하나씩 꺼내면서 이전과의 차이만큼 물 높이를 채운다.
        """

        stack = []
        volume = 0

        for i in range(len(height)):
            # 변곡점을 만나는 경우 # 현재 높이가 이전 높이보다 낮을 때
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()

                # 기둥이 하나있을 때는 물을 담을 수 없다.
                if not stack:
                    break

                # 이전과의 차이만큼 물 높이를 추가
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]
                print(f"curr_height : {height[i]}, last_height : {height[stack[-1]]}\n" +
                      f"waters : {min(height[i], height[stack[-1]]) - height[top]}, distance : {distance}\n")

                volume += distance * waters
            stack.append(i)
        return volume
