.. _app_usage:

======================
Application Usage
======================

Send image through PEDIA-Middleware
=======================================

Follow these steps to send a facial image to GestaltMatcher through the PEDIA-Middleware application:

    * Launch the PEDIA Middleware server in a browser at http://127.0.0.1:7000
    * Click on :guilabel:`Choose File` button and select the image to send.
    * After choosing a file, the :guilabel:`Submit to GestaltMatcher` button is enabled, click to submit.
    * The image is sent to GestaltMatcher service API at http://127.0.0.1:5000/predict and a successful message or error message is displayed depending on the response received from GestaltMatcher service.

.. figure:: figures/image_submit.png
    :alt: Image submitted to GestaltMatcher.
    :width: 60%
    :align: center

    This figure shows the successful message on image submission to GestaltMatcher.
