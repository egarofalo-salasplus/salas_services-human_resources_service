import requests
from django.shortcuts import render
from decouple import config
from .forms import ImputationForm
import os
import logging

# Configurar el logger
logger = logging.getLogger(__name__)

monday_base_url = "http://127.0.0.1:8000/monday"
salas_key = config("SALAS_API_KEY", default=os.getenv("SALAS_API_KEY"))
headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {salas_key}"
        }


def get_boards():
    response = requests.get(f"{monday_base_url}/boards",
                            headers=headers,
                            timeout=5000)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return {}


def get_items(board_id):
    params = {
        "board_id": str(board_id)
    }
    response = requests.get(f"{monday_base_url}/get-board-items",
                            params=params,
                            headers=headers,
                            timeout=5000)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return {}


def get_items_details(item_ids):
    response = requests.post(f"{monday_base_url}/get-column-values",
                             json=item_ids,
                             headers=headers,
                             timeout=5000)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return {}


def boards_view(request):
    form = ImputationForm()
    boards = get_boards()

    # Actualizar las opciones del formulario con los datos obtenidos
    form.fields["board"].choices = [(v, k) for k, v in boards.items()]

    if request.method == "POST":
        form = ImputationForm(request.POST)
        form.fields["board"].choices = [(v, k) for k, v in boards.items()]
        if form.is_valid():
            board_id = form.cleaned_data["board"]
            email = form.cleaned_data["email"]
            logger.info(f"Board ID: {board_id}")
            items = get_items(board_id)
            item_details = get_items_details(items)
            return render(
                request,
                "imputations/boards_view.html",
                {"form": form, "items": item_details, "email": email})

    return render(request, "imputations/boards_view.html", {"form": form})
