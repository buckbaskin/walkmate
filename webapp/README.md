# webapp

This folder contains the contents necessary to run the web server for the Walkmate wb application.

## static/

The static folder contains "static" resources such as Javascript and CSS.

## templates/

The templates folder contains HTML-like templates that the webserver fills out and sends to the client.

## ```__init__.py```

The ```__init__.py``` file creates the webapp.server object. This is used to run the application (```server.run()```) and setup routes for the API (```@server.route()```)

## ```api.py```

This is the file that the ```__init__.py``` file uses to configure the API for the server side of the application.
