# Linux-Server

## Info

Public IP address: `52.221.234.110`
Site Url: `52.221.234.110.xip.io`
Note: Only Google Login is available currently.

## Lightrail setup
1. Download Lightrail default keys.
2. mv ~/Download/LightsailDefaultKey-ap-southeast-1.pem ~/.ssh/
3. chmod 700 ~/.ssh/
4. chmod 600 ~/.ssh/LightsailDefaultKey-ap-southeast-1.pem
5. Connect to remote Server using ssh ubuntu@server -i ~/.ssh/LightsailDefaultKey-ap-southeast-1.pem

## User Management

1. Log in to remote as *ubuntu* user with `ssh ubuntu@server -i ~/.ssh/LightsailDefaultKey-ap-southeast-1.pem`
2. Add new user with `$ sudo adduser grader`
3. Create *grader* file in *sudoers.d* folder and insert the following line

    > grader ALL=(ALL:ALL) ALL

4. In local machine, generate encryption key with `$ ssh-keygen -f ~/.ssh/linuxServer.rsa`
5. Log in remote server as *ubuntu* and create file *authorized_keys* with `$ touch /home/grader/.ssh/authorized_keys`
6. Copy content of the file in *~/.ssh/linuxServer.rsa.pub* to *authorized_keys*
7. Set permission to the keys by entering the following code

    > `$ sudo chmod 700 /home/grader/.ssh`
    > `$ sudo chmod 644 /home/grader/.ssh/authorized_keys`

8. Change owner from *ubuntu* to *grader* with `$ sudo chown -R grader:grader     /home/grader/.ssh`

9. Set PasswordAuthentication field to no to enforce key-based authentication
    > `$ sudo nano /etc/ssh/sshd_config`
10. Set PermitRootLogin field to no to disable ssh login for user
    > `$ sudo nano /etc/ssh/sshd_config`

11. Run `$ sudo service ssh restart`


## Security

### Firewall
1. Edit *Port* field in *sshd_config* file to 2200
    > `$ sudo nano /etc/ssh/sshd_config`
2. Go to server instance in lightsail site
3. Select Networking tab
4. Add Custom Application with TCP Protocol at port 2200 to Firewall
5. Add Custom Application with UDP Protocol at port 123 to Firewall
6. Remove port 20 from this firewall
7. Run `$ sudo service ssh restart`
8. Connect to user *grader* by entering the following code in command line
    > `$ ssh -i ~/.ssh/linuxServer.rsa -p 2200 grader@52.221.234.110`
9. Configure ufw to allow connection for port 2200, port 80 and port 123
    > `$ sudo ufw allow 2200/tcp`

    > `$ sudo ufw allow 80/tcp`

    > `$ sudo ufw allow 123/udp`
    
    > `$ sudo ufw enable`

## Package installation

1. `$ sudo apt-get update`
2. `$ sudo apt-get install python`
3. `$ sudo apt-get install python-pip`
4. `$ sudo pip install virtualenv`
5. `$ sudo apt-get install python-requests`
6. `$ sudo apt-get install python-oauth2client`
7. `$ sudo apt-get install python-psycopg2`
8. `$ pip install Flask`
9. `$ pip install httplib2 sqlalchemy`
10. `$ sudo apt-get install libpq-dev python-dev`
11. `$ sudo apt-get install postgresql postgresql-contrib`

## Apache Configuration
1. Install Apache2
    > `sudo apt-get install apache2`

2. Install mod_wsgi
    > `sudo apt-get install python-setuptools libapache2-mod-wsgi`

3. Restart Apache
    > `sudo service apache2 restart`

4. Create directory in /var/www with `sudo mkdir catalog`
5. Git clone *item-catalog* from Linux-Serverlive branch to */var/www/catalog/*
    > `git clone https://github.com/Lancelee92/item-catalog.git`
6. Rename project folder to `item_catalog `
7. Rename main python file in project to *__init__.py*
8. Create a virtual host config file
    > `$ sudo nano /etc/apache2/sites-available/catalog.conf`
9. Insert the following code:

    ```
        <VirtualHost *:80>
            ServerName 52.221.234.110
            ServerAlias hostname 52.221.234.110.xip.io
            ServerAdmin admin@52.221.234.110
            WSGIDaemonProcess catalog python-path=/var/www/catalog:/var/www/catalog/venv/lib/python2.7/site-packages
            WSGIProcessGroup catalog
            WSGIScriptAlias / /var/www/catalog/catalog.wsgi
            <Directory /var/www/catalog/item_catalog/>
                Order allow,deny
                Allow from all
            </Directory>
            Alias /static /var/www/catalog/item_catalog/static
            <Directory /var/www/catalog/item_catalog/static/>
                Order allow,deny
                Allow from all
            </Directory>
            ErrorLog ${APACHE_LOG_DIR}/error.log
            LogLevel warn
            CustomLog ${APACHE_LOG_DIR}/access.log combined
        </VirtualHost>

    ```
10. Enable the virtual host with `$ sudo a2ensite catalog`

11. Create *catalog.wsgi* file in /var/www/catalog/ and insert the following       code

    ```
        import sys
        import logging
        logging.basicConfig(Stream=sys.stderr)
        sys.path.insert(0, "/var/www/catalog/")

        from item_catalog import application
        application.secret_key = 'super_secret_key'

    ```
12. Restart Apache2 with `sudo service apache2 restart`

## PostgreSQL configuration

1. Login with `sudo su - postgres`
2. Connect PostgreSQL shell with `$ psql`
3. Create new user with password
    
    > `# CREATE USER catalog WITH PASSWORD 'password';`

4. Allow Catalog user to *CREATEDB*
    
    > `# ALTER USER catalog CREATEDB;`

5. Create *catalog* database with *catalog* user

    > `# CREATE DATABASE catalog WITH OWNER catalog;`

6. Connect to *catalog* database with `# \c catalog`

7. Revoke all rights from public with 

    > `# REVOKE ALL ON SCHEMA public FROM public;`

8. Grant permission to catalog user

    > `# GRANT ALL ON SCHEMA public TO catalog;`

9. Exit with `# \q`

10. Edit create_engine line in *database_setup.py* and *__init__.py*

    ~~create_engine('sqlite:///itemcatalog.db')~~
    >  `create_engine('postgresql://catalog:password@localhost/catalog')`

11. Run `$ python /var/www/catalog/item-catalog/database_setup.py`

> `$ ssh -i ~/.ssh/linuxServer.rsa -p 2200 grader@52.221.234.110` to connect      server

> Use `$ sudo tail /var/log/apache2/error.log` to check log

# Item-Catalog

## **Guide** 

### Set up vagrant
1. go [virtualbox.org](https://www.virtualbox.org)
2. download and install virtualbox for your operating systems
3. go [vagrantup.com](https://www.vagrantup.com/downloads.html)
4. download and install for your operating systems
5. go to [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm)
6. download Vagrantfile in vagrant directory
7. Run `` $ vagrant init `` in item-catalog folder
8. Replace Vagrantfile in the item-catalog folder
9. Run this code to start vagrant

   `` $ vagrant up ``   
   `` $ vagrant ssh ``  

### Database
1. Run `` & python database-setup.py `` to set up the database
2. Run `` & python catalog.py `` to start the site
3. Browse the site at [http://localhost:5000](http://localhost:5000)

### JSON Api
Click on the following link to access the JSON Api. 
For Item List APi, the link used depends on the category id
`` localhost:5000/categories/<int:category_id>/itemlist/JSON ``

- [Home Page Api](http://localhost:5000/JSON)
- [Author List Api](http://localhost:5000/authorlist/JSON)
- [Recently Added Api](http://localhost:5000/topNewItem/JSON)
- [Item List Api](localhost:5000/categories/1/itemlist/JSON)


