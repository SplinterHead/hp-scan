# HP Scan
Python webhook receiver to trigger a scan and automatically email the content to a designated inbox

This project is a middlware that allows a webhook (from services like HomeAssistant, Elgato Stream Deck, etc) to trigger a scan on a HP scanner and send it to a preconfigured email inbox.

## Configuration

The HP Scan tool will need some configuration to understand where the scanner is and where the documents should end up.
The easiest way to accomplish this is to use the `.env` template to create one for your environment

| Variable              | Type     | Required | Description                                   |
|-----------------------|----------|----------|-----------------------------------------------|
| `HP_SCANNER_IP`       | `string` | Yes      | IP address of the HP Scanner                  |
| `SMTP_SERVER`         | `string` | Yes      | Hostname / IP of the SMTP server              |
| `SMTP_SERVER_PORT`    | `int`    | No       | Port for the SMTP server, defaults to 465     |
| `SMTP_SENDER_EMAIL`   | `string` | Yes      | Email address to send the document from       |
| `SMTP_SENDER_EMAIL`   | `string` | Yes      | Password of the sender to log into the server |
| `SMTP_RECIEVER_EMAIL` | `string` | Yes      | Email address to send the document to         |

## Usage

This project is bundled as a Docker container for deployment into an existing server-based environment

To launch the service, execute the Docker command (or adapt for Podman), using the created `.env` file
```bash
docker run -p 5000:5000 --env-file .env splinterhead27/hp-scan
```

Alternatively, this can be launched with Docker Compose

```yaml
services:
  hp-scan:
    image: splinterhead27/hp-scan
    ports:
      - 5000:5000
    environment:
      HP_SCANNER_IP: "192.168.xx.xx"
    restart: unless-stopped
```
## Special Thanks

This tool uses the awesome work from [prasannareddych's HPScanCLI](https://github.com/prasannareddych/HPScanCLI) tool