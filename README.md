# My Portfolio
## Here is how to run it locally
(Les instructions en français suivent)

* Start by installing [docker-compose](https://docs.docker.com/compose/install/linux/) if you don't have it already
* Clone my repository
* Run `docker-compose up --build` in the directory and watch everything get installed
* [Optional] if you would like to modify the code and get realtime modifications, use `docker-compose -f dev-docker-compose.yaml up --build` instead
* After the first build, shut it down with `ctrl+C` and run the command a second time (the first time the FastApi won't be able to connect to the MySQL server)
* go to the [FastApi swagger interface](https://docs.docker.com/compose/install/linux/) on a browser
* From there create an access key by clicking on `Create One Access` then `Try it out`, filling out the JSON object and clicking execute
* Make sure the response code is `200`
* You can now go to [localhost](http://0.0.0.0/) to enter the code and see the website

# Mon portfolio
## Voici comment vous pouvez lancer le site localement

* Installez [docker-compose](https://docs.docker.com/compose/install/linux/)
* Cloner mon repertoire
* Lancer `docker-compose up --build` dans le dossier de mon repertoire
* [Optional] si vous voulez pouvoir modifier mon code et voir les changements instantanément faites `docker-compose -f dev-docker-compose.yaml up --build` au lieu
* Faite `ctrl+C` pour l'areter et lancer la comande de l'étape précédente une deuxième fois (si vous ne faites pas cela, le FastApi ne serra pas connecté au MySQL)
* Rendez-vous à [ l'interface swagger FastApi](https://docs.docker.com/compose/install/linux/) sur votre furteur
* Clicker sur `Create One Access` et ensuite `Try it out`, remplisez l'objet JSON et clicker execute
* Rendez-vous [localhost](http://0.0.0.0/), entrez votre code et vous verrez le site