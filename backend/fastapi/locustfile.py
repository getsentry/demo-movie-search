from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def hello_world(self):
        # self.client.get("api/")
        self.client.get("api/shows/")
        # self.client.get("api/persons/")

    @task(3)
    def view_items(self):
        for item_id in range(5):
            self.client.get(f"api/shows/{1234+item_id}")

    @task
    def search_items(self):
        self.client.get("api/shows/?q=scorsese")
        self.client.get("api/shows/6112")

    def on_start(self):
        # self.client.post("/login", json={"username":"foo", "password":"bar"})
        pass