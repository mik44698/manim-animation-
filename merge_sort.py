"""A narrated, input-driven merge sort animation.

Render once with ARRAY, then replace ARRAY with EDGE_CASE_ARRAY and render
again to demonstrate the duplicate-value edge case using the same scene.
The scene shows recursive splitting, the one-value base case, stable merges,
and the final sorted result.
"""

from manim import *

ARRAY = [38, 27, 43, 3, 9, 82, 10]
EDGE_CASE_ARRAY = [38, 27, 43, 27, 9, 82, 10]

SPLIT_PAUSE = 2.8
COMPARE_PAUSE = 3.0
INSERT_PAUSE = 0.6


class MergeSort(Scene):
    def construct(self):
        if len(ARRAY) < 2:
            raise ValueError("ARRAY must contain at least two values.")

        self.cell_size = min(
            0.82,
            (12.5 - (len(ARRAY) - 1) * 0.12) / len(ARRAY),
        )
        self.label_size = max(16, int(self.cell_size * 34))
        self.active_panel = VGroup()

        title = Text("Merge Sort: Split, Then Merge", font_size=36)
        title.to_edge(UP, buff=0.25)
        subtitle = Text(
            "Each half is sorted before the two halves are merged.",
            font_size=21,
        )
        subtitle.next_to(title, DOWN, buff=0.12)
        self.play(Write(title), run_time=0.8)
        self.play(Write(subtitle), run_time=0.7)

        input_label = Text("Input", font_size=24, color=BLUE)
        input_row = self.create_array(ARRAY)
        input_label.next_to(input_row, UP, buff=0.2)
        input_row.move_to(ORIGIN)
        input_label.next_to(input_row, UP, buff=0.2)
        self.show_panel(VGroup(input_label, input_row))
        self.wait(1.4)

        sorted_values = self.sort_values(ARRAY[:], 0, "root")
        self.show_final_result(ARRAY, sorted_values)

    def sort_values(self, values: list[int], depth: int, path: str) -> list[int]:
        if len(values) == 1:
            phase = Text(f"Base case | depth {depth}", font_size=29, color=GREEN)
            phase.move_to(UP * 1.65)
            path_label = Text(f"Current group: {path}", font_size=21)
            path_label.next_to(phase, DOWN, buff=0.15)
            row = self.create_array(values).move_to(UP * 0.15)
            explanation = Text(
                "One value is already sorted, so recursion stops here.",
                font_size=21,
            )
            explanation.move_to(DOWN * 1.05)
            self.show_panel(VGroup(phase, path_label, row, explanation))
            self.wait(SPLIT_PAUSE)
            return values

        middle = len(values) // 2
        left_values = values[:middle]
        right_values = values[middle:]

        phase = Text(f"Split | depth {depth}", font_size=29, color=BLUE)
        phase.move_to(UP * 1.65)
        path_label = Text(f"Current group: {path}", font_size=21)
        path_label.next_to(phase, DOWN, buff=0.15)

        parent_row = self.create_array(values).move_to(UP * 0.65)
        left_row = self.create_array(left_values)
        right_row = self.create_array(right_values)
        children = VGroup(left_row, right_row).arrange(RIGHT, buff=0.8)
        children.move_to(DOWN * 1.05)

        left_label = Text("Left half", font_size=19, color=YELLOW)
        left_label.next_to(left_row, UP, buff=0.12)
        right_label = Text("Right half", font_size=19, color=YELLOW)
        right_label.next_to(right_row, UP, buff=0.12)
        explanation = Text(
            f"Divide {len(values)} values into groups of "
            f"{len(left_values)} and {len(right_values)}.",
            font_size=21,
        )
        explanation.move_to(DOWN * 2.35)

        self.show_panel(
            VGroup(
                phase,
                path_label,
                parent_row,
                children,
                left_label,
                right_label,
                explanation,
            )
        )
        self.wait(SPLIT_PAUSE)

        sorted_left = self.sort_values(left_values, depth + 1, f"{path}/L")
        sorted_right = self.sort_values(right_values, depth + 1, f"{path}/R")
        return self.animate_merge(sorted_left, sorted_right, depth, path)

    def animate_merge(
        self, left: list[int], right: list[int], depth: int, path: str
    ) -> list[int]:
        phase = Text(f"Merge | depth {depth}", font_size=29, color=PURPLE)
        phase.move_to(UP * 2.05)
        path_label = Text(f"Returning to: {path}", font_size=21)
        path_label.next_to(phase, DOWN, buff=0.15)

        left_row = self.create_array(left).move_to(UP * 0.45)
        right_row = self.create_array(right).move_to(DOWN * 0.4)
        left_label = Text("Sorted left half", font_size=19, color=YELLOW)
        left_label.next_to(left_row, UP, buff=0.12)
        right_label = Text("Sorted right half", font_size=19, color=YELLOW)
        right_label.next_to(right_row, UP, buff=0.12)

        output_row = self.create_empty_array(len(left) + len(right))
        output_row.move_to(DOWN * 1.55)
        output_label = Text("Merged output", font_size=19, color=GREEN)
        output_label.next_to(output_row, UP, buff=0.12)
        message = Text(
            "Compare the first unmerged value in each half.",
            font_size=21,
        )
        message.move_to(DOWN * 2.65)

        self.show_panel(
            VGroup(
                phase,
                path_label,
                left_label,
                left_row,
                right_label,
                right_row,
                output_label,
                output_row,
                message,
            )
        )

        merged = []
        left_index = 0
        right_index = 0
        output_index = 0

        while left_index < len(left) and right_index < len(right):
            left_value = left[left_index]
            right_value = right[right_index]
            left_box = left_row[left_index][0]
            right_box = right_row[right_index][0]

            self.play(
                left_box.animate.set_stroke(YELLOW, width=5),
                right_box.animate.set_stroke(YELLOW, width=5),
                run_time=0.3,
            )

            if left_value <= right_value:
                message_text = (
                    f"{left_value} <= {right_value}: take {left_value} "
                    "from the left."
                )
                next_value = left_value
                left_index += 1
            else:
                message_text = (
                    f"{left_value} > {right_value}: take {right_value} "
                    "from the right."
                )
                next_value = right_value
                right_index += 1

            next_message = Text(message_text, font_size=21)
            next_message.move_to(message)
            self.play(Transform(message, next_message), run_time=0.4)
            self.wait(COMPARE_PAUSE)

            merged.append(next_value)
            self.add_output_value(output_row, output_index, next_value)
            output_index += 1

            self.play(
                left_box.animate.set_stroke(WHITE, width=2),
                right_box.animate.set_stroke(WHITE, width=2),
                run_time=0.3,
            )
            self.wait(INSERT_PAUSE)

        if left_index < len(left):
            tail = left[left_index:]
            tail_message = Text(
                "Right half is exhausted; append the remaining left values.",
                font_size=21,
            )
            tail_message.move_to(message)
            self.play(Transform(message, tail_message), run_time=0.4)
            for value in tail:
                merged.append(value)
                self.add_output_value(output_row, output_index, value)
                output_index += 1
                self.wait(INSERT_PAUSE)
        elif right_index < len(right):
            tail = right[right_index:]
            tail_message = Text(
                "Left half is exhausted; append the remaining right values.",
                font_size=21,
            )
            tail_message.move_to(message)
            self.play(Transform(message, tail_message), run_time=0.4)
            for value in tail:
                merged.append(value)
                self.add_output_value(output_row, output_index, value)
                output_index += 1
                self.wait(INSERT_PAUSE)

        return merged

    def show_final_result(self, original: list[int], sorted_values: list[int]):
        heading = Text("Complete: the input is now sorted", font_size=30, color=GREEN)
        heading.move_to(UP * 1.75)

        original_label = Text("Original input", font_size=21, color=BLUE)
        original_row = self.create_array(original).move_to(UP * 0.7)
        original_label.next_to(original_row, UP, buff=0.15)

        sorted_label = Text("Sorted output", font_size=21, color=GREEN)
        sorted_row = self.create_array(sorted_values).move_to(DOWN * 0.65)
        sorted_label.next_to(sorted_row, UP, buff=0.15)

        explanation = Text(
            "At every merge, the smallest available front value is chosen.",
            font_size=21,
        )
        explanation.move_to(DOWN * 1.8)
        self.show_panel(
            VGroup(
                heading,
                original_label,
                original_row,
                sorted_label,
                sorted_row,
                explanation,
            )
        )
        self.wait(3)

    def show_panel(self, panel: VGroup):
        if self.active_panel.submobjects:
            self.play(
                FadeOut(self.active_panel),
                FadeIn(panel),
                run_time=0.5,
            )
        else:
            self.play(FadeIn(panel), run_time=0.5)
        self.active_panel = panel

    def create_array(self, values: list[int]) -> VGroup:
        cells = VGroup()
        for value in values:
            square = Square(side_length=self.cell_size)
            label = Text(str(value), font_size=self.label_size)
            label.move_to(square.get_center())
            cells.add(VGroup(square, label))
        cells.arrange(RIGHT, buff=0.12)
        return cells

    def create_empty_array(self, length: int) -> VGroup:
        cells = VGroup()
        for _ in range(length):
            cells.add(Square(side_length=self.cell_size))
        cells.arrange(RIGHT, buff=0.12)
        return cells

    def add_output_value(
        self, output_row: VGroup, index: int, value: int
    ):
        label = Text(str(value), font_size=self.label_size)
        label.move_to(output_row[index].get_center())
        self.play(FadeIn(label), run_time=0.3)
        output_row[index].add(label)
