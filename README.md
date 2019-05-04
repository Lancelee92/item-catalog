# Linux-Server

## Lightrail setup
1. Download Lightrail default keys.
2. mv ~/Download/LightsailDefaultKey-ap-southeast-1.pem ~/.ssh/
3. chmod 700 ~/.ssh/
4. chmod 600 ~/.ssh/LightsailDefaultKey-ap-southeast-1.pem
5. Connect to remote Server using ssh ubuntu@server -i ~/.ssh/LightsailDefaultKey-ap-southeast-1.pem

## User Management
1. Connect to user *grader* by entering `ssh -i ~/.ssh/linuxServer.rsa -p 2200 grader@52.221.234.110` in command line

## Security
1. 

#Package installation
1. `sudo apt-get update`
2. `sudo apt-get install python-requests`
3. `sudo apt-get install python-oauth2client`
4. `sudo apt-get install python-psycopg2`
5. `sudo apt-get install postgresql postgresql-contrib`
6. `sudo apt-get install libpq-dev python-dev`
7. `sudo apt-get install libpq-dev python-dev`
8.

#####Use sudo tail /var/log/apache2/error.log to check log

# item-catalog

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


