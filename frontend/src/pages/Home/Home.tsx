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
            
            <h1>//Products[ ]</h1>
            <p>{products}</p>
            
        </div>
        </>
    )
}

export default Home