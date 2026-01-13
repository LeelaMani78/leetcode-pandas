from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = 0.0
        events = []

        for sq in squares:
            y, l = sq[1], sq[2]
            total_area += l * l
            events.append((y, l, 1))          # start
            events.append((y + l, l, -1))      # ✅ FIX: y+1 -> y+l

        events.sort()

        covered_width = 0.0
        curr_area = 0.0
        half = total_area / 2.0

        prev_height = events[0][0]            # ✅ FIX: start from first event

        for height, width, delta in events:
            height_diff = height - prev_height
            if height_diff > 0 and covered_width > 0:
                area = covered_width * height_diff
                if curr_area + area >= half:
                    # ✅ FIX: correct formula
                    return prev_height + (half - curr_area) / covered_width
                curr_area += area

            covered_width += delta * width
            prev_height = height

        return prev_height
