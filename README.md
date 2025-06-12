# NhiAPI
This simple REST API supports basic CRUD requests. It was made using FastAPI and hosted on an AWS EC2 instance.

-----

# Usage
The API is accessible from the root endpoint at http://localhost:8000. 

Items can also be created, read, updated, and deleted from the inventory as in the following examples:

## POST
[/items/](http://localhost:8000/items/): creates a new item. 
Body:
```json
{
  "name": "Example item",
  "description": "An example item."
}
```

## GET
/items/{item_id}: read an item by its uniform resource identifier. 
Response:
```json
{
  "name": "Example item",
  "description": "An example item."
}
```

## PUT
/items/{item_id}: update an item using its uniform resource identifier. 
Body:
```json
{
  "name": "Updated item",
  "description": "Updated item description."
}
```

## DELETE
/items/{item_id}: delete an item using its uniform resource identifier. 
Response:
```json
{
  "name": "Deleted item",
  "description": "Deleted item description."
}