from django.apps import AppConfig

# Configurația aplicației "main_page"
class MainPageConfig(AppConfig):
    # Tipul implicit pentru cheile primare (PK) generate în modele
    default_auto_field = 'django.db.models.BigAutoField'
    # Numele aplicației - trebuie să corespundă cu folderul aplicației
    name = 'main_page'
