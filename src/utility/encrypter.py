import os
from encryption import Encrypt as crpt

# * ------------------------------------------------------
# * ENCRYPT YOUR FILE HERE
# * ------------------------------------------------------

script_dir = os.path.dirname(__file__)
file_path = os.path.join(
    script_dir, "../../data/processed/FILE_TO_ENCRYPT.csv"
)  # path to the file you want to encrypt

crpt.encrypt_file(file_path)
