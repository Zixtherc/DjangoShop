import React, { useState } from "react";
import { useLocation } from 'react-router-dom';
import styles from './ProductsDetail.module.css'; 

function ProductDetail() {

  const [selectedSize, setSelectedSize] = useState(null);
  const sizes = ['S', 'M', 'L', 'XL'];

  const location = useLocation();
  const { product } = location.state || {};
  
  
  if (!product) return <div className={styles.container}>SYSTEM_ERROR: NO_DATA</div>;
  return (

    
    <div className={styles.container}> 
      {product.image && (
        <img 
          src={`http://localhost:8000${product.image}`}
          alt={product.name} 
          className={styles.productImage} 
        />
      )}
      <h1 className={styles.productTitle}>./ {product.name} |</h1>
      <span className={styles.productPrice}>{Math.floor(product.price)}: ₴</span>
    </div>
  );
}

export default ProductDetail;