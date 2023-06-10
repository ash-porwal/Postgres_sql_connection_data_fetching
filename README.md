This repo uses the PostgreSQL database which is setup on my local(to see how to set it up please visit my article written on medium - link is in the bio). This will fetch list of tables and its all data residing in my database with schema as Public.

# Postgres_sql_connection_data_fetchingPostgres_sql_connection_data_fetching/

## Tree Structure down below. <a id="layout"></a>
```
Postgres_sql_connection_data_fetching/
├── config.ini  #credential file
├── helpers     
│   ├── __init__.py     #indicator that a directory should be treated as a Python package
│   └── postgres_data_fetching.py   #helper module to extract data
├── main.py     #main file
├── README.md
└── requirements.txt    #required modules to run the script

1 directory, 6 files

```

## Probelms I faced. <a id="layout"></a>
The Problems I faced are - 
1. First problem - As I've installed PostgreSQL on my Ubuntu machine. So, I wanted to access database through terminal only and exporting a new database became challenging for me through terminal(its solution is in my medium article, where I've exported dvdrental database).

2. Second problem I faced while installing psycopg2 library first time on my Ubuntu machine.

Below is the Overview of error:
```
while installing psycopg2 getting error
note: This error originates from a subprocess, and is likely not a problem with pip.
error: legacy-install-failure
```

**Solution for above -** 

The "legacy-install-failure" error usually occurs when there are issues with the compilation and installation process of the psycopg2 library. This error can have multiple causes, such as missing dependencies or incompatible build tools. Here are a few troubleshooting steps you can try:
**Install Dependencies: psycopg2 requires the PostgreSQL development headers and libraries to be installed. Make sure you have them installed on your system. In Ubuntu, you can install them using the following command:**
```
sudo apt-get install libpq-dev
```
For other operating systems or distributions, refer to the PostgreSQL documentation or package manager instructions.

**Python Development Headers: Ensure that you have the Python development headers installed on your system. They are necessary for building Python C extensions. You can install them using the following command:**
```
sudo apt-get install python3-dev
```
Replace python3-dev with the appropriate package name for your Python version and distribution.

**Upgrade pip and Setuptools: Outdated versions of pip and setuptools can sometimes cause installation issues. Try upgrading them by running the following commands:**  
```
pip install --upgrade pip
pip install --upgrade setuptools
```

**installing psycopg2-binary, which is a binary distribution of psycopg2 and does provide precompiled wheels.**
```
pip install psycopg2-binary
```

**Now, try to install psycopg2**
```
pip install psycopg2
```

3. Third problem - was when i tried to get connection to my database through python script, i faced - peer authentication error
and above error message means

**The error message encountered suggests that the connection to the PostgreSQL server failed due to an authentication issue. The "Peer authentication failed for user "`<user_name>`" error indicates that the authentication method specified in the PostgreSQL server configuration is set to "peer" for the "`<user_name>`" user, but the connection attempt did not provide the required credentials.**
To resolve this issue -

1. Use Password Authentication - Update the PostgreSQL server configuration to use password authentication for the "`<user_name>`" user. Open the **`pg_hba.conf`** file, typically located in the **`/etc/postgresql/<version>/main/`** directory.
2. Find the line that corresponds to the "`<user_name>`" user and change the authentication method from `peer` to `md5`. It should look like this:
```
local   all   postgres   md5
```
Save the file and restart the PostgreSQL server for the changes to take effect. 
```
#restart
systemctl restart postgresql

#check status of service after restart
systemctl status postgresql
```

## Commands to run program. <a id="layout"></a>
```
#To make virtual environment
python3 -m venv venv

#To activate source env
source venv/bin/activate

#To install pacakges from requirements.txt
python3 -m pip install -r requirements.txt

#To run the file
#in foreground
python3 main.py

#in background - & symbols tell to run process in background in Unix.
nohup python3 -u main.py > nohup.out &
```
