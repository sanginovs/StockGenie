# This file sets up the virtual environment.
# Run "source setup.sh" each time you want to run the app.
# This file is all the requirements needed to run the app


if [ ! -d venv ]
then
  virtualenv venv
fi

. venv/bin/activate

pip install Flask
pip install sqlalchemy
