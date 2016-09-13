1. Paper
	Zhifang Liu, Xiaopeng Gao and Xiang Long. 2010. Adaptive Random Testing of Mobile Application. In Proceedings of the 2nd International Conference on Computer Engineering and Technology (ICCET ’10), IEEE Computer Society, Washington, DC, USA, 2, 297-301.

2. Keywords
	1. Pervasive Computing - Integrating computing into everyday objects to compute, gather, and communicate information more easily and widely. This is also referred to as ubiquitous programming.
	2. Mobile Application - a type of software that is designed to be run on a mobile device, such as a phone or tablet. This type of software usually provides additional computing and functionality, similar to what can be found in a desktop computer. This software is also referred to as apps.
	3. Sequence Distance - the distance between two ordered event-typed lists. This measures the distance but does not consider the event’s value.
	4. Levenshtein Distance - Uses sequence distances to measure the minimum edit operation needed to transform a string to another string. This value is measured to generate random test cases.
3. Brief Notes
	1. Related Work - Memon and team used event-flow graphs and systematic test case generation to test GUI applications. This method is limited as it requires source code to perform static and dynamic analysis to understand the GUI. Ciupa and team used the algorithm proposed in this paper to improve fault detection rates by using object distances.
	2. Future Work - The work detailed in this paper could be applied to other embedded event-driven software systems, such as interactive TV and video game consoles. The team also intends combine Adaptive Random Testing with Model-based testing to more evenly test the application.
	3. Statistical Tests - The authors used formulas to analyze the effectiveness of their ART algorithm and compare it to random baseline tests. They used two metrics to test: F-measure (the number of tests cases required to detect the first failure) and the time used to find the first fault. 
	4. Motivational Statements - The authors recognized that mobile application testing is slow and could be automated to improve efficiency and accuracy. Another problem with current methods of testing applications is that the test scripts are dependent upon the user who writes them, particularly who well they understand the functions of the application, and often results in a lot of variability and inconsistency.
4. Improvements
	1. The authors provided a pseudo script of their proposed ART algorithm. I would have liked to have seen a scriptlet included as well.
	2. The authors vaguely suggested that future work should combine the Adaptive Random Testing algorithm with Model based testing, but it really doesn’t explain the potential benefits of studying this combination. This sounds like it could be a limitation of their current work, which should be identified.
	3. The authors compared ART to just randomly generated test cases, but it doesn’t really detail the method of randomly generating test cases or how it specifically differs from adaptive random test case generation.
5. Relates to Reading 3
	1. Reading 3 discussed the challenges in mobile application testing. This paper addressed the challenges it was trying to solve. It was trying to reduce the time it takes to generate good test cases and still providing good, consistent test coverage.
	2. Reading 3 addressed a wider breadth of challenges and considerations in testing mobile applications, like security and portability, without providing any suggested solutions. This reading focuses on a small section of challenges and provides a solution.
	3. The solution provided in the paper was the primary method of generating test cases in the first reading. The first reading expanded upon the Adaptive Random Testing algorithm and provided a tool using this algorithm to generate automated test cases. 
