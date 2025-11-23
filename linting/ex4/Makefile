.PHONY: linting

linting: 
	docker run --rm \
		-e SONAR_HOST_URL="http://sonarqube:9000" \
		-e SONAR_SCANNER_OPTS="-Dsonar.projectKey=reminder" \
		-e SONAR_TOKEN="squ_e543af8a236acedbbfa97a50fab92de746a76e9b" \
		--network sonar-net \
		-v .:/usr/src \
		-u $(id -u):$(id -g) \
		sonarsource/sonar-scanner-cli
