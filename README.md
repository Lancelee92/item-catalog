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


