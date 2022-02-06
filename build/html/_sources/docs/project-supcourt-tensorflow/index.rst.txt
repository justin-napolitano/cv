TensorFlow Voting Behavior Predictions
=======================================================


Description
----------------------

* The application is written python and uses the TensorFlow api to train an algorithm that predicts the outcome of court cases.
* Data is collected from `The Supreme Court Database <http://scdb.wustl.edu/about.php?s=3>`_
* The predicted outcomes of the cases proved to be correct about 80% of the time when tested against historical data.  
* Thus it appears that justices vote according to personal preferences towards political issue areas. 


Links
------
* `Github <https://github.com/justin-napolitano/Supreme-Court-Predictions>`_
* `The Supreme Court Datase <http://scdb.wustl.edu/about.php?s=3>`_
* `Sphinx Documentation <https://court-behavior.io/ml/ml-abstract.html>`_



How to Improve
-------------------

* Import this data into :ref:`The US Supreme Court Metadata Graph<metadatagraph>`.
* Train the algorithm to correlate outcome with as many other variables as possible.


Training Features
-------------------

.. toctree::
   :maxdepth: 2
   :caption: Training Features:

   training-features.rst

Python Modules
---------------

.. toctree::
   :maxdepth: 2
   :caption: Modules:
   
   /autoapi/SupremeCourtPredictionsCase/index.rst
   /autoapi/SupremeCourtPredictionsJustice/index.rst
  