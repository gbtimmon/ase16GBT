1. Paper
	S. R. Choudhary, A. Gorla, and A. Orso. Automated Test Input Generation for Android: Are We There Yet? In Proc. of the IEEE/ACM International Conference on Automated Software Engineering (ASE), 2015.
2. Keywords
	1. Activities - “the components in in charge of an app’s user interface.” These are controlled by callbacks for each lifecycle phase and are represented as UI elements like buttons.
	2. Services - “application components that can perform long-running operations in the background.” Services may be indirectly tested, but usually aren’t the focus of testing an Android app.
	3. Broadcast Receivers and Intents - “methods for inter-process communication … that can either be declared in the manifest file or at runtime.” Receivers allow an app to be triggered and react to an event such a call or text message. 
	4. Content Providers - “a structured interface to shared data stores.” These data stores impact the behavior of the application and thus content providers must have a variety of tests to understand an app’s full behavior.
3. Brief Notes
	1. Motivational Statement - In the paper the authors state two motivations or goals for this paper: “The first goal is to assess these techniques (and corresponding tools) to understand how they compare to one another and which ones may be more suitable in which context (e.g., type of apps). Our second goal is to get a better understanding of the general tradeoffs involved in test input generation for Android and identify ways in which existing techniques can be improved or new techniques be defined.” 
	2. Sampling Procedure - The authors outlined the criteria they evaluated each of their applications on to determine its performance. The criteria were: ease of use, android framework compatibility, code coverage achieved, fault detection ability.
	3. Checklist - They provided a checklist for each application tested. ![Checklist](https://github.com/gbtimmon/ase16GBT/blob/master/read/8/Figure_1.png "Checklist")
	4. Informative Visualization of Results - Here is a direct comparison of the kinds faults and number of faults detected in each application area. ![Results](https://github.com/gbtimmon/ase16GBT/blob/master/read/8/Figure_2.png "Results") They also did a statistical analysis of the coverage generated from each tool. ![Statistical Analysis](https://github.com/gbtimmon/ase16GBT/blob/master/read/8/Figure_3.png "Statistical Analysis")
4. Improvements
	1. Figure 4 provided a lot of information, but I think it could have been labeled better and included a legend to help quickly identify applications being compared as well. This is a little bit nit-picky.
	2. Future work and conclusion did not address what additional benchmarks they wished to test and how they might have impacted the current results.
	3. They discussed very specific input fuzzer applications in great detail, but these applications weren’t used in the study. The reason why input fuzzers were not used in this study was described, but why the details about different input fuzzers seemed irrelevant and misleading compared to the applications/tools actually evaluated.
5. Relates to Other Readings
	1. Dynodroid, one of the applications evaluated in this study, was developed in paper 6.
	2. This paper was just in general more detailed than the majority of the other papers. It better explains how they chose the sample applications and the significance of the criteria. 




