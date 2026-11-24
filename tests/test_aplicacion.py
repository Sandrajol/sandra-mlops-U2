import historial
from app import app
from modelo import clasificar_estado


def test_cinco_categorias():
    casos = [
        (0, 0, 0, "NO ENFERMO"),
        (2, 3, 4, "ENFERMEDAD LEVE"),
        (2, 3, 8, "ENFERMEDAD AGUDA"),
        (2, 40, 4, "ENFERMEDAD CRÓNICA"),
        (3, 100, 9, "ENFERMEDAD TERMINAL"),
    ]

    for cantidad, dias, intensidad, esperado in casos:
        assert clasificar_estado(cantidad, dias, intensidad) == esperado


def test_reporte_vacio(tmp_path, monkeypatch):
    monkeypatch.setattr(
        historial,
        "ARCHIVO",
        tmp_path / "predicciones.csv",
    )

    with app.test_client() as cliente:
        respuesta = cliente.get("/api/reporte")

    assert respuesta.status_code == 200
    reporte = respuesta.get_json()

    assert reporte["totales_por_categoria"] == {
        categoria: 0 for categoria in historial.CATEGORIAS
    }
    assert reporte["ultimas_cinco"] == []
    assert reporte["fecha_ultima"] is None


def test_registro_y_reporte(tmp_path, monkeypatch):
    monkeypatch.setattr(
        historial,
        "ARCHIVO",
        tmp_path / "predicciones.csv",
    )

    with app.test_client() as cliente:
        for dias in range(100, 106):
            respuesta = cliente.post(
                "/",
                data={
                    "cantidad_sintomas": 3,
                    "dias_sintomas": dias,
                    "intensidad": 9,
                },
            )
            assert respuesta.status_code == 200
            assert "ENFERMEDAD TERMINAL" in respuesta.get_data(as_text=True)

        respuesta = cliente.get("/api/reporte")

    assert respuesta.status_code == 200
    reporte = respuesta.get_json()

    assert reporte["totales_por_categoria"] == {
        categoria: 6 if categoria == "ENFERMEDAD TERMINAL" else 0
        for categoria in historial.CATEGORIAS
    }
    assert len(reporte["ultimas_cinco"]) == 5
    assert [
        int(registro["dias_sintomas"])
        for registro in reporte["ultimas_cinco"]
    ] == [105, 104, 103, 102, 101]
    assert reporte["fecha_ultima"] == reporte["ultimas_cinco"][0]["fecha"]
    assert reporte["fecha_ultima"] is not None