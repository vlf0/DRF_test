import React, { useState } from 'react';
import axios from 'axios';

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.withCredentials = true;


function App() {
  const [loginData, setLoginData] = useState({
    username: '',
    password: '',
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setLoginData({
      ...loginData,
      [name]: value,
    });
  };

  const handleFormSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post('http://localhost:8000/api/v1/token/', loginData);
      const token = response.data.token;
      console.log('Token:', token);

      // Store the token in local storage
      localStorage.setItem('authToken', token);

      // Redirect the user to another page (replace '/dashboard' with your desired path)
      window.location.replace('/dashboard');

    } catch (error) {
      console.error('Error:', error.message);
      // Handle error, show error message, etc.
    }
  };

  const handleLogout = () => {
    // Clear the authentication token from local storage
    localStorage.removeItem('authToken');

    // Redirect the user to the login page (replace '/login' with your login path)
    window.location.replace('/login');
  };

  return (
    <div>
      <h1>Login</h1>
      <form onSubmit={handleFormSubmit}>
        <label>
          Username:
          <input
            type="text"
            name="username"
            value={loginData.username}
            onChange={handleInputChange}
          />
        </label>
        <br />
        <label>
          Password:
          <input
            type="password"
            name="password"
            value={loginData.password}
            onChange={handleInputChange}
          />
        </label>
        <br />
        <button type="submit">Login</button>
      </form>
        <button onClick={handleLogout}>Logout</button>
    </div>
  );
}

export default App;
