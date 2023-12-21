import React from 'react';
import { useSpring, animated } from 'react-spring';

const InBlockInfo = ({ data }) => {
  const props = useSpring({
    from: { transform: 'translateY(100%)', opacity: 0 },
    to: { transform: data ? 'translateY(0%)' : 'translateY(100%)', opacity: data ? 1 : 0 },
    config: { duration: 900 },
  });

  return (
    <animated.div className='day_arrived' style={props}>
      {data ? (
        <>
          <p className='headers'>Поступившие</p>
          <p className='text_data'>{data.data}</p>
          
          {/* Add more properties as needed */}
        </>
      ) : (
        <p>Loading...</p>
      )}
    </animated.div>
  );

};

export default InBlockInfo;