import React from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';


export function LogIn() {
    const navigate = useNavigate();

    const handleFormSubmit = async (e) => {
      e.preventDefault();
  
      try {
        const response = await axios.post('http://localhost:8000/api/v1/token/', {
          username: e.target.username.value,
          password: e.target.password.value,
        });
  
        const token = response.data.token;
  
        // Save the token to local storage
        localStorage.setItem('userToken', token);
        
        // Request to fetch additional data after authentication
        const responseUserData = await axios.get('http://localhost:8000/api/v1/test/26/', {
        headers: {
          Authorization: `Token ${token}`,
        },
        });

        const userData = responseUserData.data;

        // Process the fetched user data (replace this with your logic)
        console.log('User Data:', userData);
        
        // Redirect to the next page
        navigate('/analysis', { state: { userData } });
      } catch (error) {
        console.error('Error:', error.message);
        // Handle error, show error message, etc.
      }
    };



    return (
        <form className="login_form" onSubmit={handleFormSubmit}>
            <span>Login</span> <input type="text" name="username" />
            <span>Password</span>  <input type="password" name="password" />
            <input type="submit" value="Вход"></input>
        </form>
    );
}


