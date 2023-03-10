🌱 I’m currently learning **Django,Postgresql**

<h3 align="left">Connect with me:</h3>
<p align="left">
</p>

<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/> </a> <a href="https://www.docker.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker" width="40" height="40"/> </a> <a href="https://www.postgresql.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original-wordmark.svg" alt="postgresql" width="40" height="40"/> </a> <a href="https://postman.com" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/getpostman/getpostman-icon.svg" alt="postman" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>

It is necessary to implement a network model for the sale of electronics.
The network should be a hierarchical structure of 3 levels:

Factory;
Retail network;
Individual entrepreneur.
Each link in the network refers to only one equipment supplier (not necessarily the previous one in the hierarchy). It is important to note that the hierarchy level is determined not by the name of the link, but by the relationship to the other elements of the network, i.e. the factory is always at level 0, and if the retail network refers directly to the factory, bypassing the other links, its level is 1.

Each link of the network must have the following elements:

Title;
Contacts:
Email;
A country;
City;
Street;
House number;
Products:
Name;
Model;
Release date of the product on the market;
Provider (the previous network object in the hierarchy);
Debt to the supplier in monetary terms, up to kopecks;
Creation time (filled in automatically when created).
Make a conclusion in the admin panel of the created objects

On the network object page, add:

link to "Supplier";
filter by city name;
"admin action" that clears the debt owed to the supplier from the selected objects.