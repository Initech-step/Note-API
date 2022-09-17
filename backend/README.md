## Task

The task of this API is to build a simple note app to help user keep track of todos

**Project status: Complete**

### Local machine Requirements
check the 'requirements.txt' file


**This project ships with Bootstrap 4.5, But you will need to have an active internet connection as it connects to bootstrap icons CDN**

## Steps to get the Project Up and running

1. Create a virtual environment in the backend folder and activate
2. install requirements.txt
3. navigate with the terminal into the main folder where `manage.py` is located
4. In the terminal run `python manage.py makemigrations` : This is to initialize the database
5. In the terminal run `python manage.py migrate`
6. In the terminal run `python manage.py runserver`

**This will expose a localhost Port which you can visit to view the application**
**Enjoy viewing the application and making your own changes**

I built a simple vue application to consume this API. Check the frontend folder.

# API Documentation

### Base URL 'http://localhost:8000/api/'
### all endpoints must have an ending slash

-------
ENDPOINTS
-------
#### GET 'note/'
Action: gets all notes



#### POST 'note/'
Action: add a note

Request body
```
{
    "note":"text xxxxx",
    "category": "category xxxx"
}
```


#### GET 'note/${note_id}/'

Sample response:
```
{   
    "id": 1,
    "note":"text xxxxx",
    "category": xxxx
}
```


#### PUT 'note/${note_id}/'
```
{
    "note":"text xxxxx",
    "category": "category xxxx"
}
```

Sample response: STATUS_200_OK



#### DELETE 'note/${note_id}/'
sample response: STATUS_200_OK



#### GET 'category/'
Action: gets all categories



#### POST 'category/'
Action: add a category

Request body
```
{
    "category": "category xxxx"
}
```


#### GET 'category/${category_id}/notes/'
Action: get notes by category



#### GET 'predit/${id}/'
Action: This serves as a preflight request before the edit of a note


### Happy coding
