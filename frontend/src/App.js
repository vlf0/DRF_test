import React from 'react';
import './components/login_form.css'; 
// eslint-disable-next-line
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { LogIn } from './components/LoginForm';
import GetAnalysis from './components/Analysis';

function App() {
  return (
      <Routes>
        <Route path="/" element={<LogIn />} />
        <Route path="/analysis" element={<GetAnalysis />} />
      </Routes>
  );
}

export default App;
