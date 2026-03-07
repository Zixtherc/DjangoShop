// @ts-ignore
import React from "react";
// @ts-ignore
import { useSmoothScroll } from '../../components/ScrollTo/ScrollTo';

import styles from "./Home.module.css"

function Home() {

    return(
        <div className={styles.introduce}>
            <h1>QUANTUM {"{FIELDS}"}</h1>
            <h1>{'{FLUX}'}</h1>
            <h1>::[0110]::</h1>
            <h1>Σ</h1>
            <h1>𝝅</h1>
        </div>

    )

}

export default Home