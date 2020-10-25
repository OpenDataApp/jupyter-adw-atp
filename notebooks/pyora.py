import os
import re
from zipfile import ZipFile

def make_folder(folder_path):
    """Description
    Create a default folders
    """
    return os.makedirs(folder_path, mode=0o700, exist_ok=True)

def unzip_wallet(zip_wallet, wallet_folder):
    
    wallet_db_name = zip_wallet.split("_")[1].split(".")[0].lower()
    
    try:
        
        unzip_folder =  os.path.join(wallet_folder, wallet_db_name)
        make_folder(unzip_folder)
        
        with ZipFile(os.path.join(wallet_folder, zip_wallet), 'r') as zwallet:
            zwallet.extractall(unzip_folder)
    except:
        print(f"Extract zip error {zip_wallet}")

def update_sqlnet_ora(path_sqlnet_ora="wallet/jupyter/sqlnet.ora", DIRECTORY="/home/jovyan/work/notebooks/wallet/jupyter/"):
    
    # read init value and change it
    f = open(path_sqlnet_ora, "r")
    init_sqlnet = f.read()
    fin_sqlnet = re.sub('\"(.+)\"', DIRECTORY, init_sqlnet)
    f.close()
    
    # rewrite fin value
    f = open(path_sqlnet_ora, "w")
    f.write(fin_sqlnet)
    f.close()

def db_setup(db_name, db_user, db_password, wallet_folder="wallet"):
    """Description
    Create base configurations to connect with ATP-ADW data base.
    """
    
    # if not exist
    make_folder(wallet_folder)
    
    # parameters db connection 
    db_name = db_name.lower() # default behavior from DB-CONNECTION at OCI
    db_user = db_name 
    db_password = db_name
    zip_wallet_path = os.path.join(".", wallet_folder)
    
    # check wallet zip in folder
    try:
        zip_wallet = os.listdir(zip_wallet_path)[0]
        # Unzip wallet
        unzip_wallet(zip_wallet, wallet_folder)
    except:
        print(f"Wallet_{db_name}.zip not founded in -> {wallet_folder} folder")
           
    # update sqlnet_ora
    unzip_folder = os.path.join(wallet_folder, db_name)
    sqlnet_ora_path = os.path.join(unzip_folder,"sqlnet.ora")
    update_sqlnet_ora(sqlnet_ora_path, unzip_folder)
    