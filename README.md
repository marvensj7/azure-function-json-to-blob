# Azure Function Python Example: Writing JSON to Blob Storage

## Scenario
A Python Azure Function receives JSON input via HTTP POST and writes it as a blob in Azure Blob Storage.

## Permissions Fix
If you saw "permission denied", the likely issue is a missing/wrong storage connection string or misconfigured role.  
**Fixed:** Set the correct `AzureWebJobsStorage` connection string (Storage Account Contributor role, or connection string with write access).

## Files
- `function_app/WriteToBlob/__init__.py` – Main function code.
- `function_app/WriteToBlob/function.json` – Function binding config.
- `function_app/local.settings.json` – Local settings (reference, don’t commit secrets).
- `cloudshell_test.sh` – Script to trigger and test the function.
- `evidence/successful_run.json` – Example result of a successful run.

## Setup

### 1. Deploy Function
- Deploy via VS Code, Azure CLI, or Azure Portal.
- Set environment variables in Azure Portal:
    - `AzureWebJobsStorage`: Your storage account connection string
    - `BLOB_CONTAINER_NAME`: (optional) Container name, defaults to `mycontainer`

### 2. Set Permissions
- Storage account should allow write access for the Function App.
- (If using Managed Identity, assign “Storage Blob Data Contributor” role to the function’s identity.)

### 3. Test with Cloud Shell

Edit `cloudshell_test.sh`:
- Set `FUNCTION_URL` to your function endpoint
- Set `FUNCTION_KEY` (from Azure Portal > Function App > Functions > write2blob > Get Function URL)

Run:
```sh
bash cloudshell_test.sh
```
You should see a message like in `evidence/successful_run.json`.

## Evidence

```json
{
  "result": "Blob data_20250917143119.json written successfully."
}
```

## Notes
- The function creates the blob container if it does not exist.
- For local testing, set secrets in `local.settings.json` (do NOT commit real secrets).
