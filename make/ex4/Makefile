SRC = main.cpp
EXEC = a.out
IMAGE_NAME = cpp-demo-app

.PHONY: all docker-image run clean

all: docker-image

docker-image: $(EXEC)
	@docker build -t $(IMAGE_NAME) .
	@rm $(EXEC)

$(EXEC): $(SRC)
	@g++ -o $(EXEC) $(SRC)

run:
	@docker run --rm $(IMAGE_NAME)

clean:
	@docker rmi $(IMAGE_NAME) || true
