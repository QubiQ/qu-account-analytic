.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
	:target: http://www.gnu.org/licenses/agpl
	:alt: License: AGPL-3

============================
Analytic Tag Product Partner
============================

Generates analytic tags on Sale Orders, Purchase Orders and Invoices from a product, a customer and a provider.


Installation
============

Just install.


Configuration
=============

Set default codes for your products and references for your partners.


Usage
=====

Create a Sale Order/Purchase Order/Invoice, add lines and fill the product and the new fields "Customer" and "Provider". The module will search for/create an analytic tag following the next format: [product_code]-[customer_reference][provider_reference].

The module works in conjunction with the "Inter Company Rules". 


Bug Tracker
===========

Bugs and errors are managed in `issues of GitHub <https://github.com/QubiQ/qu-server-tools/issues>`_.
In case of problems, please check if your problem has already been
reported. If you are the first to discover it, help us solving it by indicating
a detailed description `here <https://github.com/QubiQ/qu-server-tools/issues/new>`_.

Do not contact contributors directly about support or help with technical issues.


Credits
=======

Authors
~~~~~~~

* QubiQ, Odoo Community Association (OCA)


Contributors
~~~~~~~~~~~~

* Xavier Piernas <xavier.piernas@qubiq.es>
* Valentín Vinagre <valentin.vinagre@qubiq.es>


Maintainer
~~~~~~~~~~

This module is maintained by QubiQ.

.. image:: https://pbs.twimg.com/profile_images/702799639855157248/ujffk9GL_200x200.png
   :alt: QubiQ
   :target: https://www.qubiq.es

This module is part of the `QubiQ/qu-server-tools <https://github.com/QubiQ/qu-server-tools>`_.

To contribute to this module, please visit https://github.com/QubiQ.