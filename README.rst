State of the Map Japan 2014 website being built by OpenStreetMap Foundation Japan, based on symposion fork that is used for PyCon JP 2014.
That is because I18N and japanese translation.

PyConJP 2014 website was built by forking PyCon 2014 website code.

PyCon 2014 website being built by Caktus Consulting Group, based on symposion.

Rather than use this as the basis for your conference site directly, you should
instead look at https://github.com/pinax/symposion which was designed for reuse.

PyCon 2014 is built on top of Pinax Symposion but may have customizations that
will just make things more difficult for you.

Installation instructions are in this README.  There's more documentation
at https://readthedocs.org/projects/pycon/.

To get running locally
----------------------

* Install dependency packages. for Ubuntu 12.04 and 14.04

    $ misc/setup_environment.sh

  If you run it on 14.04 and deriveratives, you should work around;

    $ sudo ln -s /usr/include/freetype2 /usr/local/include/freetype

* Create a new virtualenv and activate it::

    $ virtualenv env/sotmjp-website
    $ . env/sotmjp-website/bin/activate

* Install the requirements for running and testing locally::

    $ pip install -r requirements/dev.txt

  (For production, install -r requirements/project.txt).

* Copy ``sotmjp/settings/local.py-example`` to ``sotmjp/settings/local.py``.
* Edit ``sotmjp/settings/local.py`` according to the comments. Note that you
  `will` have to edit it; by default everything there is commented out.

* Setup the database::

  for development just do:

    $ ./init_db.sh

  for staging/production

    $ createdb sotmjp2014

* Create a user account::

    $ ./manage.py createsuperuser

* If you have ssh access to the staging server, copy the database and media::

    $ fab staging get_db_dump:sotmjp2014_staging
    $ fab staging get_media

  Change ``sotmjp2014`` in that first command to the name of your local database.

* Run local server::

    $ ./manage.py runserver

For production
--------------

* Start with instructions above, except:

  * Install requirements from requirements/project.txt instead of requirements/dev.txt
  * Stop when you get to `Run local server`

* Edit ``sotmjp/settings/local.py`` to make sure DEBUG=False.
* Add an appropriate ALLOWED_HOSTS setting (https://docs.djangoproject.com/en/1.5/ref/settings/#std:setting-ALLOWED_HOSTS)
* Install ``lessc`` (Go to http://lesscss.org and search for "Server-side usage")
* Pre-compress everything by running::

    $ ./manage.py compress --force

  That will write compressed css and js files under site_media
* Gather the static files::

    $ ./manage.py collectstatic --noinput

* Build site css file

    $ ./build-css.sh

* Arrange to serve the site_media directory as ``/2014/site_media/whatever``.
  E.g. ``site_media/foo.html`` would be at ``/2014/site_media/foo.html``.
* Arrange to serve the wsgi application in ``symposion/wsgi.py`` at ``/``, running
  with the same virtualenv (or equivalent).  It will only handle URLs
  starting with ``/2014`` though, so you don't have to pass it any other requests.

To run staging
--------------

* Use Vagrant to prepare environment

* Setup same for production but except;

  $ misc/start_staging.sh


To run tests
------------

::

    python manage.py test

More documentation
------------------

There's more documentation under ``docs/``.
