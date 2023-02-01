# Aliases
alias v := venv
alias a := activate
alias p := pip
alias i := install
alias m := migrate
alias mm := make_migrations
alias r := run
alias s := superuser
alias f := freeze

# Recipes


# Display available recipes
default:
    @just --list

#Freeze pip to requirements.txt
freeze:
    pip freeze > requirements.txt
    
# Create venv
venv:
    python -m venv --prompt ai-audio .venv

# Activate venv
activate:
    source .venv/bin/activate

# Update pip to latest version
pip:
    python -m pip install --upgrade pip

# Install requirements
install:
    pip install -r requirements.txt

# Migrate
migrate:
    python manage.py migrate

# Make Magrations
make_migrations:
    python manage.py makemigrations

superuser:
    python manage.py createsuperuser

run:
    python manage.py runserver

test:
    set -a && . .venv/bin/activate && set +a

