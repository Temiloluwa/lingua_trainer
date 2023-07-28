import * as React from 'react';

interface IHeaderProps {
}

const Header: React.FunctionComponent<IHeaderProps> = (props) => {
  return (
    <div className='navbar-custom'>
      <h3>LANGUAGE LEANER</h3>
    </div> 
  )
};

export default Header;
