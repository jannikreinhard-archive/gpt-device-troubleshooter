# Response-error regression fix

The update rejects empty model replies, filters invalid entries from chat history, bounds HTTP requests, and displays request failures without saving them as assistant messages. The UI resets category state after request errors.

Run `python3 -m unittest discover -s tests -v`. These tests mock network calls; they do not validate the Azure deployment, Graph permissions, live API compatibility or model context limits. This repository remains archived.
