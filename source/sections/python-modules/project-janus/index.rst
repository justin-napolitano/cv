.. _janus_graph_database:

################################################
JanusGraph Modules
################################################


Summary
----------
* An extension of the python-gremlin library. The modules is designed to work well with pandas DataFrames.
* The collection of functions are written to permit an asynchronous df.apply() across n threads to mimic transaction functionality of spark df’s without the overhead of running a local Spark cluster.
* Runner applications are also included that create example city and zip code graphs

Links
------
`GitHub <https://github.com/justin-napolitano/JanusGraphAPI>`_


Module Documentation
---------------------

.. toctree:: 
    :caption: JanusGraph Modules

    
    /autoapi/GremlinConnect/index.rst
    /autoapi/AddChildrenToRoot/index.rst
    /autoapi/AddIsRootProperty/index.rst
    /autoapi/AddSproutedProperty/index.rst
    /autoapi/TSubmit/index.rst
    /autoapi/Query/index.rst
    /autoapi/CleareGraph/index.rst


    