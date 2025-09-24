# 🍽️ RestaurantApp

Aplicație web dezvoltată în **Python + Django** pentru gestionarea unui restaurant.  
Include funcționalități de **înregistrare**, **autentificare** și **gestionarea meniului** (adăugare produse).

## 🚀 Funcționalități principale
- 👤 Înregistrare și autentificare utilizatori
- 🔐 Sistem de login/logout
- 🍕 Creare, vizualizare și gestionare produse din meniu
- 🖼️ Posibilitatea de a adăuga imagini și prețuri la produse
- 📱 Interfață simplă și prietenoasă

## 📦 Instalare și rulare

1. Clonează repository-ul:
   ```bash
   git clone https://github.com/DanielMrg-tech/Proiectul_Final
   asgiref==3.9.1
    colorama==0.4.6
    Django==5.2.6
    django-classy-tags==4.1.0
    django-cms==5.0.3
    django-formtools==2.5.1
    django-rest-framework==0.1.0
    django-sekizai==4.1.0
    django-treebeard==4.7.1
    djangocms-admin-style==3.3.1
    djangorestframework==3.16.1
    iniconfig==2.1.0
    packaging==25.0
    pillow==11.3.0
    pluggy==1.6.0
    Pygments==2.19.2
    pytest==8.4.2
    pytest-django==4.11.1
    setuptools==80.9.0
    sqlparse==0.5.3
    tzdata==2025.2


# ✅ Tehnologii utilizate

    Python 3.x
    
    Django 4.x
    
    SQLite (implicit) sau PostgreSQL/MySQL pentru producție
    
    HTML, CSS, Bootstrap (pentru interfață)

# 📂 Structura proiectului
    restaurant-app/
    │
    ├── restaurant/         # aplicația principală Django
    ├── accounts/           # autentificare și gestionare utilizatori
    ├── templates/          # fișiere HTML
    ├── db.sqlite3          # baza de date implicită
    ├── manage.py           # script principal Django
    └── requirements.txt    # dependențe proiect

# Url-uri folosite
        path('', views.main_page, name='main_page'),
    path('about_restaurant/', views.about_restaurant, name='about_restaurant'),
    path('api/', include(router.urls)),

    path('meniu/', views.meniu_view, name='meniu'),
    path('meniu/<int:pk>/delete/', views.delete_meniu, name='delete_meniu'),
    path('meniu/<int:pk>/edit/', views.update_meniu, name='update_meniu'),
    path('users/<int:user_id>/meniu/', views.meniu_by_user, name='meniu_by_user')