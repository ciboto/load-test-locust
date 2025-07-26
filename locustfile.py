from locust import HttpUser, task, between

class PublicApiUser(HttpUser):
    wait_time = between(1, 3)  # tempo entre requisições (simula usuários reais)

    @task(2)  # mais peso → executa com mais frequência
    def get_post(self):
        self.client.get("/posts/1")

    @task(1)
    def create_post(self):
        payload = {
            "title": "Teste de carga",
            "body": "Conteúdo gerado pelo Locust",
            "userId": 1
        }
        self.client.post("/posts", json=payload)
