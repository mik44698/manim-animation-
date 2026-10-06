from manim import *

ARRAY = [38, 27, 43, 3, 9, 82, 10]


class MergeSort(Scene):
    def construct(self):
        # Title
        title = Text("Merge Sort", font_size=40)
        title.to_edge(UP)
        self.play(Write(title))

        explanation = Text(
            "Divide the array into smaller pieces",
            font_size=24
        )
        explanation.next_to(title, DOWN)

        self.play(Write(explanation))

        # Original array
        original = self.create_array(ARRAY)
        original.move_to(UP * 1)

        depth_zero = Text("Depth 0", font_size=20)
        depth_zero.next_to(original, LEFT)

        self.play(Create(original), Write(depth_zero))
        self.wait(2)

        # First split
        middle = len(ARRAY) // 2

        left_values = ARRAY[:middle]
        right_values = ARRAY[middle:]

        left = self.create_array(left_values, 0.7)
        right = self.create_array(right_values, 0.7)

        left.move_to(LEFT * 2.5 + DOWN * 0.7)
        right.move_to(RIGHT * 2.3 + DOWN * 0.7)

        self.play(
            TransformFromCopy(original, left),
            TransformFromCopy(original, right)
        )

        depth_one = Text("Depth 1", font_size=20)
        depth_one.to_edge(LEFT)
        depth_one.set_y(-0.7)

        self.play(Write(depth_one))
        self.wait(2)

        # Second split
        left_middle = len(left_values) // 2
        right_middle = len(right_values) // 2

        group1_values = left_values[:left_middle]
        group2_values = left_values[left_middle:]

        group3_values = right_values[:right_middle]
        group4_values = right_values[right_middle:]

        group1 = self.create_array(group1_values, 0.55)
        group2 = self.create_array(group2_values, 0.55)
        group3 = self.create_array(group3_values, 0.55)
        group4 = self.create_array(group4_values, 0.55)

        group1.move_to(LEFT * 4.5 + DOWN * 2.3)
        group2.move_to(LEFT * 2 + DOWN * 2.3)
        group3.move_to(RIGHT * 1.5 + DOWN * 2.3)
        group4.move_to(RIGHT * 4 + DOWN * 2.3)

        self.play(
            TransformFromCopy(left, group1),
            TransformFromCopy(left, group2),
            TransformFromCopy(right, group3),
            TransformFromCopy(right, group4)
        )

        depth_two = Text("Depth 2", font_size=20)
        depth_two.to_edge(LEFT)
        depth_two.set_y(-2.3)

        self.play(Write(depth_two))

        base_text = Text(
            "Keep splitting until each group has one element",
            font_size=22
        )
        base_text.to_edge(DOWN)

        self.play(Write(base_text))
        self.wait(3)


    def create_array(self, numbers, scale=1):
        boxes = VGroup()

        for number in numbers:
            square = Square(side_length=0.8)
            label = Text(str(number), font_size=28)
            label.move_to(square.get_center())

            cell = VGroup(square, label)
            boxes.add(cell)

        boxes.arrange(RIGHT, buff=0)
        boxes.scale(scale)

        return boxes