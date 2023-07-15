![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome Christopher Meddings,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!


# __Portfolio Project 3 - Python__
## __ChrisSweeper: Mine Hunter__
![ChrisSweeper: Mine Hunter]()

### __Demo__

The live site can be viewed here - [ChrisSweeper: Mine Hunter](https://chrisweeper-minehunter-70712a3a8751.herokuapp.com/)

Github repository can be viewed here - [CMed01/portfolio-milestone-3](https://github.com/CMed01/portfolio-milestone-3)


## Table of Contents
* [User Experience](#user-experience)
* [Technologies](#technologies)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

## __User Experience__

### __Strategy__
The aim of the website is to display an interactive mine searching game.
Reasons for the site:
* Enjoyment
* User interaction

#### __User Stories__
* As a user I want to be able to:
    * Easily understand the main purpose of the website.
    * Easily navigate the website to find and intereact with the content.
    * Easily understand the instructions of the game.
    * Specify the size of the mine grid before starting the game, adjusting the difficulty.
    * Generate a game grid with randomly generated mines equal to the width of the grid. The values of each grid square will initially be hidden from view
    * View the number of mines left to detect and the number of attempts remaining to locate all the mines
    * Input co-ordinates to reveal grid squares and gain knowledge of the number of mines in the surrounding grid squares.
    * Gain information of the number of mines surrounding
    * View the complete grid layout and location of mines and remaining square values when either all mines have been found or attempts have run out.

* As a developer I want:
    * The user to be able to change the level of difficulty by allowing them functionailty to determine the size of the grid.
    * The user to have limited number of attempts to find all mines, so that the game presents a challenging and engaging experience.
    * The user to be able to track their progress, with information detailing the number of mines and lives remaining as well an updated mine grid.

### __Scope__
Functionally the site must be:
* Easy to navigate.
* Input functionality working.
* The terminal to clear after each successful input.
* Clear information given if incorrect inputs are made.

Content should include the following:
* Provide the user with the rules of the game.
* Provide interactive functinaility to play the game.

### __Structure__
Based on the content required in the scope of this projct, this website will consist of one page. The page will contain a simple structure with an embedded terminal. Within the terminal will be the interactive function of this game.

### __Skelton (Lucidhart)__
As the template for the front-end website design is pre-set. There are no wireframes included in this readme. [Lucidchart](https://www.lucidchart.com/) was used to create the process map for the game logic.

<details open>
<summary>Process map </summary>
<br>

![Game process map](./readme-assets/process-map.png)

</details>

### __Surface (including Features)__

#### __Features__
* Initial screen
* Grid display
* Co-ordinate guess
* Inout validity

* Future
    * Add recursive function to expose all grid values with 0
    * Add flag function to convert to a more traditional minesweeper game.

## __Technologies__

### __Languages__

* Python

### __Frameworks, programs and libraries__



## __Testing__

### __Validator testing__



### __Browser Compatability__
* Browser testing was completed on the following browsers using [SauceLabs](https://saucelabs.com/)
    - Chrome Version 112.0.5615.138 (Official Build) (64-bit)
    - Firefox Version 111.0 (64-bit) 
    - Edge Version 112.0.1722.34 (Official Build) (64-bit)
    - Safari Version 16.1 (18614.2.9.1.12) (accessed via macOS Ventura 13) 

### __Test Cases and Results__

<details open>
<summary>The below table details the test cases that were used. </summary>
<br>
</details>

## __Deployment__

### __How this site was deployed__

1. In the GitHub repository, navigate to the Settings tab, then choose Pages from the left hand menu

2. From the source section drop-down menu, select the Master Branch

3. Page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment

4. Any changes pushed to the master branch will automatically start a workflow to build and deploy the page with the update code.

The link to the live website can be found here - 

### __How to clone the repository__

1. Go to the 
 repository on GitHub.

2. Click the "Code" button to the right of the screen, click HTTPs and copy the link there

3. Open a GitBash terminal 

4. Change the working directory to the location where you want the clone directory.

5. On the command line, type "git clone" then paste in the copied url (https://github.com/CMed01/portfolio-milestone-2.git) and press the Enter key to begin the clone process

## __Credits__

### __Content__

* All content was written by the developer

### __Code__

* 


### __Media__


### __Acknowledegements__

I would like to express my gratitude to my mentor Brian Macharia, for his guidance, support and encouragement throughout my second project.