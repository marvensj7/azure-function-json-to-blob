import logging
import azure.functions as func
import os
from azure.storage.blob import BlobServiceClient
import json
from datetime import datetime

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse("Invalid JSON input.", status_code=400)

    blob_conn_str = os.getenv("AzureWebJobsStorage")
    container_name = os.getenv("BLOB_CONTAINER_NAME", "mycontainer")

    if not blob_conn_str:
        return func.HttpResponse("Missing storage connection string.", status_code=500)

    try:
        blob_service_client = BlobServiceClient.from_connection_string(blob_conn_str)
        container_client = blob_service_client.get_container_client(container_name)
        # Create container if it doesn't exist
        try:
            container_client.create_container()
        except Exception:
            pass  # Already exists

        # Write JSON to blob with timestamp
        blob_name = f"data_{datetime.utcnow().strftime('%Y%m%d%H%M%S')}.json"
        blob_client = container_client.get_blob_client(blob_name)
        blob_client.upload_blob(json.dumps(req_body), overwrite=True)

        return func.HttpResponse(f"Blob {blob_name} written successfully.", status_code=200)
    except Exception as e:
        logging.error(f"Failed to write to blob: {e}")
        return func.HttpResponse(f"Failed to write to blob: {str(e)}", status_code=500)