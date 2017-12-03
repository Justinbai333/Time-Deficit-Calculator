# Time-Deficit-Calculator
For Machine Problem 7 of CS125 in UIUC
This is a program that counts the time deficit clocks would experience due to special and general relativity. (Denoted by SR and GR)

It uses for loop to calculate midpoint Riemann sum of the desired integration. 

It can be used for two cases:

(i) Calculating the time deficit a clock on the earth would experience annually.

(ii) Calculating the time deficit a clock on a satellite orbiting around earth at certain fixed radius would experience annually.

All physics formulus used in this program are covered in PHYS 211, 214, 225 of UIUC physics curriculum.
Users of this program are assumed to own basic knowledge of classical mechanics and relativity.
Program is designed only for calculation use, not for the study of physics.

# Instructions

## Standalone script
To run the standalone script, run `python Time\ Deficit\ Calculator.py` in the root directory of this project.

## Web app
To run the web app, install Flask.
`pip install flask`
Then run `python app.py` and enter 127.0.0.1:5000 in your browser.

# Contributions
Justin designed and wrote all the code to calculate the time deficits for each clock type using physics.
Brian allowed users to enter parameters for the standalone script and developed the web app that displays the calculations on a web page.
