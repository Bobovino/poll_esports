pip freeze >requirements.txt

docker images #List images
docker ps -a #List containers

docker rmi -f IMAGE_ID
docker rm -f CONTAINER_ID

#restart docker images and containers
docker stop $(docker ps -aq)
docker rm $(docker ps -aq)
docker rmi $(docker images -q)
docker-compose up --build

docker stop $(docker ps -aq)
docker rm $(docker ps -aq)
docker-compose build web 
docker-compose up

docker-compose exec web python manage.py createsuperuser


docker run -it --entrypoint /bin/bash poll_esports-web        

python manage.py makemigrations
python manage.py migrate
python manage.py startapp taskapp

#Empezar terminal del container
docker exec -it web /bin/sh
./manage.py shell

from polling_app.models import RegionsModel

records = RegionsModel.objects.all()
for record in records:
    print(record.region)

#Execute tasks
from newapp.tasks import tp1, tp2, tp3, tp4
tp1.delay()
tp2.delay()
tp3.delay()
tp4.delay()

#Task grouping
from newapp.tasks import tp1, tp2, tp3, tp4
from celery import group
task_group= group(tp1.s(), tp2.s(), tp3.s(), tp4.s())
task_group.apply_async()

#Task chaining
from newapp.tasks import tp1, tp2, tp3, tp4
from celery import chain

task_chain=chain(tp1.s(), tp2.s(), tp3.s())
task_chain.apply_async()


chmod +x ./entrypoint.sh