# Django Food App

`DjangoFoodApp` is a Django app with PostgresQl database.



On startup Django superuser is created with credentials passed in env variables defined in `.env.example`
<hr>

## How to try it out

The project is prepared to be run locally in docker using docker-compose.

1. Install, setup and run [Docker Desktop](https://www.docker.com/)
2. Open Terminal and `cd` to `DjangoFoodApp`
3. run `make up` -this command will build and run Docker containers for:
   1. Webapp - on  http://0.0.0.0:8000
   3. PostgreSQL
4. Go to http://0.0.0.0:8000/food login using django superuser credentials: login: django_admin, password: example_password or register new user and login.
5. Click `Add Item` and add example following items:
```
  Item name: Pizza
  Item desc: Cheesy Pizza,
  Item price: 20,
  Item image: https://ocdn.eu/pulscms-transforms/1/-vxk9kqTURBXy8wNmQzYjQ5YzA2MzRiYTVkZTg2N2M3NjFiYjBjZGFmNC5qcGVnk5UDAB_NA-jNAjKTBc0DFM0BvJMJpmU0ZjU3ZQaBoTAB/pizza-margherita.jpg
```
```
  Item name: Burger
  Item desc: Cheesy Burger
  Item price: 10
  Item image: https://www.unileverfoodsolutions.pl/dam/global-ufs/mcos/nee/poland/recipe/italian-burger/wloski-burger_1611135467.jpg
```
```
  Item name: Burrito,
  Item desc: Fluffy Burrito,
  Item price: 30,
  Item image: https://bi.im-g.pl/im/e7/5c/18/z25543655IER,Burrito.jpg
```
6. To stop all containers press `Ctrl+C` in the Terminal
7. To remove created volumes along with the containers run `make clean`

<hr>

Thanks for your visit, feel free to contact me on [LinkedIn](https://www.linkedin.com/in/daniel-pyrzanowski-77503b251)