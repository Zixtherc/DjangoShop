import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

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
        <form onSubmit={handleSubmit}>
            <input type="text" placeholder="Username" value={username} onChange={event => setUsername(event.target.value)}/>
            <input type="password" placeholder="Password" value={password} onChange={event => setPassword(event.target.value)}/>
            <button type="submit">Login</button>    
            {responseData}
        </form>
    )
}
export default Login