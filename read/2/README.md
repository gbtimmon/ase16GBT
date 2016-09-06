
1. Paper
	Cuixiong Hu and Iulian Neamtiu. 2011. Automating GUI testing for Android applications. In Proceedings of the 6th International Workshop on Automation of Software Test (AST '11). ACM, New York, NY, USA, 77-83. 

2. Keywords
	1. Test automation
The process of running testing suites without the need for manual intervention. This can greatly speed up the testing process and allows for the periodic checking for errors.
	2. GUI Testing
The process of testing the user interface for an application. These tests typically require parsing through menus of the application and frequently require manual testing. 
	3. Test Case Generation
Using a tool or process to create uses cases for an application to verify it is functioning and validating that it is functioning as expected. Examples of frameworks for generating test cases is the JUnit framework for Java applications and Monkey for Android application GUIs. 
	4. Empirical Bug Studies
A study was performed in this paper on ten codebases for popular android applications in order to search for the most common bug occurrences throughout. Code had to have a long lifetime, detailed bug history and source code available. 
3. Brief Notes:
	1. Study Instrument - Empirical Bug Study: for the paper the authors performed a study on the most commonly occurring bugs throughout ten popular Android applications. The criteria for an application was a long code lifetime, detailed bug history and the availability of source code for the project. Bugs were split into various categories for each application and was summed up.
	2. Related Work -  Previous verification of mobile applications was centered around security testing. The Saint tool evaluated the permissions of the application in the mobile environment and TaintDroid monitored to the flow of application data (potentially sensitive data) for leaks. Previous GUI testing frameworks, such as GUITAR, could not be applied to the Android mobile environment due system architecture of the intended target, Java desktop applications.
	3. Future Work - The paper notes that a lot of bugs fell into the other category so they wanted to further define the categories in order to analyze the bugs better. The authors also hope to add their model to Static analysis tools to catch I/O bugs at compile time rather than during automated testing. 
	4. Baseline Results - There was a table provided that outlines the known bugs found, along with new bugs found in each category. ![Baseline Image](https://github.com/gbtimmon/ase16GBT/blob/master/read/2/baseline_results.png "Baseline Results")
	5. Informative Visualizations - The authors provided a simplified view of their approach, showing inputs and outputs. They also outlined the state machine of android activity to better define an Android activity. ![Informative Visual 1](https://github.com/gbtimmon/ase16GBT/raw/master/read/2/informative_visual_1.png "Informative Visual 1") ![Informative Visual 2](https://github.com/gbtimmon/ase16GBT/blob/master/read/2/informative_visual_2.png "Informative Visual 2")  
4. Improvements
	1. The authors should have realized much sooner that only 4-5 categories would not be sufficient to divide bugs accurately. I think they should have created more categories out of the gate. 
	2. The authors use Monkey event generator, which is provided by the Android SDK to generate events for tests. Perhaps the authors could have discussed the limitations of only using one event generator or better classify the types of events that can be generated with this tool.
	3. The authors could find or collect user data for applications and use that user data to find commonly used usage paths for the tool to study. That way you could also represent the user-base in addition to random selection.
5. Relates to Reading 1
	1. The original reading used the classifications of bugs outlined in this paper (Activity, Event) to classify bugs found using the tool they developed.
	2. The original reading and this paper used the Monkey tool developed with the Android SDK to generate event sequences.
