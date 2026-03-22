// @ts-ignore
import React from "react";
// @ts-ignore
import { useSmoothScroll } from '../../components/ScrollTo/ScrollTo';
// @ts-ignore
import SphereScene from '../../components/GeometricalWireFrame/Sphere';
// @ts-ignore
import GravityGrid from "../../components/GeometricalWireFrame/Plane";

import {getDataApi} from '../../api/api.ts'

import styles from "./Home.module.css"


const symbols = [
    "QUANTUM {FIELDS}",
    "{FLUX}",
    "::[0110]::",
    "Σ",
    "π",
    '3.14159265359',
    '∫',
    '∅',
];



function Home() {
    const [products, setProducts ] = React.useState('');

    React.useEffect(() => {
        const load = async () => {
            const data = await getDataApi('products');
            setProducts(data)
        };
        load();
    }, []);

    return(
        <>
        <div className={styles.grid}>
            <div className={styles.introduce}>
                {symbols.map((text, index) => (
                    <h1 key={index} className={styles.symbol}>
                        {text}
                    </h1>
                ))}
                <SphereScene className={styles.sphereBack} />
            </div>

        </div>
            
        <div className={styles.products}>
            <h1>//Products [ ]</h1>
            
            {/* Проверяем, что products — это массив, и перебираем его */}
            {Array.isArray(products) && products.map((product) => (
                <div key={product.id} style={{ marginBottom: '20px', border: '1px solid #333', padding: '10px' }}>
                <h2>{product.name}</h2>
                <p>{product.description}</p>
                <span>Price: {product.price}</span>
                
                {/* Добавляем картинку */}
                {product.image && (
                    <img 
                    src={`http://127.0.0.1:8000${product.image}`} 
                    alt={product.name} 
                    />
                )}
                </div>
            ))}
            </div>
        </>
    )
}

export default Home