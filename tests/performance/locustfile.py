from locust import HttpUser, task


class ProjectPerfTest(HttpUser):

    @task()
    def index(self):
        self.client.get("/")

    @task()
    def summary(self):
        login_data = {"email": "john@simplylift.co"}
        self.client.post('/showSummary', data=login_data)

    @task()
    def booking(self):

        self.client.get('/book/Spring Festival/Simply Lift')

    @task()
    def purchase(self):
        booking_data = {"club": "Simply Lift",
                        "competition": "Spring Festival",
                        "places": "10"}
        self.client.post('/purchasePlaces', data=booking_data)

    @task
    def logout(self):
        self.client.get('/logout')
