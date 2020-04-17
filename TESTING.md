<div align="center">

[View this website through Heroku](https://rate-my-mech.herokuapp.com/) 
</div>

## Testing 

### Validation

The code for the application has been tested using [W3C's HTML Validator](https://validator.w3.org/) for the HTML code, [W3C's CSS Validator](https://validator.w3.org/) for the CSS code and [JSHint](https://jshint.com/) for the JavaScript code.
For the code written in python I used [PEP8online](http://pep8online.com/) as a validator.

We get one error when running the HTML validator:
* On the page displaying the keyboards: "Duplicate ID". - This is because the flask/jinja code generates a for-loop and thus creating the similar object multiple times. This does not affect the applications performance.

We get no errors when running the CSS code through the CSS validator. 

We get one warning when running JSHint:
* On the JavaScript code for filtering keyboards on the "keyboard page" we get: "'size' is better written in dot notation". This is a recommendation and does not affect the performance of the application.

We get one warning when running running the python validator: "Line 15: line too long (82 > 79 characters)". This regards the key used to encrypt the passwords. This does not affect the performance of the application.

### Function by function 

#### Navigation bar logo
* Tested on all pages and the logo redirects the user to the home page. No errors.

#### Navigation bar menu buttons
* Tested on all pages and each button redirects the user to the selected page. Log in/log out button work as expected. No errors. 

#### Collapsable navbar
* Tested on all pages and each button redirects the user to the selected page. The navbar then collapses after choosing an option. Log in/log out button work as expected. No errors. 

#### Home page
* The two buttons on the bottom of the page work as expected, both when logged in or not. No errors. 

#### Keyboards page
* Sorting function work as expected. All cards display as expected and "view keyboard" button for each card redirect the user to the selected keyboard. No errors.
* The clear function of the dropdown menues does not work as intended. The keyboards displayed for the user are correct but the slected options in the dropdown menues does not go back to their base value. Needs additional JavaScript code to work as expected. Rather a bug than an error.

#### View specific keyboard
* All information rendered and displeyed as expected. When user is logged in, edit button work as expected. No errors.

#### Login page
* The login function work as expected. When trying to log in without passing in any information the user is faced with alert messages showing input is required.
When passing in a username and/or a password that does not exist, the user is redirected to an error page saying that something went wrong and gives the user the alternative to go back to the login page or register.

#### Register/sign up page
* The sign up function work as expected. When trying to log in without passing in any information the user is faced with alert messages showing input is required. When registred, the user is redirected to the login page. 
* One bug is detected, we can create multiple users with the same username, this must be investigated further.

#### Profile / My Keyboards
* The projects created by the user is displayed and all buttons work as expected. No errors. 

#### Edit/Delete page
* The page collect previous selected options/text input as expected. The update function work as expected. The delete function work as expected. No errors. 


## General issues
* One general issue has been beeing spotted regarding images. Sometimes some images are not beeing displayed and the 'img' element does not lean back on the 'alt' attribute, instead display a brocken image icon. This need more investigation. 

## Future testing

* In the future, automatic testing will be included to make the testing more comprehensive. 