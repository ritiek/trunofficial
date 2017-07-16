Trunofficial Documentation
***************************
.. module:: Trunofficial

This is the documentation for trunofficial - unofficial API to the Truecaller phone number search

A quick start intro with usage examples is available in the `README <http://github.com/ritiek/trunofficial/blob/master/README.rst>`_

Development / Source code / Bug reporting: `github.com/ritiek/trunofficial/
<https://github.com/ritiek/trunofficial/>`_


Trunofficial Objects
====================

Trunofficial objects relate to information fetched from the Truecaller databse.  They hold metadata such as
*owner name*, *id*, *provider* and *trace*

Trunofficial Sub-Objects
========================

Phone objects relate to information to the phone number. They hold
phone-specific data such as *phone number*, *number type*, *country code* and *dial code*.


Creating Truonfficial Objects
=============================

Create a Trunofficial object using the :func:`trunofficial.search` function, giving a phone number as the argument.


.. function:: trunofficial.search(number)


    Creates a new Trunofficial object.

    :param number: Phone number of the user
    :type url: str

Example::

    import trunofficial
    owner = trunofficial.search("2024561111")

Trunofficial Attributes
-----------------------

Once you have created a Trunofficial object using :func:`trunofficial.search`, several data
attributes are available

.. attribute:: Trunofficial.id

    The id of the owner (*str*)

.. attribute:: Trunofficial.name (*str*)

    The name of the owner

.. attribute:: Trunofficial.score

    The score of the owner (*str*)

.. attribute:: Trunofficial.access

    The public accessibility of the database (*str*)

.. attribute:: Trunofficial.enhanced

    The availibility of enhanced information (*str*)

.. attribute:: Trunofficial.internet_address

    The publicly accessible information like e-mail (*int*)

.. attribute:: Trunofficial.badges

    The badges earned by the owner (*str*)

.. attribute:: Trunofficial.tags

    The tags earned by the owner (*str*)

.. attribute:: Trunofficial.sources

    The sources available of the owner (*str*)

.. attribute:: Trunofficial.provider

    The phone number provider (*str*)

.. attribute:: Trunofficial.trace

    The available trace of the owner (*str*)

.. attribute:: Trunofficial.sourcestats

    The available source stats of the owner (*str*)

An example of accessing this owner metadata is shown below::

    import trunofficial
    owner = trunofficial.search("2024561111")
    print(owner.id)
    print(owner.name)
    print(owner.score)
    print(owner.access)
    print(owner.enhanced)
    print(owner.internet_address)
    print(owner.badges)
    print(owner.tags)
    print(owner.sources)

Which will result in this output::

    uLByRJydv5fh+1nHPzemqg==
    Obama
    0.8
    PUBLIC
    True
    []
    []
    [u'4', u'51']
    []


Phone Objects
=============

.. class:: trunofficial.Phone

After you have created a :class:`Trunofficial` object using :func:`search`, you
can then access the phone information by using

.. attribute:: Trunofficial.phone


Phone Attributes
----------------

    A Phone object can be used to access the following attributes


.. attribute:: Phone.number

    The phone number of the owner formatted in e164 format

.. attribute:: Phone.numbertype

    The type of number of the owner

.. attribute:: Phone.national

    The phone number of the owner formatted in national format

.. attribute:: Phone.dialcode

    The dial code prefix of the phone number

.. attribute:: Phone.countrycode

    The country code s depicted by the phone number

.. attribute:: Phone.carrier

    The carrier of the phone number

.. attribute:: Phone.spamscore

    The spam score of the owner. Higher the score, the greater the spammer.

.. attribute:: Phone.spamtype

    The label of the spam type

.. attribute:: Phone.phonetype

    The label of the phone type

An example of accessing Phone attributes::

    >>> import trunofficial
    >>> owner = trunofficial.search("2024561111")
    >>> mobile = owner.number
    >>> mobile.phone
    u'+912024561111'
    >>> mobile.numbertype
    u'FIXED_LINE'
    >>> mobile.carrier
    u'BSNL'


Address Objects
===============

.. class:: trunofficial.Address

After you have created a :class:`Trunofficial` object using :func:`search`, you
can then access the address information by using

.. attribute:: Trunofficial.addresss

Address Attributes
------------------

    An Address object can be used to access the following attributes


.. attribute:: Address.area

    The area as the phone number depicts

.. attribute:: Address.city

    The city as the phone number depicts

.. attribute:: Address.countrycode

    The country code as depicted by the location

.. attribute:: Address.timezone

    The time zone as depicted by the location

.. attribute:: Address.type

    The label of the address type

An example of accessing Address attributes::

    >>> import trunofficial
    >>> owner = trunofficial.search("2024561111")
    >>> house = owner.address
    >>> house.area
    u'Pune, Maharashtra'
    >>> house.city
    u'Pune, Maharashtra'
    >>> house.timezone
    u'GMT+05:30'

