# Cenário: Criar post com diferentes dados
from locust import HttpUser, task, between
import random

class CreateDynamicPost(HttpUser):
    wait_time = between(2, 4)

    @task
    def create_post_random(self):
        titles = ["Teste A", "Teste B", "Carga X", "Simulação Y"]
        payload = {
            "title": random.choice(titles),
            "body": "Gerado automaticamente para carga.",
            "userId": random.randint(1, 10)
        }
        self.client.post("/posts", json=payload)
