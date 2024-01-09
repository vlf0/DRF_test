import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import GetAnalysis from './components/dashboard/Analysis';
import DetailBoard from './components/details/Details';



function App() {

  const currentDatetime = new Date().toLocaleDateString('ru-RU');

  return (
      <Routes>
        <Route path="/" element={<GetAnalysis />} />

        <Route path="/arrived_detail" element={<DetailBoard textHeader={'Детализация обратившихся'} currentDatetime={currentDatetime} />} />

        <Route path="/signout_detail" element={<DetailBoard textHeader={'Детализация выписанных'} currentDatetime={currentDatetime} />} />

        <Route path="/OAR_detail" element={<DetailBoard textHeader={'Детализация реанимационных отделений'} currentDatetime={currentDatetime} />} />


      </Routes>
  );
}

export default App;
