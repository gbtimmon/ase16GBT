1. Paper
	A. MacHiry, R. Tahiliani, and M. Naik. Dynodroid: An input generation system for android apps. Technical report, Program Analysis Group, Georgia Tech, 2012.

2. Keywords
	1. Event Driven Programming - This is a design paradigm in software engineering, where a program is executed by following the flow of events that trigger different processes.
	2. Observe-Select-Execute cycle - A life cycle principle for developing a system that uses events to trigger a new process. The Observe phase is when the application identifies (observes) the events that are relevant and necessary to the current functionality. The Select phase is where a particular event is selected. Finally, in the Execute phase, the selected event is used to trigger a process and cause the application to move to a new state with new potential events. 
	3. Broadcast Receiver - A process/method that responds to messages broadcasted by other applications or the device itself.
	4. System services - “A fixed set of processes that provide abstractions of different functionality of an Android device,” [pg 228]. In other words, these are different sets of functionality, either internal or external, that are triggered by incoming data.
3. Brief Notes
	1. Informative Visualizations - The authors included helpful diagrams of the entire process which their program flows through. 
	![Diagram](https://github.com/gbtimmon/ase16GBT/blob/master/read/6/Figure_1.png "Process Diagram")
	The authors also included their state transition to show the program moves through the execution.
	![StateMachine](https://github.com/gbtimmon/ase16GBT/blob/master/read/6/Figure_2.png "State Machine")
	2. Baseline Results and New Results - The authors included comparison graphs of their code coverage against different baselines to get a clearer picture of the new vs. the old results.
	![Results](https://github.com/gbtimmon/ase16GBT/blob/master/read/6/Figure_3.png "Results")
	3. Sampling Procedures - The authors very clearly and in a detailed manner described how they tested their program. They used consistent hardware ( Linux machines with 8GB memory and 3.0GHz processors) and consistent software version (Android’s Gingerbread) and described why. They choose the most popular software version, not necessarily the newest or most stable, as it is installed on the most devices. They sampled 50 randomly chosen open-source applications to test against by keeping the SLOC from 16 to 21.9K.
	4. Related Works - The approaches this program is modeled off of are popularly described in other papers. This application used an existing described application called Monkey to generate Fuzz (random) tests. This application also used previously developed tool, Hierarchy Viewer, to observe UI relationships.
4. Improvements
	1. When discusses the related works, I feel this paper could have done a better job giving credit to previously completed (and cited) works to describe how they utilized the various tools and results.
	2. In Table 8, where the authors list the identified classifications of bugs that were detected among the 50 sampled apps. The authors only listed the names of the applications in which they found bugs. For future knowledge and testing, they should have listed the other apps tested, but had no bugs, in case future testing programs are able to generate better coverage and identify different tests.
	3. Figure 4 is depicts the new results against the baselines results. However, these graphs (4a and 4b) are not very readable. In addition, Figure 4c is not clear and doesn’t properly label the axis; the authors wait until the caption to describe the units. This could have been better represented to make it quickly clear to the user what they are looking at. 
5. Relates to Reading
	1. The Dynodroid tool detailed in this paper uses Android’s Monkey testing tool as a baseline comparison, just as the authors did in Paper 1 for their AndroidRipper tool.
	2. Like in Paper 5, the process emphasized in the dynodroid tool uses symbolic execution to identify test cases for event driven applications. 
