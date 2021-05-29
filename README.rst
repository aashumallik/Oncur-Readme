medico
======

consultation platform
.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style


Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html


Initial Setup
-------------

TODO: Flesh out the procedure more.

Virtual Environments
^^^^^^^^^^^^^^^^^^^^

First we need to setup a virtual environment before you can do anything.
So go ahead and open your terminal, assuming you're on a Linux/Mac system,
and type `sudo pip install virtualenvwrapper`. It remains the most
convenient way to install dependencies. Make sure you have Python 3.x!

Follow the instructions at the virtualenvwrapper online docs and if you
have a `.bashrc` or similar, add any commands they ask you to. If all went
well, you should be able to run the commands -:

* `mkvirtualenv -a . <name of environment` (what `-a .` does is that it
forces the terminal to enter your project directory, assuming that's where
you are when you run this command, whenever you activate the environment).

* `workon <name of environment>` (for when you need to activate it)

* `deactivate` (for when you want to deactivate it and move to another
environment).

Virtualenvs allow you to separate your package installs so that they don't
mix with each other. Different sets of installs for different projects.

Installing Requirements
^^^^^^^^^^^^^^^^^^^^^^^

Once you're done with environment setup, head over to the `requirements`
directory and run the command `pip install -r local.txt`. You would
substitute the `production.txt` file for when you run the installation
procedure on your production server. Any package changes need to be
recorded in this file for future installs. Think of it as an easy first
step to automate your build and installation pipeline.

Database Setup
^^^^^^^^^^^^^^

TODO: Add database setup instructions.

Running Localserver
^^^^^^^^^^^^^^^^^^^

Once Django has been installed, you can fire up a terminal window and run
the command `python manage.py runserver`. For administrator access, run
the command `python manage.py createsuperuser` and follow the
instructions. As you can see, the `manage.py` is important in Django land.
It is used to run management commands.

With the superuser credentials you can login on
http://localhost:8000/admin to access the admin dashboard. You've made
your first step into the app!

Basic Commands (Stuff from earlier readme)
------------------------------------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Type checks
^^^^^^^^^^^

Running type checks with mypy:

::

  $ mypy medico

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ pytest

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html




Email Server
^^^^^^^^^^^^

In development, it is often nice to be able to see emails that are being sent from your application. If you choose to use `MailHog`_ when generating the project a local SMTP server with a web interface will be available.

#. `Download the latest MailHog release`_ for your OS.

#. Rename the build to ``MailHog``.

#. Copy the file to the project root.

#. Make it executable: ::

    $ chmod +x MailHog

#. Spin up another terminal window and start it there: ::

    ./MailHog

#. Check out `<http://127.0.0.1:8025/>`_ to see how it goes.

Now you have your own mail server running locally, ready to receive whatever you send it.

.. _`Download the latest MailHog release`: https://github.com/mailhog/MailHog/releases

.. _mailhog: https://github.com/mailhog/MailHog



Deployment
----------

The following details how to deploy this application.
The application is deployed on Heroku





