# emptor_backend

## About my decisions

I've chosen Django since I haven't worked with Python for 3 years and it's the Python framework that I'm the most comfortable with.

About the database, I decided to design it as a reporting database. When it comes to data normalization, it would be better to design it as an operational database, but for all read operations, some join operations would be necessary. Furthermore, there wouldn't be other reasons for using an operational database besides having a well-normalized database. So in this case, I've chosen performance over normalization. This article helped me to make this decision: https://martinfowler.com/bliki/ReportingDatabase.html

I've saved the data of the WorldBank site as CSV files and created a Django custom management command for populating the database with this data.

Unfortunately, I didn't have enough spare time to do everything I was planning. I left some things for the last minute, like creating environment variables, creating more tests and integrating Sentry into the project, but I ran out of time.

## Inital project setup

```!
docker-compose up

docker-compose exec web python manage.py migrate
```

## For populating the database

```!
docker-compose exec web python manage.py populateapidatabase
```

The project is already running in `http://localhost:8000/` and the API is in `http://localhost:8000/api/display_data/`. Now let's run the frontend project. In the frontend project, there's a README.md with all the instructions for this.
