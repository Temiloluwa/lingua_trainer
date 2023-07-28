import * as React from 'react';
import avatarImg from '../assets/img/profile/sample-avatar.webp';

interface ILeftSibarProps {
}

const LeftSibar: React.FunctionComponent<ILeftSibarProps> = (props) => {
  return (
    <>
      <div className="header">
        <div className="sidebar-avatar-container">
          <img className="sidebar-avatar" src={avatarImg} alt="Avatar" />
        </div>
        <h5 className="name">Rose Mary</h5>
      </div>
      <div className="main">
        <h3>Challenges</h3>
        <ul>
          <li>
            <a href="#" className='active'>Speak with Native Speaker</a>
          </li>
          <li>
            <a href="#">Vocabulary trainer</a>
          </li>
          <li>
            <a href="#">Watch German Movie</a>
          </li>
        </ul>
      </div>
      <div className="footer">
        <h3>Contact</h3>
      </div>
    </>
  );
};

export default LeftSibar;
