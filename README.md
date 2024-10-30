
# Dog Quotes API with CRUD Operations 🐾

This Dog Quotes API allows users to interact with a list of dog-related quotes. It provides endpoints to retrieve random quotes, add new ones, update or delete existing quotes by their index. It’s perfect for anyone who needs some dog-inspired inspiration or who wants to build applications featuring dog quotes.

## Table of Contents
1. [Getting Started](#getting-started)
2. [Endpoints](#endpoints)
3. [Example JSON Quotes](#example-json-quotes)
4. [Installation](#installation)
5. [Usage](#usage)

## Getting Started

Clone this repository and run the API locally to interact with the list of quotes.

```bash
git clone https://github.com/yourusername/dog-quotes-api.git
cd dog-quotes-api
```

### Installation

1. **Python** (3.6 or later) must be installed.
2. Install dependencies with:
   ```bash
   pip install flask
   ```

### Usage

Run the server locally by executing:

```bash
python app.py
```

The server will be hosted on `http://127.0.0.1:5000`.

## Endpoints

### Retrieve a Random Quote
- **GET /quote**
  - Returns a random dog quote.
  
### Retrieve All Quotes with Indexes
- **GET /quotes**
  - Returns all quotes with indexes for easier management.

### Add a New Quote
- **POST /quote**
  - Add a new quote by sending a JSON body:
    ```json
    {
      "quote": "Your dog-related quote here."
    }
    ```

### Update a Quote by Index
- **PUT /quote/<index>**
  - Update a quote by providing the index and a JSON body:
    ```json
    {
      "quote": "Updated quote text."
    }
    ```

### Delete a Quote by Index
- **DELETE /quote/<index>**
  - Deletes the quote at the specified index.

## Example JSON Quotes

The project starts with 100 inspiring, heartwarming, and humorous dog quotes.

```json
[
  "Dogs do speak, but only to those who know how to listen.",
  "A dog is the only thing on earth that loves you more than you love yourself.",
  ...
]
```

## Contributing

Contributions are welcome! Feel free to submit a pull request or suggest improvements by creating an issue.

---


