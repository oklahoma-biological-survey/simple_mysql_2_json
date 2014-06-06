simple MySQL to json
======================

Simple script to access remote mysql and turn into json.


### Python Environment Install
<pre><code>
    $ easy_install pip <br>
    $ pip install virtualenv <br>
    $ virtualenv virtpy <br>
    $ source virtpy/bin/activate <br>
    $ pip install -r requirement.txt <br>
</code></pre>

###  Setup and Run 
<pre><code> 
        $ cp config.py.template config.py <br>
        # edit config.py and set host,username,password <br>
        $ python mysql_cy <br>
</code></pre>


### Result
<pre><code>
[
    {
        "county": "CHEROKEE",
        "number": "1",
        "habitat": null,
        "family": "SCINCIDAE",
        "month": "APR",
        "citatin": null,
        "museum": null,
        "TIMESTAMP": "2013-05-02T15:44:50Z",
        "comname": "COAL SKINK",
        "species": "ANTHRACINUS",
        "obsnum": "18466",
        "obsvr": "MAREK, S. AND BUTLER, R.",
        "year": "2013",
        "remarks": "COUNTY RECORD. ADULT MALE",
        "genus": "EUMECES",
        "local": "LAKE EUFAULA STATE PARK",
        "class": "REPTILIA",
        "day": "20"
    },
    {
        "Sample":"Other records removed"
    },
    {
        "county": "LOVE",
        "number": "1",
        "habitat": null,
        "family": "COLUBRIDAE",
        "month": "MAY",
        "citatin": null,
        "museum": null,
        "TIMESTAMP": "2014-05-12T15:11:53Z",
        "comname": " NIGHT SNAKE",
        "species": "TORQUATA JANI",
        "obsnum": "18467",
        "obsvr": "MIKE MALEVICH",
        "year": "2014",
        "remarks": "HAVE PHOTO",
        "genus": "HYPSIGLENA",
        "local": "HICKORY CREEK WILDLIFE MANAGEMENT AREA",
        "class": "REPTILIA",
        "day": "11"
    }
]
</code></pre>
