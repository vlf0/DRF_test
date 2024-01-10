import React from 'react';
import { useSpring, animated } from 'react-spring';
import Header from './Header';
import SignInDetailBoard from './signIn_detail_board/SigInDetailBoard';
import SignOutDetailBoard from './signout_detail_board/SignOutDetailBoard';
import '../menu/top_block.css';
import '../dashboard/dashboard_content.css';



const profiles = ['Кардио', 'Невро', 'Терапия']; //List of depts from KISDB
const arrivedFacts = [10, 15, 8]; //List of fact arrived patients
const combinedData = profiles.map((profile, index) => ({ профиль: profile, план: arrivedFacts[index] })); //Mapping two lists above

function DetailBoard({textHeader, currentDatetime, sign}) {

  const props = useSpring({
    from: { opacity: 0 },
    to: { opacity: 1 },
    config: { duration: 700 },
  }); 

    return (
      <>
      <animated.div
      className='top_block'
      style={props}>
        <Header textHeader={textHeader} currentDatetime={currentDatetime}/>
      </animated.div>
      <animated.div className='dashboard' style={props}>

        {/* <SignInDetailBoard signInCount={30} refuseCount={10} combinedData={combinedData}/> */}
        {sign === 'out' ? <SignOutDetailBoard profiles={profiles} /> : <SignInDetailBoard signInCount={30} refuseCount={10} combinedData={combinedData}/>}

        {/* <SignInDetailBoard blockName={'Гопитализированные по каналам'} /> */}
      </animated.div>
      </>
    );
  }
  
  export default DetailBoard;