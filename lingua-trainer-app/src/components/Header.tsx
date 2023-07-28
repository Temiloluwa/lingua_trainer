import * as React from 'react';
import logo from "../assets/img/app/small_logo.jpg";
import germanFlag from "../assets/img/app/german_flag.png";

interface IHeaderProps {
}

const Header: React.FunctionComponent<IHeaderProps> = (props) => {
  return (
    <div className="navbar-custom">
      <div className="header-left">
        <img src={logo} alt="Header Image" className=""/>
        <h2>LANGUAGE TRAINER</h2>
      </div>
        <img src={germanFlag} alt="German Flag" className="flag"/>
      
    </div>
    
  )
};

export default Header;
