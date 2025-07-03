# Llamada API

This repository contains a small script (`registros.py`) used to download
employee check-in data from the Asiatech ERP API.

## Environment variables

The script expects the following environment variables to be defined:

- `ASIATECH_API_KEY` – the API key provided by Asiatech.
- `ASIATECH_API_SECRET` – the API secret associated with the key.

Set these variables in your environment before running the script. For example:

```bash
export ASIATECH_API_KEY="your_api_key"
export ASIATECH_API_SECRET="your_api_secret"
python registros.py
```

The `fetch_checkins` function can be used programmatically to retrieve
check-in data between two dates filtered by device.
