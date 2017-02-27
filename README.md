# calmmute
Calmmute is built upon the idea that commutes are cognitively important: having time between engagements allows our brains to finish processing the last thing we did before it begins work on the next. We noticed that often people either schedule meetings back-to-back, or use their "awkward" between-meeting time to do more work. Both of these scenarios remove the precious commute time and can cause stress and cognitive difficulty.

## Current State of the Software:
![Homepage](https://github.com/YehEmily/calmmute/blob/master/screenshots/1)


The user opts in to the calmmute experience and tells the site how they feel and how much time they have for this. This takes them to a page where they are served some meditation music and a yoga pose. They have the option to get a new yoga pose without interrupting the music. When they are done, they can provide feedback on the experience.

## How the Code Works:
### Organization
There are two pages of our site: The greeting page and the Calmmute page. The greeting page is built in index.html and server.py, and is made up of html and some javascript/jquery. The Calmmute page is built in calmmute.html, pose.html, and server.py, and is made up of html, javascript/jquery, and embedded elements from The Meditation Podcast's soundcloud page and www.yoga.com for the music and yoga pose respectively. 

### Data Flow
The user's feedback and other entered data is saved to a text file. It is not currently displayed or used beyond that. 

### How to Run the Code
First, download the repo from github. Our project requires you to have urllib.request. Our page is currently run locally, so you will need to navigate to its location in your terminal and then enter "python3 server.py" This should start up the server and give you a link for your browser to access Calmmute. Enjoy!

## Issues and Future Work
### Known issues
Calmmute does not consistently function in the Firefox browser, for unknown reasons related to the embedded video. Chrome seems to work fine.
### What Could Be Next
We aren't sure what the best delivery of this page is. As an installation, it could be run from a tablet or other smart device with a screen, and could be installed in an appropriate curated space. As an app, a person could engage with it regardless of location. As a web-page or app, the interface could be both in an installation setting and portable. We have not decided which to do as of the completion of this stage. 

Use the time information that the user enters at the beginning to customize their experience: choose a song of appropriate length, somehow alert them that their time has elapsed. 

