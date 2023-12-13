import React, {useState} from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';




export function LogIn() {
    const [text, setText] = useState(null)
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
        const responseUserData = await axios.get('http://localhost:8000/api/v1/hospdata/', {
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
        console.error('Error:', error.response.status);

        // Output error text if user creds are invalid
        if (error.response.status === 400) {
          console.error('Error:', text);
          setText('Incorrect login or password');
        }
        
    };
      }
    
    return (
      <>
        <form className="login_form" onSubmit={handleFormSubmit}>
            <span>Login</span> <input type="text" name="username" />
            <span>Password</span>  <input type="password" name="password" />
            <input type="submit" value="Вход"></input>
        </form>

        {text && <p style={{ color: 'red' }}>{text}</p>}  
      </>
    );
}


