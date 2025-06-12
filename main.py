from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()



# define Item data model 
class Item(BaseModel):
    name: str
    description: str

# in-memory inventory
items = []



### CRUD operations

# POST method to create an item
@app.post("/items/", response_model=Item)
async def create_item(item: Item):
   items.append(item)
   return item

# API endpoint for GET item requests

@app.get("/items/")
async def list_items():
    return items

@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

# UPDATE method for items
@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    
    items[item_id] = item
    return item

# DELETE method 
@app.delete("/items/{item_id}", response_model=Item)
async def delete_item(item_id: int):
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    
    deleted_item = items.pop(item_id)
    return deleted_item