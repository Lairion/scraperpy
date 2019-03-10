==============
Allo.ua Scraper Hints
==============
---------------

* `Installation`_
* `Create database`_
* `Usage`_
* `Display`_


---------------

---------------

============
Installation
============

Clone the repo:

.. code-block:: bash

    $ git clone https://github.com/Lairion/MyScraper.git

Then run install packages using pip:

.. code-block:: bash

    $ pip install -r req.txt

-----------------

=====
Create database
=====

First, need create db for the task, I have script for this. 
You need run script for this and input name db (only name, don't use '.sqlite3'):

.. code-block:: bash

   $ python create_db.py

-----------------

=====
Usage
=====

If you created db using 'create_db.py', you can continue to work.
Next you need run next script using this command and input name db:

.. code-block:: bash

   $ python scripts.py

-----------------


=====
Display
=====

If you want quick checking the db use this command and input name db:

.. code-block:: bash

   $ python display_data.py

-----------------