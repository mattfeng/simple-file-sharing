# Simple File Sharing

## Description
Simple File Sharing is a online file sharing service backed by Amazon S3.

## Use Cases
* Quick sharing of non-sensitive documents.
* Temporary file and notes storage.

## How to Use
* Deploying an instance of Simple File Sharing should be manageable through the provided Dockerfile. A list of all the environment variables that need to be set can be found in [DEPLOYMENT.md](DEPLOYMENT.md).

* To upload a file, use the following command: `curl -F 'data=@path/to/file' <upload_url>/u`
* To download a file, simply go to the link with the five alphanumeric character stub.

## Why?
I often use two different computers when working (one laptop and one desktop), and there have been countless times when I wanted to transfer a file on one machine to the other (often for reading on a bigger screen, or to have the reading on the go). While there are more secure and traditional ways to transfer files (e.g. `scp`, `python -m http.server`, etc), the problem I found with these approaches was the number of steps involved -- I would have to get my IP address and open a port on my firewall, or have to install an additional binary (the machines I use have ephemeral login storage). It was a time hassle, which would be necessary if I was transferring important documents, but these were ordinary PDFs that could be found online (just with extremely long URLs). Thus, I wanted to create a service that I could use to share any document (in the case that the document was not yet hosted online) quickly and easily.

## TODO
* [ ] Optional symmetric encryption via Frenet encryption scheme
