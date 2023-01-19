build:
	docker build --tag bot .

run: build
	docker run bot