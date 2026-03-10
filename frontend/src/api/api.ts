import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/api'

export const getDataApi = async (url: string) =>{
    try{
        const response = await axios.get(`${API_URL}/${url}/`);
        return response.data;
    }
    catch(error){
        console.error('API_FETCH ERROR:', error);
        return [];
    }
}