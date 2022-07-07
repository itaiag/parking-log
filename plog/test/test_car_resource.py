

def test_get_cars(client):
    response = client.get("/api/v1/car")
    assert response.status_code == 200
    print(response.text)


def test_get_car(client):
    response = client.get("/api/v1/car/1")
    print(response.text)
    assert response.status_code == 200


def test_add_car(client):
    response = client.post("/api/v1/car", data={"car_name": "Tesla"})
    print(response.text)
    assert response.status_code == 200


def test_delete_car(client):
    response = client.delete("/api/v1/car/3")
    print(response.text)
    assert response.status_code == 200
