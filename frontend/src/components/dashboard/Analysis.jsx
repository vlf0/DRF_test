import React from 'react';
import { useLocation } from 'react-router-dom';
import { useSpring, animated } from 'react-spring';
import ArrivedChart from '../charts/ArrivedChart';
import TopBlock from '../menu/TopBlock';
import BlockInfo from '../boards/BlockInfo';
import HospRefuseChart from '../charts/HospRefuseChart';
import InsuranceChart from '../charts/InsuranceChart';
import "../parent.css" 
import './dashboard_content.css'


function GetAnalysis() {
console.log('GetAnalysis rendered');

  const location = useLocation();
  const userData = location.state?.userData;

  const props = useSpring({
    from: { opacity: 0 },
    to: { opacity: 1 },
    config: { duration: 1200 },
  });

  return (
    <>  
      <TopBlock />
      <animated.div className='dashboard' style={props}>
        <div className='board-cards'>
          <BlockInfo headerText='Поступившие' data={[122, 147]}/>
          <BlockInfo headerText='Госпитализировано' data={[90, 88]}/>
          <BlockInfo headerText='Отказано' data={[32, 18]}/>
          <BlockInfo headerText='Выписанные' data={[54, 62]}/>
          <BlockInfo headerText='Умершие' data={[12, 7]}/>
          <BlockInfo headerText='ОАР' data={[18, 19]}/>
        </div>
        <div className='board-charts'>
          <ArrivedChart />
          <HospRefuseChart />
          <InsuranceChart />
        </div>
      </animated.div>
    </>
  );
}

export default GetAnalysis;
