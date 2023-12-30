import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import GetAnalysis from './components/dashboard/Analysis';
import ArrivedDashboard from './components/dashboard/second_dashboards/ArrivedDashboard';
import DeadsDashboard from './components/dashboard/second_dashboards/DeadsDashboard';
import SignOutDashboard from './components/dashboard/second_dashboards/SignOutDashboard';
import DetailBoard from './components/details/Details';

function App() {
  return (
      <Routes>
        <Route path="/" element={<GetAnalysis />} />
        <Route path="/arrived" element={<ArrivedDashboard />} />
        <Route path="/deads" element={<DeadsDashboard />} />
        <Route path="/signout" element={<SignOutDashboard />} />

        <Route path="/arrived_detail" element={<DetailBoard />} />
        <Route path="/refuse_detail" element={<DetailBoard />} />
        <Route path="/hosp_detail" element={<DetailBoard />} />
        <Route path="/signout_detail" element={<DetailBoard />} />
        <Route path="/deads_detail" element={<DetailBoard />} />
        <Route path="/OAR_detail" element={<DetailBoard />} />


      </Routes>
  );
}

export default App;
