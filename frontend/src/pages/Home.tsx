// frontend/src/pages/Home.tsx
import { useEffect, useState } from "react"

interface Product {
  id: number
  name: string
  price: number
}

export default function Home() {
  const [products, setProducts] = useState<Product[]>([])

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/products/")
      .then(res => res.json())
      .then(data => setProducts(data))
  }, [])

  return (
    <div>
      <h1>Home Page</h1>
      
      {products.map(product => (
        <div key={product.id}>
          <h3>{product.name}</h3>
          <p>{product.price}$</p>
        </div>
      ))}
    </div>
  )
}