import React from 'react';

import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import GetAnalysis from './components/dashboard/Analysis';

function App() {
  return (
      <Routes>
        <Route path="/" element={<GetAnalysis />} />
      </Routes>
  );
}

export default App;
