import React from 'react';
import { useSpring, animated } from 'react-spring';
import Header from './Header';
import SignInDetailBoard from './signIn_detail_boards/SigInDetailBoard';
import '../menu/top_block.css';
import '../dashboard/dashboard_content.css';


function DetailBoard({textHeader, currentDatetime}) {

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
        <SignInDetailBoard signInCount={30} refuseCount={10}/>
        {/* <SignInDetailBoard blockName={'Гопитализированные по каналам'} /> */}
      </animated.div>
      </>
    );
  }
  
  export default DetailBoard;