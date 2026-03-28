import { useLocation } from 'react-router-dom';

function ProductDetail() {
  const location = useLocation();
  const { product } = location.state || {}; 
  if (!product) return <div>Данные не переданы или страница обновлена</div>;

  return (
    <div>
      <h1>{product.name}</h1>
      <p>{product.price}</p>
    </div>
  );
}


export default ProductDetail;