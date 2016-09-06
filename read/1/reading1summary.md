1. Paper:

 Using GUI Ripping for Automated Testing of Android Applications
 D. Amalfitano, A. Fasolino, S. Carmine, A. Memon, and P. Tramontana. Using GUI ripping for automated testing of Android applications. In Proceedings of 27th Intl. Conf. on Automated Software Engineering (ASE), 2012.

2. Keywords

 1. Rip: a technique to reverse engineer a model from a given system

 2. State Machine Model (GUI Tree):  A model AndroidRipper maintains informally referred to as a GUI Tree. The GUI Tree model maintains a set of states in the GUI and the transitions associated with the states that are encountered during the ripping process. 

 3. Bug Detection: Part of the overall goal of AndroidRipper. Upon its inspection of “WordPress for Android,” AndroidRipper discovered four previously undocumented bugs. By discovering new previously unfound bugs, AndroidRipper proved its effectiveness in finding bugs in a short amount of testing time making it a valuable investment. 

 4. Adaptive Random Testing: a method of testing that combines random candidate selection with a filtering process to encourage an even spread of test cases throughout the input domain. Android Ripper uses this to generate automated tests for mobile applications.

3. Brief Notes:

 1. Motivational Statement:
 While Android applications utilize Java, they cannot be tested using the traditional Java automated testing tools. This results in a number of bugs in the mobile application, such as frequent bugs due to incorrect management of the ‘Activity’ component lifecycle. This team of authors created a tool that generates test cases and automatically runs them against the application’s GUI to uncover bugs. 

 2. Sampling Procedures: 
 Authors chose to test their implementation of AndroidRipper against the open-source Android app “Wordpress for Android” (available at http://android.wordpress.org/). The authors cited the app’s “active development” and “broad user community”, along with the issue tracking system employed by the application’s developers, as reasons for using this application as the sample test application.

 3. Checklists:
 Within the section of design, the authors outlined concepts that the ripping technique relied upon. The outlined concepts were an event, an action, a task, and the GUI exploration criterion. An event is a user action performed on a GUI widget. An action is a sequence of zero or more data events followed by a single command. A task is an action and a GUI state representing action performed in a particular GUI state. Finally the GUI exploration criterion is a logical predicate that determines if the GUI exploration must be continued or terminated.  

 4. New Results: 
 The authors were able to uncover 4 previously unfound bugs, as well as coverage and process cost. They outlined their findings in the tables below:

 https://github.com/gbtimmon/ase16GBT/blob/3087063fbc490f74f301bff31b80ed02953cbeb1/read/Table12.png

4. Improvements:

 1. The authors could test more than one Android application in future work.
 2. The application can takes several hours to run and does not address what happens when the application encounters a crash. The paper does not define what happens or constitutes a crash.  
 3. The author could increase the number of crashes measured, since the current amount may be too low to be statistically relevant. 
 4. The abstract of the paper does not mention the design process of the AndroidRipper project, but a large section of the paper is focused on that subject.


5. Bonus Formal Survey:
   As the utilization and demand for Android applications has increased rapidly since 2010, so has the need for a testing platform for Android applications increased. A team of professors from the Università Federico II Napoli and from the University of Maryland have collaborated to produce a tool, Android Ripper, that is able to test Android apps through their respective Graphical User Interface (GUI), emphasizing the ability to identify bugs commonly classified as Activity. 
 
   Android Ripper is able to test the GUI by ripping, or reverse engineering, the app’s user interface and then executing a set of events, implemented as a list of tasks. As each task is fired, the state of the GUI is recorded and added to a growing GUI tree. The state may be failed or false if a bug is found and true if it executed in a manner which is expected. 
   This tool design was modeled after and combines attributes of two approaches to Android GUI testing, using state machines to describe the GUI and using a tree model consisting of simulated user events. The Android Ripper can be manually tuned to better handle different GUIs and detect specific runtime crashes unique to the application. 

   Android Ripper build upon previous work such as the Android Development Tool Monkey, which also use random discovery of Events in the application to identify novel test cases. Android Ripper makes improvements in automated detection of errors and in building a better internal model of the application. Android Ripper is able to identify a wider range of errors than previous algorithms. For instance, Monkey is unable to identify Activity errors.

   Android Rippers effectiveness was proven through testing using a live open-source android application, called WordPress for Android. The Android Ripper tool was able to identify bugs and gather code coverage and other metrics about the sample application. Android Ripper was able to generate six to eight crashes identifying four bugs, while the Monkey application was only able to generate a three crashes identifying a single Bug. In addition Android Ripper shows 12% better line of code coverage with comparable runtimes. 