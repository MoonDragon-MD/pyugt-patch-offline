# Offline server by MoonDragon-MD ( https://github.com/MoonDragon-MD )
# Version: 1.0
# 12/2024
import logging
import ssl
from flask import Flask, jsonify, request

# Configura il logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Crea l'istanza dell'app Flask
app = Flask(__name__)

# Loggare quando la connessione ? SSL o non SSL
@app.before_request
def log_request_info():
    if request.is_secure:
        logger.info("SSL connection established")
    else:
        logger.info("Non-SSL connection established")

# Definisci una route
@app.route('/cookieconsentpub/v1/geo/location', methods=['GET'])
def geo_location():
    geolocation_data = {
        'stateCode': 'China', 
        'countryCode': 'ZH',  
        'regionCode': 'zh'  # Facoltativo
    }
    return jsonify(geolocation_data), 200

if __name__ == '__main__':
    # Percorsi al certificato SSL autofirmato e alla chiave privata
    cert_file = 'certificate.crt'  
    key_file = 'privatekey.key' 

    # Crea il contesto SSL con la libreria ssl di Python
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)  # Usa TLS 1.2 per la connessione sicura
    context.load_cert_chain(certfile=cert_file, keyfile=key_file)  # Carica il certificato e la chiave privata

    # Logga quando il server inizia a eseguire e utilizza SSL
    logger.info(f"Starting Flask server with SSL certificate: {cert_file}")

    # Avvia il server Flask con il contesto SSL
    app.run(host='0.0.0.0', port=443, ssl_context=context)
