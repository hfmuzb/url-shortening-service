run:
	docker compose up -d app db

build:
	docker compose up -d --build app db

stop:
	docker compose down

restart:
	docker compose down
	docker compose up -d --build app db
