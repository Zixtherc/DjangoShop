import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

function Register(){
    const navigete = useNavigate();
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [email, setEmail] = useState('');
    const [phone_number, setPhone] = useState('');
    const [responseData, setResponseData] = useState(null);

    const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) =>{
        event.preventDefault();

        try{
            const response = await fetch("http://localhost:8000/register/",
                {
                    method: "POST",
                    headers:{'Content-Type': "application/json"},
                    body: JSON.stringify({username, password, confirmPassword, email, phone_number}),
                });
        if (!response.ok){
            throw new Error('An error with registation.');
        }
        const data = await response.json();
        setResponseData(data);
        navigete('/login');
    }   catch(error){
        console.error('An error', error);
        }
    };
    return (
        <form onSubmit={handleSubmit}>
            <input type="text" placeholder="Username" value={username} onChange={event => setUsername(event.target.value)}/>
            <input type="password" placeholder="Password" value={password} onChange={event => setPassword(event.target.value)}/>
            <input type="password" placeholder="Confirm Password" value={confirmPassword} onChange={event => setConfirmPassword(event.target.value)}/>
            <input type="email" placeholder="Email" value={email} onChange={event => setEmail(event.target.value)}/>
            <input type="tel" placeholder="Phone" value={phone_number} onChange={event => setPhone(event.target.value)}/>
            
            <button type="submit">Register</button>
            
            {responseData}
        </form>
    )
}
export default Register