"""
Backend module for the FastAPI application.

This module defines a FastAPI application that serves
as the backend for the project.
"""

from fastapi import FastAPI, Query
from typing import Optional
import pandas as pd

app = FastAPI()

df = pd.read_csv('/app/app/output.csv')
df_musei = pd.read_csv('/app/app/musei_veneto.csv')

@app.get('/')
def read_root():
    """
    Root endpoint for the backend.

    Returns:
        dict: A simple greeting.
    """
    return {"Hello": "World"}


@app.get('/query/{person_name}')
def read_item(
    comune: str
):
    """
    Retrieve accommodation and museum information based on specified filters.

    Args:
        comune (str): The municipality for which to retrieve information.
        piscina (Optional[bool]): Filter by swimming pool availability.
        accesso_disabili (Optional[bool]): Filter by disabled access.
        fitness (Optional[bool]): Filter by fitness facilities availability.
        sauna (Optional[bool]): Filter by sauna availability.
        aria_condizionata (Optional[bool]): Filter by air conditioning.
        lago (Optional[bool]): Filter by lake availability.

    Returns:
        dict: Accommodation and museum information based on specified filters.
    """
    comune = comune.upper()

    results = df[df['COMUNE'] == comune]
    denominazione_alloggio = results['DENOMINAZIONE'].tolist()
    results_musei = df_musei[df_musei['Comune'] == comune]
    denominazione_musei = results_musei['Nome'].tolist()

    result_list = []
    for nome in zip(denominazione_alloggio):
        result_item = {"nome": nome}

        result_list.append(result_item)

    if denominazione_musei or denominazione_alloggio:
        return {"comune": comune, "risultati": result_list, "musei_consigliati": denominazione_musei}
    else:
        return {"error": "No results"}
