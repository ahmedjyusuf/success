# success

site name
	Meta Tutoring

homepage desgin ideas for online Tutoring website '/'
	https://www.goskills.com/
	https://auzmor.com/learn/


change directory to the ./backend folder and install requirements.txt with command below
	pip install -r requirements.txt
	python manage.py runserver

	I have created a super user for you with the following credentials which you can login at '/login' or '/admin'
		login with email: dfm880@gmail.com
		password: year2023


signup '/signup''
	check errors example: The password is too similar to the first name. btw the errors are coming from the backend server.
	
	after Signing up display message saying please check your email for account verification
		then redirect to '/'

email verification '/activate/:uid/:token'
	message: thank you for verifty you email, please log in.
		redirect to '/login' after verification

userprofile '/profile'
	login with: dfm880@gmail.com
	password: year2023

	display the user and their zoom class info


Zoom
	make '/zoom/:link' route that takes in the zoom link and make a react/zoom integration. I think there's a react zoom sdk you can user for that.




delete_users.py script
	script to delete users for re-testing, Run following command. only 2 main amind users will remain
	python delete_users.py


my build command to copy over build folder to the backend
	"build": "rm -rf ../backend/build && react-scripts build && cp -r build ../backend/build",
