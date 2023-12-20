import React from 'react';
import { useSpring, animated } from 'react-spring';
import InBlockInfo from './InBlockInfo';

const TopBlock = () => {
  const props = useSpring({
    from: { opacity: 0 },
    to: { opacity: 1 },
    config: { duration: 1200 },
  });

  const textContent = 'Оперативная сводка ГКБ им. Демихова'

  const currentDatetime = new Date().toLocaleDateString("ru-RU");

  const inBlockInfoData = {
    data: "Some data for InBlockInfo",
  };

  return (
    <animated.div className='top_block' style={props}>
      <p className='main_header'>{textContent}</p>
      <span className='now_date'>{currentDatetime}</span>
      {/* Add more properties as needed */}
    </animated.div>
  );
};

export default TopBlock;
