// @ts-ignore
import React from "react";
// @ts-ignore
import { useSmoothScroll } from '../../components/ScrollTo/ScrollTo';
// @ts-ignore
import SphereScene from '../../components/GeometricalWireFrame/Sphere';
import styles from "./Home.module.css"

const symbols = [
    "QUANTUM {FIELDS}",
    "{FLUX}",
    "::[0110]::",
    "Σ",
    "π",
    '3.14159265359',
];

function Home() {

    return(
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

    )
}

export default Home