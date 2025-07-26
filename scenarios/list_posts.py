# Cenário: Listar todos os posts
from locust import HttpUser, task, between

class ListPosts(HttpUser):
    wait_time = between(1, 2)

    @task
    def list_all_posts(self):
        self.client.get("/posts")
