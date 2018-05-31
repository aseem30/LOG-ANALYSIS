# LOG ANALYSIS

* Printing report based on data in database by using python(2.7.14) and postgresql.

### Installations

1.Install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/) version till 5.1 only as the versions above it are not compatible with current version of vagrant.
2.Download or clone [fullstack-nandegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository from github.
3.Now we have newsdata.sql in our vagrant directory.
4. For further refernces about installations, refer `Part 3: Lesson  2: Elements of SQL` in your classroom.

### Running the program
* Change the directory to vagrant directory.
* Run `vagrant up` command to run the vagrant on virtual machine.
* Run `vagrant ssh` to login into virtual machine.
* Change the directory to `/vagrant`.
* Use command `psql -d news -f newsdata.sql` to load database.
    -use `\c` to connect to `database="news"`
    -use `\dt` to see the tables in database
    -use `\dv` to see the views in database
    -use `\q` to quit the database
* Use command `python LOG-ANALYSIS.py` to run the program
* For further refernces about running the project, refer `Prepare the software and data` lecture in the `Project description` section of your classroom.

### PSQL Command Used To create the view

#### ARTICLE VIEW

```
CREATE VIEW arview AS
SELECT title,
       author,
       count(title) AS views
FROM articles,
     log
WHERE log.path LIKE concat('%',articles.slug)
GROUP BY articles.title,
         articles.author
ORDER BY views DESC;
```

#### AUTHOR VIEW

```
CREATE VIEW auview AS
SELECT name,
       sum(arview.views) AS total
FROM arview,
     authors
WHERE authors.id=arview.author
GROUP BY authors.name
ORDER BY total DESC;
```

#### TOTAL REQUESTS VIEW

```
CREATE VIEW totrequests AS
SELECT count(*) AS COUNT,
       date(TIME) AS date
FROM log
GROUP BY date
ORDER BY COUNT DESC;
```

#### ERROR REQUESTS VIEW

```
CREATE VIEW err_requests AS
SELECT count(*) AS COUNT,
       date(TIME) AS date
FROM log
WHERE status!='200 OK'
GROUP BY date
ORDER BY COUNT DESC;
```

#### ERROR PERCENTAGES VIEW
```
CREATE VIEW err_percentages AS
SELECT totrequests.date,
       round((100.0*err_requests.count)/totrequests.count,2) AS err_prc
FROM err_requests,
     totrequests
WHERE err_requests.date=totrequests.date;
```	