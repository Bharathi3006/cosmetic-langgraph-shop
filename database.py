products = [
    {
        "id": 1,
        "name": "Velvet Touch Lipstick",
        "category": "Lips",
        "price": 24.99,
        "description": "A luxurious matte lipstick with long-lasting color and hydration.",
        "image": "https://images.unsplash.com/photo-1586495777744-4413f21062dc?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTB8fGxpcHN0aWNrfGVufDB8fDB8fHww"
    },
    {
        "id": 2,
        "name": "Glow Getter Highlighter Palette",
        "category": "Face",
        "price": 45.00,
        "description": "Four blinding shades to give you that perfect golden hour glow.",
        "image": "https://images.unsplash.com/photo-1596704017358-b967f55b440f?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8bWFrZXVwJTIwcGFsZXR0ZXxlbnwwfHwwfHx8MA%3D%3D"
    },
    {
        "id": 3,
        "name": "Precision Eyeliner Pen",
        "category": "Eyes",
        "price": 18.50,
        "description": "Waterproof, smudge-proof liquid eyeliner for the sharpest wings.",
        "image": "https://images.unsplash.com/photo-1629198735284-818276f7c70e?W=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8ZXllbGluZXJ8ZW58MHx8MHx8fDA%3D"
    },
    {
        "id": 4,
        "name": "Pro Blending Brush Set",
        "category": "Tools",
        "price": 55.00,
        "description": "A set of 12 professional-grade synthetic brushes for seamless application.",
        "image": "https://images.unsplash.com/photo-1596462502278-27bfdd403348?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8bWFrZXVwJTIwYnJ1c2hlc3xlbnwwfHwwfHx8MA%3D%3D"
    },
    {
        "id": 5,
        "name": "Hydrating Rose Setting Spray",
        "category": "Face",
        "price": 28.00,
        "description": "Lock in your look all day with a refreshing burst of rosewater.",
        "image": "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8c2V0dGluZyUyMHNwcmF5fGVufDB8fDB8fHww"
    },
    {
        "id": 6,
        "name": "Volumizing Mascara",
        "category": "Eyes",
        "price": 22.00,
        "description": "Dramatic volume and length without clumps.",
        "image": "https://images.unsplash.com/photo-1631214524020-7e18db9a8f92?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8bWFzY2FyYXxlbnwwfHwwfHx8MA%3D%3D"
    }
]

def search_products(query: str):
    """
    Simple keyword search for mock purposes.
    In a real app, this would use vector search or SQL LIKE queries.
    """
    query = query.lower()
    results = []
    for p in products:
        if query in p["name"].lower() or query in p["description"].lower() or query in p["category"].lower():
            results.append(p)
    return results

def get_all_products():
    return products
