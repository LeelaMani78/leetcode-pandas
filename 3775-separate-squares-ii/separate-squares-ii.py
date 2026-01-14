class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # Treat squares as axis-aligned rectangles: [x, x+l) × [y, y+l)
        events = []  # (y, type(+1 add / -1 remove), x1, x2)
        xs = []
        for x, y, l in squares:
            x1, x2 = x, x + l
            y1, y2 = y, y + l
            events.append((y1, 1, x1, x2))
            events.append((y2, -1, x1, x2))
            xs.append(x1)
            xs.append(x2)

        if not events:
            return 0.0

        events.sort()
        xs = sorted(set(xs))

        # If only one unique x, union length is always 0
        if len(xs) <= 1:
            return float(events[0][0])

        # Segment tree over x-intervals between consecutive xs points
        seg_n = len(xs) - 1  # number of elementary segments
        cover = [0] * (4 * seg_n)
        length = [0] * (4 * seg_n)

        def push_up(node: int, l: int, r: int) -> None:
            if cover[node] > 0:
                length[node] = xs[r + 1] - xs[l]
            elif l == r:
                length[node] = 0
            else:
                length[node] = length[node * 2] + length[node * 2 + 1]

        def update(node: int, l: int, r: int, ql: int, qr: int, delta: int) -> None:
            if ql <= l and r <= qr:
                cover[node] += delta
                push_up(node, l, r)
                return
            mid = (l + r) // 2
            if ql <= mid:
                update(node * 2, l, mid, ql, qr, delta)
            if qr > mid:
                update(node * 2 + 1, mid + 1, r, ql, qr, delta)
            push_up(node, l, r)

        def x_index(val: int) -> int:
            # binary search in xs
            lo, hi = 0, len(xs) - 1
            while lo < hi:
                mid = (lo + hi) // 2
                if xs[mid] < val:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        # Pass 1: total union area
        total_area = 0
        i = 0
        prev_y = events[0][0]

        while i < len(events):
            y = events[i][0]
            dy = y - prev_y
            if dy:
                total_area += length[1] * dy
            # apply all events at this y
            while i < len(events) and events[i][0] == y:
                _, typ, x1, x2 = events[i]
                l_idx = x_index(x1)
                r_idx = x_index(x2) - 1
                if l_idx <= r_idx:
                    update(1, 0, seg_n - 1, l_idx, r_idx, typ)
                i += 1
            prev_y = y

        half = total_area / 2.0

        # Pass 2: find minimal y where area below == half
        # Reset segment tree
        cover = [0] * (4 * seg_n)
        length = [0] * (4 * seg_n)

        def push_up2(node: int, l: int, r: int) -> None:
            if cover[node] > 0:
                length[node] = xs[r + 1] - xs[l]
            elif l == r:
                length[node] = 0
            else:
                length[node] = length[node * 2] + length[node * 2 + 1]

        def update2(node: int, l: int, r: int, ql: int, qr: int, delta: int) -> None:
            if ql <= l and r <= qr:
                cover[node] += delta
                push_up2(node, l, r)
                return
            mid = (l + r) // 2
            if ql <= mid:
                update2(node * 2, l, mid, ql, qr, delta)
            if qr > mid:
                update2(node * 2 + 1, mid + 1, r, ql, qr, delta)
            push_up2(node, l, r)

        i = 0
        prev_y = events[0][0]
        area_below = 0.0

        while i < len(events):
            y = events[i][0]
            dy = y - prev_y
            if dy:
                slab_area = length[1] * dy
                if area_below + slab_area >= half:
                    # answer inside this slab
                    if length[1] == 0:
                        return float(prev_y)  # should not happen for crossing, but safe
                    return float(prev_y + (half - area_below) / length[1])
                area_below += slab_area

            # apply all events at this y
            while i < len(events) and events[i][0] == y:
                _, typ, x1, x2 = events[i]
                l_idx = x_index(x1)
                r_idx = x_index(x2) - 1
                if l_idx <= r_idx:
                    update2(1, 0, seg_n - 1, l_idx, r_idx, typ)
                i += 1

            # If we hit exactly half at an event boundary, minimal y is this boundary
            if abs(area_below - half) <= 1e-12:
                return float(y)

            prev_y = y

        # Fallback (should not be reached normally)
        return float(prev_y)

        