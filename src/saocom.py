""""Código de prueba para abrir y manipular imagenes de SAOCOM"""
from fileinput import filename
from ftplib import FTP
import os

import geopandas
import pandas
import pyroSAR

# Accedo a las imágenes guardadas en el disco
FILE_DIR = "/home/tele/proyects/geoSAR/src/data/S1A_OPER_SAR_EOSSP__CORE_L1A_OLF_20210930T172207.zip"

scene = pyroSAR.identify(FILE_DIR)

if __name__ == "__main__":
    print(scene)