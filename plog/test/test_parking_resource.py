def test_get_parking(client):
    response = client.get("/api/v1/park")
    assert response.status_code == 200
    print(response.text)


def test_add_parking(client):
    data = {"driver": "Itai", "car_id": 1, "park_spot_id": 20}
    response = client.post("/api/v1/park", data=data)
    assert response.status_code == 200
    print(response.text)

