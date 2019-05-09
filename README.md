# revisit-advisor
This robot advisor pulls up a stock from the alphavantage API and gives a summary of the stock's performance before making a recommedation on whether the user should buy, hold or sell the stock. The recommendations are simplistic, and based on the author's individual opiions about the stock. The recommendations are considered professional investing advise and should not be taken as representation, but a simple statement of the author's personal evaluation of the stock.

Configuration
To configure you will need
1. An API key from alphavantage https://www.alphavantage.co/support/#api-key
2. Some popular stocks you might like

Installing
1.To install simply download the link to the app code on the author's github https://github.com/mr1301/revisit-advisor
2.Load the code onto a terminal
3. Input your secret API Key into the dot.env file
4. Input the stock symbol you are looking for e.g MSFT and run the program

Packages Used
For full functionality ths app requires 
1. A requests package - to access the Alphavantage url
2. A  Dotenv package - to store the secret API
3. A json module - to parse the text from the requested url
4. A csv package  - to write and read data from and to the stock history file
5. An os modula - to locate files in the directory
6. A datetime module - to time the recommendation
7. A pytest module was used to conduct automatic tests

All of the above are needed to ensure all the functionality is met. Copying this code should come with all the modules, but do import if they aren't available or incompatible.
After running the code a recommendation and brief stock history should be displayed. Feel free copy to share your results.

Manifest
advisor.py - the appplication
advisor_test - the pytest for the application
.gitignore - to store the secret API Key file
.env - hold the API Key in here
prices4.csv - contains the actual results from the request
example.csv - used for pytesting
License file

Copyright
This product is licensed under the MIT licesne, see lincense file for reference.

Troubleshooting & known bugs
All the pytest run for this file where successful.  A manual test was conducted to check url collected, but an automatic test could be a bug because of having to use the API Key in the test, and not having an effective way of testing the API key without revealing it.

Author 
Mercy Radithupa

Credits & acknowledgments
This assignment could not have been completed without the help and guidance of Prof. Rossetti's lectures, videos and examples. In particular for the pytesting this source was helpful: https://github.com/s2t2/robo-advisor-screencast/pull/1/files.