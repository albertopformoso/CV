create:
	make build
	docker-compose -f ./docker/docker-compose.yaml up -d

remove:
	docker-compose -f ./docker/docker-compose.yaml down

build:
	docker build . --tag cv_app --file ./docker/Dockerfile

secret:
	kubectl apply -f ./kube/app_secret.yaml

deployment:
	@if [ -z $(docker images | grep 'cv_app') ]; then\
		make build;\
	fi
	make secret
	kubectl apply -f ./kube/app_deployment.yaml

show:
	minikube service pyapp-service
	minikube service list

delete:
	kubectl delete -f ./kube/app_secret.yaml
	kubectl delete -f ./kube/app_deployment.yaml