1. Paper
	Yang, S., Yan, D., and Routev, A. 2013. Testing for poor responsiveness in Android applications. In Proc. International Workshop on the Engineering of Mobile-Enabled Systems. MOBS '2013. 10-20.
2. Keywords
	1. Poor Responsiveness - In a mobile (Android) application, “if an application takes more than 200 ms to respond to a user event, it is perceived to be sluggish and unresponsive.”
	2. Test Amplification - A method of executing and evaluating a program against several test criteria that have been “amplified by throwing additional exceptiosn at API calls,” in order to find negative “janky” (poor responsive) results.
	3. Flash Storage Access - This is a file system that is implemented on top of flash storage, which means that there is both internal and external non-volatile storage, so data is not erased when power is lost.
	4. Jank - Excessive work performed in the event-handling thread, which in ANdroid is the main thread of the application. This term was coined by Google engineers. 
	5. Bitmap Processing - A bitmap is a display space where each bit (pixel) has a defined color. A large bitmap is computationally expensive to process and should not be done in the UI thread. This can be used to identify poor responsive time when process larging HD images.  
3. Brief Notes
	1. Motivational Statements - Poor responsiveness is a major usability problem and is detrimental to an Android application’s success. However, there are very few tools that are able to comprehensively and correctly identify errors due to poor responsiveness.
	2. New Results - The authors presented their results in a formatted table, detailing how each application performed with how many fails. The authors were able to make the initial conclusion that their testing method is able to detect poor responsiveness errors in Android applications, using various case studies. ![Results](https://github.com/gbtimmon/ase16GBT/blob/master/read/7/Figure1.png "Results")
	3. Related Works - The authors discussed various methods of measuring and preventing poor responsiveness in mobile applications, all of which involve identifying and characterizing the latency of event handling code. One specific approach, LagHunter, uses heuristics to measure and track the run time of particular methods within an application.
	4. Future Work - The authors point out that there is much room for exploration in the areas of automated discovery (both static and dynamic analysis) that is able to manipulate large/expensive resources, designing new patterns and principles that account for and prevent responsiveness defects, among many other suggestions. 
4. Improvements
	1. The authors do not address how the applications used in the Case Studies were selected.
	2. Based on the wording, I believe the authors did not construct uniform tests that were executed across all applications. I think they constructed individual tests for each application. This consistency may not have reflected accurate results. Maybe the tests could have found more potential errors, or discovered more because the tests were directed there based on user knowledge. 
	3. I would like to have seen more detailed results about how the amplification criteria performed when executed. Another table would have been helpful to see how all of the different API calls performed. Maybe one didn’t cause as many errors. 
5. Relates to Reading
	1. This paper is aiming to identify different errors than any paper previously discussed. All other papers from Paper 1 on have focused on identifying different errors that were related to results, null pointers, etc. This paper focused on “Application Not Responding” errors and issues associated with timeouts.
	2. This paper actually used the tool discussed in the first paper, AndroidRipper, to construct test cases for the GUI.
