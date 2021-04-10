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

Example RestAPI URL:

Health: http://127.0.0.1:<port>/health

Diag: http://127.0.0.1:<port>/diag
  
convert: http://127.0.0.1:<port>/convert --> method is POST
under post Method body send countryname as form-data
E.g: 
![image](https://user-images.githubusercontent.com/43188052/114275832-0fbb4a80-99f2-11eb-90fc-52bc5cbd9949.png)

