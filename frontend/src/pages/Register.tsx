import React, { useState } from "react";

function Register(){
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirm] = useState('');
    const [email, setEmail] = useState('');
    const [phone, setPhone] = useState('');
    const [response, setResponseData] = useState(null);

    const HandleSubmit = async (e: React.FormEvent<HTMLFormElement>) =>{
        e.preventDefault();

        try{
            const response = await fetch("http://localhost:8000/register/",
                {
                    method: "POST",
                    headers:{
                        'Content-Type': "application/json",
                    },
                body: JSON.stringify({
                    username,
                    password,
                    confirmPassword,
                    email,
                    phone,
                }),
                });
        if (!response.ok){
            throw new Error('An error with registation.');
        }
        const data = await response.json();
        setResponseData(data);
    }   catch(error){
        console.error('An error', error);
    }
};
}
export default Register