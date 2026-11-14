# python-network_0

This project is an introduction to networking with `curl`: reading the size
and body of a response, HTTP methods (`GET`, `DELETE`, `OPTIONS`, `POST`),
status codes, custom headers, and POST parameters.

## Requirements

- Bash scripts for Ubuntu 20.04 LTS, first line `#!/bin/bash`
- Second line is a comment describing the script
- All files end with a new line and are executable
- The scripts use `curl`

## Files

| File | Description |
| ---- | ----------- |
| `0-body_size.sh` | Displays the size of the response body in bytes |
| `1-body.sh` | Displays the body of a `200` response only |
| `2-delete.sh` | Sends a `DELETE` request and displays the body |
| `3-methods.sh` | Displays the HTTP methods the server accepts |
| `4-header.sh` | Sends `X-HolbertonSchool-User-Id: 98` and displays the body |
| `5-post_params.sh` | Sends a `POST` with `email` and `subject` and displays the body |

## Author

dngoga1-ai
