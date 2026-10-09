# ── locked · read-only boilerplate ──
# imports: manim, numpy (np), pandas (pd), scipy, sympy + stdlib listed below
# anything else is blocked — bespoke needs → contact your instructor
from manim import *
import numpy as np
import pandas as pd
import scipy
import sympy
import math, random, statistics, itertools, functools, collections
import datetime, decimal, fractions, re, string

class MergeSort(Scene):
    def construct(self):
        ARRAY = [38, 27, 43, 3, 9, 82, 10]
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



    # my code
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

        group1.shift(UP*4)
        group2.shift(UP*4)
        group3.shift(UP*4)
        group4.shift(UP*4)

        self.play(FadeIn(group1, group2, group3, group4))


        #Text
        ex1 = Text("Single arrays are already sorted", font_size=20)
        ex1.to_edge(UP)
        self.play(Write(ex1))

        #Split into single arrays

        group2middle = len(group2) // 2
        group3middle = len(group3) // 2
        group4middle = len(group4) // 2


        g2firstvalue = group2[:group2middle]
        g2secvalue = group2[group2middle:]
        g3firstvalue = group3[:group3middle]
        g3secvalue = group3[group3middle:]
        g4firstvalue = group4[:group4middle]
        g4secvalue = group4[group4middle:]

        self.play(
            g2firstvalue.animate.shift(LEFT),
            g3firstvalue.animate.shift(LEFT),
            g4firstvalue.animate.shift(LEFT),
        )
        self.wait(2)
        self.play(FadeOut(ex1))



        #compare and merge scene

        #text
        ex2 = Text("Array values are compared when merged, and the smaller value is pushed to the front", font_size=20)
        ex3 = Text("Single arrays are merged into smaller arrays first", font_size=20)
        ex4 = Text("The two sorted halves are merged into a fully sorted array", font_size=20)

    
        ex2.to_edge(UP)
        ex3.to_edge(UP)
        ex4.to_edge(UP)

    
        self.play(Write(ex2))

        #merging

        one = [ARRAY[0]]
        two = [ARRAY[1]]
        three = [ARRAY[2]]
        four = [ARRAY[3]]
        five = [ARRAY[4]]
        six = [ARRAY[5]]
        seven = [ARRAY[6]]



        firstmerge = self.merge(one, two)
        secondmerge = self.merge(firstmerge, three)
    
        firstarray = self.create_array(secondmerge, 0.55)

        thirdmerge = self.merge(four, five)
        fourthmerge = self.merge(six, seven)
    
        secondarray = self.create_array(thirdmerge, 0.55)
        thirdarray = self.create_array(fourthmerge, 0.55)

        fifthmerge = self.merge(thirdmerge, fourthmerge)
        sixthmerge = self.merge(secondmerge, fifthmerge)

        fourtharray = self.create_array(fifthmerge, 0.55)

        fiftharray = self.create_array(sixthmerge, 0.90)



        firstarray.move_to(DOWN*0.5 + LEFT*3)
        secondarray.move_to(DOWN*0.5)
        thirdarray.move_to(DOWN*0.5 + RIGHT*3)
        fourtharray.move_to(DOWN*1.5 + RIGHT*1.5)
        fiftharray.move_to(DOWN*3 + LEFT*0.5)

    
        self.play(Create(firstarray, run_time = 2))
        self.wait()
    
        self.play(FadeOut(ex2))
        self.play(Write(ex3))
        self.wait()

    
        self.play(Create(secondarray))
        self.wait()
        self.play(Create(thirdarray))
        self.wait()

    
        self.play(Create(fourtharray, run_time=2))
        self.wait()

        self.play(FadeOut(ex3))
        self.wait()
        self.play(Write(ex4))

    
        self.play(Create(fiftharray, run_time=3))
        self.wait()





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

    #my code

    def merge(self, left, right):
        NEWARRAY=[]
        l = r = 0

        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                NEWARRAY.append(left[l])
                l += 1
            else:
                NEWARRAY.append(right[r])
                r += 1
        NEWARRAY.extend(left[l:])
        NEWARRAY.extend(right[r:])
        return NEWARRAY
