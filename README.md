<h1 align="center">
<a href="https://rate-my-mech.herokuapp.com/" target="_blank"> <img src="static/images/logo.png" alt="Rate My Mech logo"></a>  
</h1>

<div align="center">

[View this website through Heroku](https://rate-my-mech.herokuapp.com/) 
</div>

Rate My Mech is a community platform for keyboard enthusiats. The application contains different pages depending of if the user is logged in or not. 
If the user is not logged in the site displays, a home page, a keyboard page for viewing shared keyboards, a login/sign up page and an about page.
If the user is logged in a profile page and a page for building and sharing keyboard are available. The logged in user is also able to edit and delete their own keyboards. 

Rate My Mech was developed by a keyboard enthusiast for other keyboard enthusiats. The main purpose is for users to share their mechanical keyboards and find inspiration from others for their next build. 
The idea of the application is to make it user friendly and as a wise man once said: "good design is invisable", thus the application is kept as clean as possible. 

The goal of the application is:
* Host a user firendly environment which is intuitive by nature
* Provide both front end usability and back end functionality in order to create a full application experience 
* Spread joy

The users goals are:
* Share their keybords 
* Gain inspiration from other keyboards 

## UX

#### Ideal users are:
* English speaking
* Keyboard enthusiats

#### Users are searching for:
* A community platform for mechanical keyboards 
* A user friendly website which is responsive and suitable for both larger monitors and smaller screen sizes

#### This application make it easy for users to share and gain inspiraton because:
* It is intuitive and easy to use 
* It contains only neccesary features, thus reaching the statement above
* The application provides filter functionality which makes it easier for the user to find what they want

#### User stories 
* As a first time visitor, I want to view others mechanical keyboards to get inspiration
* As a first time visitor, I want to register for an account
* As a first time visitor, I want to (in a simpel way) use the platform to build and share my own mechanical keyboard
* As a returning visitor, I want to be able to log back into my previosly registrated user
* As a returning visitor, I want to be able change previous projects and upload new projects

#### Balsamiq mockups

## Featureas

#### Navigation bar and footer 

The navbar take two shapes depending if the user is logged in or not. If the user is not logged in the following navbar is displayed:
<img src="static/images/demo/demonotloggedinnavbar.png" alt="Demonstration navbar">
In this format, the navbar is kept very simplistic. The logotype is located to the left and when clicked takes the user to the home page. 
To the right we find the home button, the keyboard button and a login button. 
The keyboard button takes the user to the page to view uploaded keyboard while the login button takes the user to the login/registration page.



If the user is logged in, more options are available: 
<img src="static/images/demo/demologgedinnavbar.png" alt="Demonstration navbar">
Here we add more options to the user. The user is now able to view their own profile page displaying their uploaded keyboards and also build a new keyboard to share. 



The footer remains the same, not depending of the user being logged in or not:
<img src="static/images/demo/demofooter.png" alt="Demonstration navbar">
The footer contains three parts. First a link to the about page and beneath it a copyright statement and a recognition that the front end was built using the Materialize library.

#### Home 

<img src="static/images/demo/demohome.png" alt="Demonstration navbar">

At the home page the user is displayed with the logotype, a short statement. and a picture of "keyboard of the week".
Further down, two bottons are displayed. If the user is not logged in, the two buttons will be "keyboards" and "login/sign up".
If the user is logged in, the buttons will be "keyboards" and "Share your keyboard". 

#### Keyboards 

<img src="static/images/demo/demokeyboards.png" alt="Demonstration navbar">

At the keyboards page, the user will be able to view all keyboards that has been uploaded to the community. 
The user will be able to sort the keyboards depending on case material, keyboard size and layout. 
The user can also clear the filters by clicking the button "clear filters". 

On all keyboard cards, the button "view keyboard" is available. If clicked, the user will be sent to a page with a more indepth view of the specific keyboard.

#### View specific keyboard 

<img src="static/images/demo/demoviewkeyboard.png" alt="Demonstration navbar">

When the "View keyboard" button is clicked on the previous page, the user will get more information of the keyboard of their choice. 
Here, the user can see the full description of the keyboard, who created it, an enlarged picture, what switches are used, from which brand the components are from and more. 

This page also include an "edit button" if the user is the creator of the keyboard. This button will take the user to the edit/delete page which is presented further down in this README. 

#### Login / Registration 

<img src="static/images/demo/demologin.png" alt="Demonstration navbar">



#### Profile / My keyboards

<img src="static/images/demo/demoprofile.png" alt="Demonstration navbar">

My keyboards is visible for logged in users only. At this page, all the projects created by the logged in user is gathered. 
From this page, the user can easily view their own keybords in depth and from there edit or delete the keyboards. 
Below the kayboards an option for sharing another keyboards is displayed. 

If the user have no shared keyboards the page will display a text with this information, and the user have the option to share their first keyboard. 

#### Build keyboard 

<img src="static/images/demo/demobuild.png" alt="Demonstration navbar">

When the logged in user want to share their keyboard, they are faced with an intuitive way of doing so. 
The user need to name the project and describe it. These two input fields are the only two required for the upload to pass the system. 
The other options to pass in are displayed in dropdown menues with alternative. These dropdown menues cover case information, switch information and layout/size information. 
The user is also able to pass in a URL for the keyboard if desired. 

The keyboard is passed to the database when the save button is clicked. 

#### Edit / Delete  

As mentioned above, the user will be displayed with the option to edit a keyboard on the indepth view page if they are the creator of the specific keyboard. 
The edit/delete page look identical to the "build" page except that the fields are filled in based on the information from when the keyboard first was built or from the last edit. 
Also, instead of the save bottom on the bottom of the page, the user now have the option to save the changes or delete the keyboard. 

#### About 

The about page contain the Rate My Mech logo and a short text why the application was created and whom it is for. 

#### Database 

<img src="static/images/demo/demodatabase.png" alt="Demonstration navbar">

# Technologies used 


* Python
- Flask
- PythonDNS
* Heroku
* MongoDB

