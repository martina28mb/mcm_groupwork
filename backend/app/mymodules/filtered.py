import pandas as pd  

# Defining a function to apply filters for accomodation research
def apply_filters(df,  piscina, accesso_disabili, fitness, sauna, aria_condizionata, lago):
    """
    Apply filters to the DataFrame based on specified criteria.

    Args:
        df (DataFrame): The DataFrame to filter.
        piscina (bool): Filter by swimming pool availability.
        accesso_disabili (bool): Filter by disabled access availability.
        fitness (bool): Filter by fitness facilities availability.
        sauna (bool): Filter by sauna availability.
        aria_condizionata (bool): Filter by air conditioning availability.
        lago (bool): Filter by lake availability.

    Returns:
        DataFrame: The filtered DataFrame.
    """
    # Apply the swimming pool filter
    if piscina is not None and piscina:
        df = df[df['PISCINA'] == 'Vero']

    # Apply the disabled access filter
    if accesso_disabili is not None and accesso_disabili:
        df = df[df['ACCESSO AI DISABILI'] == 'Vero']

    # Apply the fitness facilities filter
    if fitness is not None and fitness:
        df = df[df['FITNESS'] == 'Vero']

    # Apply the sauna filter
    if sauna is not None and sauna:
        df = df[df['SAUNA'] == 'Vero']

    # Apply the air conditioning filter
    if aria_condizionata is not None and aria_condizionata:
        df = df[df['ARIA CONDIZIONATA'] == 'Vero']

    # Apply the lake filter
    if lago is not None and lago:
        df = df[df['LAGO'] == 'Vero']

    return df  # Return the filtered DataFrame
