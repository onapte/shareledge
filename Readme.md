Check [shareledge](https://youtu.be/MCXjIWhEbxk).

# Introduction to the project
This project's name is Shareledge, an online platform which allows content writers and bloggers to create and publish articles, tutorials and blogs on various topics. A user who is interested to publish articles or tutorials should register with Shareledge and then contact the admin to get verified for publishing. The users who are not verified will not have an option to create and publish.

# Distinctiveness and Complexity
The project is distinct from other CS50w projects in following ways   
* Unlike CS50w's Search, this project does not implement a search bar with Google's search mechanism or uses the Google's search API. Instead, it implements its own search mechanism. This project includes a search bar in the 'Articles' section which allows users to search or filter articles by category. The results of the search does not include Google web results but, the articles having the search query as a substring in their category. For example, if the search query is 'Blog' then the articles with category containing 'Blog' as a substring would be shown to the user. The project also does not have any interface similiar to the CS50w's Search project.
* Unlike CS50w's Wiki, this project does not include the implementation of any encyclopedia where there is be a fixed amount of information for each topic editted and saved by only the admin. This project allows users as verified authors to create and publish articles, tutorials or blogs on domains of their choice. In CS50w's Wiki, the markdown is converted to html and vice-versa. But, this project does not include an functionality which utilizes markdown to html conversion or vice-versa.
* Unlike CS50w's Commerce, this project does not implement an E-commerce site where users can create listings, place bids or win auctions. Instead, it allows users as verified authors to create and publish; allows any signed in user to rate an article or blog, place comment, subscribe to get notifications and additionaly, see other user rating and comments. It also allows anonymous users to read any article or blog of his or her choice. It also allows users access to a user-guide page where most of their questions can be answered.
* Unlike CS50w's Mail, this project does not involve use of single page applications. It also does not involve use of an API which allows users to send and receive mails. Also, there is no concept of 'Archived' in this project. Instead, it uses Django's mail sending interface via the 'smtplib' through which users can get notifications when any authorized user published an article or when a user has just subsribed to get notifications. It utilizes numerous specific pages to accomplish various tasks.
* Unlike CS50w's Network, this project does not implement a social media like application where users interact with each other, create posts and like each other's posts. Instead, this project allows users to rate articles based on the depth of information provided and view other user ratings. This project utilizes asynchronous requests only when a signed in user comments on an article. It also does not involve a feature which allows users to follow/unfollow other users.  

# Project files
In its main directory, this project includes only one app named 'shareledge'. Inside this app, the static files are contained in the static folder and the templates are contained in the templates folder. The static folder contains CSS and JS files related to each of the templates. Additionaly, it also contains a folder named 'ckeditor-plugins' which contains all the extra plugins related to the python package 'ckeditor'. The 'ckeditor' is a rich text editor which allows users to create neatly formatted and appealing articles with additional options. The templates folder contains the HTML files named after its specific function. For example, 'userProfile.html' includes template code to display user profile. This project utilizes db.sqlite3 database to store backend data. Also, the 'settings.py' file under the project folder includes functionality that allows Django to send e-mails to users and add special features to 'ckeditor'. So, in a nutshell  
* The file 'layout.html' contains the template layout of this project which serves as the base for other templates. Its related file is 'layout.css'.
* The file 'article.html' contains the information of a specific article opened by the user. Its related files are 'article.css' and 'article.js'.
* The file 'articles.html' contains a list of all the published articles in the website along with a search bar which allows users to filter articles based on category. Its related file is 'articles.css'.
* The file 'create.html' allows verified authors to create and publish articles by providing title, category, image url and content. Its related files are 'createArticle.css' and 'createArticles.js'.
* The file 'email.html' contains an email template that will be sent to the email of users who have subscribed to the newsletter.
* The file 'home.html' contains a template that will displayed as the home page. Its related files are 'home.css' and 'home.js'.
* The file 'login.html' allows users to sign in to the website.
* The file 'register.html' allows anonymous users to register with the website.
* The file 'unauthorized.html' contains an image and a message that is displayed only when a user tries to gain unauthorized access of certain components in the website. For example, this templated will be display when a non-verified author tries to navigate to the url of the create articles section.
* The file 'userGuide.html' provides users a guide in order to familiarize them with the user interface provided by the website.
* The file 'userProfile.html' displays various information of the users who have registered with the website like first name, last name, last login, status etc,. Its related file is 'userProfile.css'.

# Running the project
By providing steps to run the project we assume that django is installed in your system. To run the project the following steps can be followed.  
1. Open the terminal app available in your Operating System.
2. Navigate to the directory where you have this project installed or set up.
3. Run **'python manage.py runserver'** in the terminal.
4. Copy the link provided by the server in the terminal and open the link with any web browser installed in your system.

# Project features
* Users can view a list of published articles and filter them by category. The categories displayed will contain the search query as a substring.
* Registered users can rate the article after which they will shown the average rating of the article. The average article ratings will also be visible for each article in the article list.
* Registered users can add single-line/multi-line comments to an article which cannot be deleted.
* Registered users who wish to publish an article, blog or tutorial should contact admin via the email id given in the user guide section. The registered users will be allowed to access the create page only when the admin(s) manually activates it using admin interface.
* Registered users can subscribe to the newsletter with different email ids. After the subscribe button is clicked, the server sends them an acknowledgement message in their respective emails. Thereafter, if any new article is published by any of the verified users they will be notified by the server in their respective emails.
* Each article page contains a section which displays additional articles related to the same category.
* The verified users are allowed access to the create page. Using the ckeditor tools, the verified users can embed YouTube videos in the article, add emojis, add text-colours, add text weights and styles, change font-size, add images, add code-snippets, and add many other features.
