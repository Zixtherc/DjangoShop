import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

import styles from './Login.module.css';

import Eye from "../../components/EyeWatcher/Eye";

const symbols = [
    "ROOT [ESCALATION/]",
    "0x7FFFD28B",
    "λ",
    "101001100011",
    "::[SYSTEM_INIT]::",
    "0xDEADC0DE",
    "//dev/null",
    "system_call: 0x80",
]

function Login(){
    const navigate = useNavigate();
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [responseData, setResponseData] = useState(null);

    const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();

        try{
            const response = await fetch('http://localhost:8000/login/',
                {
                    method: 'POST',
                    'headers':{'Content-Type': 'application/json'},
                    body: JSON.stringify({username, password})

                });
            if (!response.ok){
                throw new Error('An error with login.')
            };
            const data = await response.json()
            setResponseData(data);
            navigate('/');
        }
            catch(error){console.error();}
    };
    return(
        <>
        <div className={styles.gridLogin}>
            <div className={styles.loginSymbols}>
                {symbols.map((text, index) => (
                    <h1 key={index}>
                        {text}
                    </h1>
                    ))}
                    <div style={{ position: 'absolute', top: '15%', left: '20%' }}><Eye /></div>
                    <div style={{ position: 'absolute', top: '70%', left: '10%' }}><Eye /></div>
                    <div style={{ position: 'absolute', top: '25%', right: '15%' }}><Eye /></div>
                    <div style={{ position: 'absolute', top: '80%', right: '25%' }}><Eye /></div>
            </div>
            <form onSubmit={handleSubmit} className={styles.formLogin}>
                <input type="text" placeholder="Username" value={username} onChange={event => setUsername(event.target.value)}/>
                <input type="password" placeholder="Password" value={password} onChange={event => setPassword(event.target.value)}/>
                <button type="submit" className={styles.submitBtn}>Login</button>    
                {responseData}
            </form>
        </div>

        </>
    )
}
export default Login