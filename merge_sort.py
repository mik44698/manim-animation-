

from manim import *



# ==========================================

# INPUT PARAMETER

# ==========================================



# Render 1: Primary input

ARRAY = [38, 27, 43, 3, 9, 82, 10]



# Render 2: Change the line above to:

# ARRAY = [5, 5, 5, 5, 5, 5, 5]





class MergeSort(Scene):



    def construct(self):

        if not ARRAY:

            raise ValueError("ARRAY must contain at least one number.")



        self.is_equal_case = (

            len(ARRAY) > 1

            and all(value == ARRAY[0] for value in ARRAY)

        )



        self.title = Text("Merge Sort", font_size=40)

        self.title.to_edge(UP)



        self.play(Write(self.title))

        self.wait(1)



        if self.is_equal_case:

            self.show_short_edge_case()

        else:

            self.show_introduction()

            self.show_splitting()

            self.show_merging()

            self.show_conclusion()



    # ==========================================

    # CREATE ARRAY BOXES

    # ==========================================



    def create_array(self, numbers, scale=1, color=WHITE):

        boxes = VGroup()



        for number in numbers:

            square = Square(

                side_length=0.8,

                color=color

            )



            label = Text(

                str(number),

                font_size=28

            )

            label.move_to(square.get_center())



            boxes.add(VGroup(square, label))



        boxes.arrange(RIGHT, buff=0)

        boxes.scale(scale)



        return boxes



    # ==========================================

    # INTRODUCTION

    # ==========================================



    def show_introduction(self):

        heading = Text(

            "Divide and Conquer Algorithm",

            font_size=28

        )

        heading.move_to(UP * 1.5)



        description = Text(

            "Split the array, sort each half, then merge",

            font_size=23

        )

        description.next_to(heading, DOWN, buff=0.5)



        original = self.create_array(ARRAY, 0.9)

        original.move_to(DOWN * 0.6)



        self.play(Write(heading))

        self.play(Write(description))

        self.play(FadeIn(original))

        self.wait(3)



        self.play(

            FadeOut(heading),

            FadeOut(description),

            FadeOut(original)

        )



    # ==========================================

    # BUILD RECURSION TREE

    # ==========================================



    def build_tree(self, values, depth=0):

        node = {

            "values": list(values),

            "depth": depth,

            "left": None,

            "right": None

        }



        if len(values) > 1:

            middle = len(values) // 2



            node["left"] = self.build_tree(

                values[:middle],

                depth + 1

            )



            node["right"] = self.build_tree(

                values[middle:],

                depth + 1

            )



        return node



    # ==========================================

    # PHASE 1: RECURSIVE SPLITTING

    # ==========================================



    def show_splitting(self):

        heading = Text(

            "Phase 1: Recursive Splitting",

            font_size=28

        )

        heading.move_to(UP * 2.6)



        self.play(Write(heading))



        root = self.build_tree(ARRAY)



        def maximum_depth(node):

            if node["left"] is None:

                return node["depth"]



            return max(

                maximum_depth(node["left"]),

                maximum_depth(node["right"])

            )



        max_depth = maximum_depth(root)



        leaves = []



        def collect_leaves(node):

            if node["left"] is None:

                leaves.append(node)

            else:

                collect_leaves(node["left"])

                collect_leaves(node["right"])



        collect_leaves(root)



        if len(leaves) == 1:

            leaf_positions = [0]

        else:

            spacing = min(

                1.35,

                10.0 / (len(leaves) - 1)

            )



            start = -spacing * (len(leaves) - 1) / 2



            leaf_positions = [

                start + i * spacing

                for i in range(len(leaves))

            ]



        for leaf, x in zip(leaves, leaf_positions):

            leaf["x"] = x



        def assign_positions(node):

            if node["left"] is not None:

                assign_positions(node["left"])

                assign_positions(node["right"])



                node["x"] = (

                    node["left"]["x"]

                    + node["right"]["x"]

                ) / 2



        assign_positions(root)



        levels = max_depth + 1

        top_y = 1.45

        bottom_y = -2.75



        if levels == 1:

            vertical_step = 0

        else:

            vertical_step = (

                top_y - bottom_y

            ) / (levels - 1)



        all_objects = VGroup()



        def draw_node(node, parent=None):

            depth = node["depth"]

            y = top_y - depth * vertical_step



            numbers = self.create_array(

                node["values"],

                scale=min(

                    0.7,

                    2.2 / max(1, len(node["values"]))

                )

            )



            numbers.move_to([node["x"], y, 0])



            if parent is None:

                self.play(FadeIn(numbers))

            else:

                self.play(

                    TransformFromCopy(parent, numbers),

                    run_time=0.55

                )



            all_objects.add(numbers)



            if node["left"] is None:

                self.play(

                    *[

                        cell[0].animate.set_color(GREEN)

                        for cell in numbers

                    ],

                    run_time=0.3

                )

                return



            draw_node(node["left"], numbers)

            draw_node(node["right"], numbers)



        draw_node(root)



        base_text = Text(

            "Green boxes: Base cases (one element)",

            font_size=22,

            color=GREEN

        )

        base_text.move_to(DOWN * 3.35)



        self.play(Write(base_text))

        self.wait(3)



        self.play(

            FadeOut(all_objects),

            FadeOut(base_text),

            FadeOut(heading)

        )



    # ==========================================

    # CALCULATE MERGE SORT

    # ==========================================



    def calculate_merges(self, values):

        if len(values) <= 1:

            return list(values), []



        middle = len(values) // 2



        left_sorted, left_steps = self.calculate_merges(

            values[:middle]

        )



        right_sorted, right_steps = self.calculate_merges(

            values[middle:]

        )



        merged = []

        i = 0

        j = 0



        while i < len(left_sorted) and j < len(right_sorted):

            if left_sorted[i] <= right_sorted[j]:

                merged.append(left_sorted[i])

                i += 1

            else:

                merged.append(right_sorted[j])

                j += 1



        merged.extend(left_sorted[i:])

        merged.extend(right_sorted[j:])



        step = (

            left_sorted,

            right_sorted,

            merged

        )



        return merged, left_steps + right_steps + [step]



    # ==========================================

    # PHASE 2: MERGING

    # ==========================================



    def show_merging(self):

        heading = Text(

            "Phase 2: Merge Sorted Groups",

            font_size=28

        )

        heading.move_to(UP * 2.5)



        self.play(Write(heading))



        sorted_array, steps = self.calculate_merges(ARRAY)



        for index, step in enumerate(steps):

            left_values, right_values, result = step



            self.animate_merge(

                left_values,

                right_values,

                final=(index == len(steps) - 1)

            )



        if not steps:

            single = self.create_array(sorted_array, 0.85)



            self.play(FadeIn(single))

            self.wait(2)

            self.play(FadeOut(single))



        self.play(FadeOut(heading))



    # ==========================================

    # ANIMATE EACH MERGE

    # ==========================================



    def animate_merge(

        self,

        left_values,

        right_values,

        final=False

    ):

        label = Text(

            "Final Merge"

            if final

            else "Compare and select the smaller value",

            font_size=23

        )

        label.move_to(UP * 1.7)



        left = self.create_array(left_values, 0.8)

        right = self.create_array(right_values, 0.8)



        left.move_to(LEFT * 2.7 + UP * 0.5)

        right.move_to(RIGHT * 2.7 + UP * 0.5)



        self.play(

            Write(label),

            FadeIn(left),

            FadeIn(right),

            run_time=1

        )



        total = len(left_values) + len(right_values)

        slots = VGroup()



        for _ in range(total):

            slots.add(

                Square(side_length=0.65, color=GRAY)

            )



        slots.arrange(RIGHT, buff=0.08)

        slots.move_to(DOWN * 1.5)



        self.play(Create(slots), run_time=0.7)



        i = 0

        j = 0

        result_values = []

        placed = VGroup()



        while i < len(left_values) or j < len(right_values):

            comparing = (

                i < len(left_values)

                and j < len(right_values)

            )



            if comparing:

                self.play(

                    left[i][0].animate.set_color(YELLOW),

                    right[j][0].animate.set_color(YELLOW),

                    run_time=0.35

                )



                comparison = Text(

                    f"Compare {left_values[i]} and {right_values[j]}",

                    font_size=22

                )

                comparison.move_to(DOWN * 0.5)



                self.play(

                    Write(comparison),

                    run_time=0.4

                )



            if j >= len(right_values) or (

                i < len(left_values)

                and left_values[i] <= right_values[j]

            ):

                chosen = left_values[i]

                source = left[i]

                i += 1

            else:

                chosen = right_values[j]

                source = right[j]

                j += 1



            result_values.append(chosen)



            new_cell = self.create_array([chosen], 0.8)

            new_cell.move_to(

                slots[len(result_values) - 1].get_center()

            )

            new_cell[0][0].set_color(GREEN)



            self.play(

                TransformFromCopy(source, new_cell),

                run_time=0.55

            )



            placed.add(new_cell)



            if comparing:

                self.play(

                    FadeOut(comparison),

                    run_time=0.2

                )



            self.wait(0.2)



        result_label = Text(

            "Merged: " + str(result_values),

            font_size=21,

            color=GREEN

        )

        result_label.move_to(DOWN * 2.6)



        self.play(Write(result_label))

        self.wait(3 if final else 1.5)



        self.play(

            FadeOut(label),

            FadeOut(left),

            FadeOut(right),

            FadeOut(slots),

            FadeOut(placed),

            FadeOut(result_label)

        )



    # ==========================================

    # RENDER 2: SHORT EDGE-CASE DEMONSTRATION

    # ==========================================



    def show_short_edge_case(self):
        # Render 2 uses the same complete splitting and merging
        # animations as Render 1, rather than an abbreviated example.
        heading = Text(
            "Edge Case: All Equal Values",
            font_size=28
        ).move_to(UP * 2.3)

        original = self.create_array(ARRAY, 0.85)
        original.move_to(UP * 0.8)

        self.play(Write(heading))
        self.play(FadeIn(original))
        self.wait(1)
        self.play(FadeOut(original), FadeOut(heading))

        # Every recursive split, down to one-element base cases.
        self.show_splitting()

        # Every merge and comparison, calculated from ARRAY.
        self.show_merging()

        value = ARRAY[0]
        stability = Text(
            "Equal values keep their original relative order",
            font_size=22,
            color=GREEN
        ).move_to(UP * 0.6)

        labels = VGroup(
            Text(f"{value}A", font_size=30, color=BLUE),
            Text(f"{value}B", font_size=30, color=ORANGE)
        )
        labels.arrange(RIGHT, buff=1)
        labels.move_to(DOWN * 0.4)

        self.play(Write(stability), FadeIn(labels))
        self.wait(2)
        self.play(FadeOut(stability), FadeOut(labels))

        final = Text(
            "All equal values remain correctly sorted!",
            font_size=25,
            color=GREEN
        )
        self.play(Write(final))
        self.wait(2)

    # ==========================================



    def show_conclusion(self):

        heading = Text(

            "Merge Sort Summary",

            font_size=30

        )

        heading.move_to(UP * 2)



        lines = VGroup(

            Text(

                "1. Divide the array recursively",

                font_size=24

            ),

            Text(

                "2. Stop at the base case",

                font_size=24

            ),

            Text(

                "3. Merge in sorted order",

                font_size=24

            ),

            Text(

                "Time Complexity: O(n log n)",

                font_size=24,

                color=GREEN

            )

        )



        lines.arrange(DOWN, buff=0.35)

        lines.move_to(DOWN * 0.2)



        self.play(Write(heading))



        self.play(

            LaggedStart(

                *[Write(line) for line in lines],

                lag_ratio=0.6

            ),

            run_time=5

        )



        self.wait(4)



        self.play(

            FadeOut(heading),

            FadeOut(lines)

        )



        ending = Text(

            "Merge Sort Complete!",

            font_size=34,

            color=GREEN

        )

        ending.move_to(ORIGIN)



        self.play(Write(ending))

        self.wait(3)

