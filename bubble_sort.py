from manim import *
SLOW_MODE = False

class BubbleSortPass(Scene):
    def construct(self):
        numbers = [5, 2, 8, 1, 4, 3]
        boxes = VGroup()

        for number in numbers:
            square = Square(side_length=1.2)
            label = Text(str(number), font_size=36)
            label.move_to(square.get_center())

            cell = VGroup(square, label)
            boxes.add(cell)

        boxes.arrange(RIGHT, buff=0.15)
        boxes.move_to(ORIGIN)

        self.play(Create(boxes), run_time=2)
        self.wait(1)
        speed = 1.5 if SLOW_MODE else 0.6

        title = Text("Bubble Sort - One Pass", font_size=36)
        title.next_to(boxes, UP, buff=1)

        self.play(Write(title), run_time=speed)


        for i in range(len(numbers) - 1):

            
            boxes[i][0].set_stroke(YELLOW, width=6)
            boxes[i + 1][0].set_stroke(YELLOW, width=6)

            comparison = Text(
                f"Compare {numbers[i]} and {numbers[i + 1]}",
                font_size=28
            )
            comparison.next_to(boxes, DOWN, buff=0.8)

            self.play(Write(comparison), run_time=speed)
            self.wait(speed)
    
            if numbers[i] > numbers[i + 1]:
                swap_text = Text("Swap!", font_size=28, color=GREEN)
                swap_text.next_to(comparison, DOWN, buff=0.3)

                self.play(Write(swap_text), run_time=speed / 2)

            
                left_position = boxes[i].get_center()
                right_position = boxes[i + 1].get_center()

                
                self.play(
                    boxes[i].animate.move_to(right_position),
                    boxes[i + 1].animate.move_to(left_position),
                    run_time=speed
                )

                
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                boxes[i], boxes[i + 1] = boxes[i + 1], boxes[i]

                self.play(FadeOut(swap_text), run_time=0.3)

        
            boxes[i][0].set_stroke(WHITE, width=2)
            boxes[i + 1][0].set_stroke(WHITE, width=2)

            self.play(FadeOut(comparison), run_time=0.3)