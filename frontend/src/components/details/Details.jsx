import React from 'react';
import { useSpring } from 'react-spring';


function DetailBoard() {

    const props = useSpring({
      from: { opacity: 0 },
      to: { opacity: 1 },
      config: { duration: 1200 },
    });
  
    return (
      <>  
        <p>test</p>
      </>
    );
  }
  
  export default DetailBoard;