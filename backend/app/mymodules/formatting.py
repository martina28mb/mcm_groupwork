import pandas as pd  

# Defining a function to format the results 
def format_results(results):
    """
    Format the results Dataframe into a list of dictionaries.

    Args:
        results (Dataframe): The Dataframe containing the results.

    Returns:
        list: A list of dictionaries representing the formatted results.
    """
    # Extracting required columns from the results 
    alloggio = results['DENOMINAZIONE'].tolist()  # Accommodation names
    l_alloggio = results['SITO WEB'].tolist()     # Accommodation websites
    i_alloggio = results['INDIRIZZO'].tolist()    # Accommodation addresses
    n_telefono = results['TELEFONO'].tolist()     # Accommodation phone numbers
    i_email = results['EMAIL'].tolist()           # Accommodation email addresses
    
    # Initializing an empty list to store formatted results
    result_list = []

    # Iterating through the lists simultaneously using zip
    for nome, link, indirizzo, telefono, email in zip(alloggio, l_alloggio, i_alloggio, n_telefono, i_email):
        # Create a dictionary for each result item
        result_item = {"nome": nome}  # Include accommodation name
        
        # Include accommodation website if available
        if pd.notna(link):
            result_item["link"] = link
        
        # Include accommodation address if available
        if pd.notna(indirizzo):
            result_item["indirizzo"] = indirizzo
        
        # Include accommodation phone number if available
        if pd.notna(telefono):
            result_item["telefono"] = telefono
        
        # Include accommodation email address if available
        if pd.notna(email):
            result_item["email"] = email

        # Append the result item to the result list
        result_list.append(result_item)

    return result_list  # Return the list of formatted results
