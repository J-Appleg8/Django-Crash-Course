# Django Overview

User will request a URL on the site

- That request will go to a urls.py file
  -- Which will then call the views.py file
  --- And then that will call the models.py file
  ---- Which will query the database and feed it back to views.py ----- which creates the view of the website
  ------ Using templates to fill that view with HTML/CSS/JavaScript
  ------- And then that gets sent back to the user
