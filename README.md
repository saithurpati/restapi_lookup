# restapi_lookup

Craft demo 

lookup folder contains python code to get country name by providing country code 

Note: pip3 install -r requirments.txt

E.g: Python3 lookup.py --countryCode=AU,IN,AE

restapi Folder containes dockerfile and restapi code 
create docker image and push it to dockerhub and then update image path in 

deployment.yml file under k8s 

k8s --> Folder contains deployment and service yml files

kubectl apply -f deployment.yml 
kubectl apply -f service.yml 
