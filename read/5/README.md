1. Paper
	Casper S Jensen, M. R. Prasad, and A. Møller. Automated testing with targeted event sequence generation. In Proceedings of the 2013 International Symposium on Software Testing and Analysis, pages 67-77.

2. Keywords
	1. Symbolic Execution - a process for evaluating a program to determine which inputs to a program will trigger program execution. This can be used to generate test data, where input data is represented by symbolic values from a set of values to generate an output.
	2. Android - an operating system created by Google for mobile devices, such as mobile phones and tablets. This open source operating system is a linux-based platform that allows developers to create applications that extend the functionality of the mobile device.
	3. Concolic Execution - a hybrid process that combines both symbolic and concrete execution to execute or test a program. With this technique, concrete execution dictates the symbolic execution, as the concrete set of paths provided from concrete execution are tested with the symbolic inputs prorvided by symbolic execution.
	4. Event Handler - a routine in a program that asynchronously handles inputs, or events, to a program. These events are often keystrokes or mouse clicks inputted to the program intended to trigger some action. 
3. Brief Notes
	1. Motivational Statements - The authors included a whole section (2. Motivating Example) that describes what they intended to research and prove. The author’s proposed algorithm works to identify anchor and connector events to achieve a specific initial state; this approach is intended to reach more complex, challenging event sequences that previous automated test frameworks do not reach. In their evaluation, the authors also listed and answered the questions they had intended to answer in this paper. 
	2. Related Work - This paper builds on the concolic testing technique, ACTEve, by searching for particular targets from a given starting point; they also abstract the concolic execution used for reasoning with UI models. This paper also builds on Ma et al.’s proposed call-chain-backward symbolic execution, by constructing event sequences backward from a narrowed search and by considering the relationships between events.
	3. Informative Visualizations - The authors included a helpful visual/generic script of their proposed algorithm that better describes how it functions. This figure is below. 
	In addition, the authors included a graph to visualize the results of the event sequence lengths captured in their generated test cases. This figure is below.

	4. Future Work - The authors predicted various sequences that their algorithm would reach, but not all were covered in the generated tests. The authors proposed that improving the algorithm, specifically the symbolic constraint solver component, then all predicted event sequences would have been reached.
4. Improvements
	1. The authors benchmarked their algorithm by measuring how many event sequences were reached out of how many were predicted. This paper does not describe how the predicted sequences were determined. This could be helpful in expanding the algorithm to reach the test cases, along with understanding how the algorithm identified more test sequences than were predicted in more than one application.
	2. A good chunk of the paper describes and expands upon the figure of their event sequence generation algorithm, however, some aspects are very detailed in the paper, but others are not very well described, such as ExtractTestCase. 
	3. The paper discusses a very good example application that motivated the generation of this algorithm, TaxCalculator, but the authors didn’t test their algorithm against this application. They could have used this application as a baseline and analyzed all event sequences found rather than just the complex ones.
5. Relates to Readings
	The AndroidRipper testing tool detailed in paper 1 is referred to in this paper as a “good starting point for automated testing,” as they prove why their algorithm is more detailed than the source logic of AndroidRipper.
Unlike with paper 1, these authors only test their tool against complex event sequences rather than trying to baseline by finding all potential test cases.
