# Cenário: Buscar usuários
from locust import HttpUser, task, between

class GetUsers(HttpUser):
    wait_time = between(1, 2)

    @task
    def get_users_page(self):
        self.client.get("/users?page=1")
