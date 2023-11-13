# pedia-middleware
This is a middleware application for handling integration of variant analysis tools like VarFish with PEDIA (Prioritization of Exome data by image analysis). It can be independently embeded 
as an iFrame in the Variant Analysis tool. It displays a view that takes the patient image as input and submits it to the GestaltMatcher service. It then retrieves the gene list with the 
gestalt scores from the GestaltMatcher service and posts it back to the parent window (i.e. the tool embedding this application) 

To run the django application, first create an enviornment and activate it:
<code>
conda create --name pedia_mid_env
conda activate pedia_mid_env
</code>

Then install the requirements:
<code>
pip install django
pip install django_rest_framework
</code>

Start the application server on a different port than Varfish, for example on port 7000:
<code>
python manage.py runserver 7000
</code>

To run the GestaltMatcher service,follow the steps mentioned here:

https://github.com/igsb/GestaltMatcher-Arc/tree/service#gestaltmatcher-rest-api
