sudo apt-get install -y \
    python-pip \
    build-essential \
    git \
    python \
    python-dev

sudo pip install --upgrade pip 
sudo pip install --upgrade virtualenv 

if [ ! -d venv ]
then
  virtualenv venv
fi


#Installing MongoDB:
sudo apt-get install -y mongodb-org

#To start MongoDB:
mongod -f mongod.conf

. venv/bin/activate
pip install --upgrade tensorflow      # for Python 2.7
pip install -r requirments.txt
