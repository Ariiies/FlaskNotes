# FlaskNotes

This project is a **web application** built with Flask that allows users to efficiently **manage and search notes**. It offers the following features:

## Features
- **Create, edit, and delete notes**: Users can manage their notes with ease through a simple interface.
- **Advanced search**: An optimized search system helps users find relevant notes quickly.
- **User authentication**: Secure login and logout functionality ensures that only authorized users can access their data.
- **Session handling**: The app maintains user sessions, so they don't need to log in repeatedly.
- **Paginated results**: When searching or viewing notes, results are displayed in pages for better navigation.

## Technology Stack
- **Flask**: The core framework used to build the application.
- **Jinja2**: For rendering HTML templates dynamically.
- **Flask-Session**: Used to handle user sessions securely.
- **SQLite/MySQL** (or any other DB): Database integration for storing user and note data.

## How It Works
1. **User Management**: Users can sign in and out, with session data being stored securely.
2. **Note Management**: Users can create, view, edit, and delete their notes.
3. **Search System**: The app includes a robust search feature to quickly find specific notes.
4. **Pagination**: Large search results are paginated for easier browsing.

## Page views 
 ### 
 1. **Main page.** <br>
 first view to open the page. <br>

    ![Main Page](page_views/mainpage.png "Main Page")
    
2. **Search Sage.** <br>
    Page where the search starts.
    ![Search Page](page_views/searchpage.png "Search Page")
3. **Result of search.** <br>
    View of the results obtained for the "Nolan" search.
    ![Results Search](page_views/resultsearch.png "Result Search")
4. **Show All Notes.** <br>
    View of notes page where all notes stands.
    ![All Notes](page_views/allnotes.png "All Notes")
5. **Note Page.** <br>
    View obtained for select and click a note.
    ![Note Page](page_views/notepage.png "Note Page")
6. **Login Page** <br>
    View of the login page, where the user logs in.
    ![Login Page](page_views/loginpage.png "Login Page")
7. **Logview.** <br>
    View of the main page when a user logs in, the only difference is the new button with the users name and the welcome.
    ![Logview](page_views/logview.png "Logview")
8. **Options User.**<br>
    Options user's view, only option to view profile's user and log out.
    ![Options User](page_views/opcionsuser.png "Options User")
9. **User Profile.** <br> 
    User's profile view where there is only data and the option to create a new note.
    ![User Profile](page_views/userprofile.png "User Profile")
10. **Create Note.** <br>
    Creation note's view.
    ![Main Page](page_views/createnote.png "Main Page")
11. **Footer.** <br> 
    Footer view where you can see the page navigator, which is dynamic according to the number of available pages.
    ![Footer](page_views/footer.png "Footer")

