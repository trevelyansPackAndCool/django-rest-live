Changelog
=========
0.8.0 (2025-01-29)
------------------
* Added Channels 4 and Django 4.2+ / 5.0 support
* Added `return_all` subscription option to receive full queryset on updates
* Added AuthenticationFailed exception handling in permission checks
* Added support for dict-based querysets (array compatibility)
* Paginate subscription querysets
* Use Django's ASGIRequest for better compatibility
* Updated minimum requirements: Python 3.8+, Django 4.2+, Channels 4+, DRF 3.14+

0.7.0 (2022-02-13)
------------------
* Support for database deletes

0.3.0 (2020-10-23)
------------------
* Improve efficiency by remove a blanket signal connect
* Fix extraneous context switching 

0.2.2 (2020-09-13)
------------------
* Initial working version 
