# NewRead
Project description
an app that allows a reader to read a book/text/etc. 1 word at a time putting out hundreds of words a minute based on what the user wants. holding down a button the user selects (defualt spacebar) will have the text be read to the user. this text can be written or maybe even imported from another source and once it's there you can see what you have read and click to where you want to read forward or backwards. the plan to make this work is the words read will be highlighted a color (color tbd maybe blue) that the user can change. the speed at which you read can be changed and the text will start at a lower speed and ramp up to the speed selected. the default start speed will be changable aswell as the ramp up speed so the user can have the speed they want to have.

I will be utilizing python, django, html, and css to work on this project as well as other resources to help me learn along the way.

one part mentioned in the description above that will cause problems is the importing texts. This could hopefully import PDFs, HTMLs, TXTs, WRDs, and websites however each will display a unique problem that must be solved, especially websites. maybe by only looking at the body texts that would work, maybe i need to strip the sidebars, advertisements, pictures, etc. the work with the the text so i can get titles. I'm going to need to do a lot of research in unkown territory.

How to run the project.
Visiting the website [no website provided yet] should run the project, however to recreate you will need to download Python 3.12.3, django 5.0 on the IDE of your choice, Visual Studio Code was my IDE of choice.

How to use the project.
Textbox: on the website there will be a visible textbox that you can write in; this is where you want to input the text you want to read, probably works best if copy+pasted or if i can get the import to work.
Label: In the middle of the page there will be a label that will display what is in the textbox 1 word at a time, this should be empty if the textbox is empty, have the first word of the textbox if a text was just inputted, or be on the word you last read when you were reading.
Read button: a button under the label that will indicate what key the user wants to use to read the text, this button can also be pushed in place of the key hold to read through the text.
Wps speed: close to the label, this is a textbox, 2 button combo that will allow the user to choose the speed at which they read at. I will need to do some testing to find a good default value, however the user can type a prefered number in there or use the buttons to make the speed number go up or down (probably in multiples of 5 or 10).
Menu: there should be a menu button that can change all settings and defaults to the users' liking.