import * as React from 'react';
import avatarImg from '../assets/img/profile/sample-avatar.webp';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faCubesStacked, faRoad, faFilm } from '@fortawesome/free-solid-svg-icons'

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
          <FontAwesomeIcon icon={faCubesStacked} className='challenge-icon'/>
            <a href="#" className='active'>Speak with Native Speaker</a>
          </li>
          <li>
            <FontAwesomeIcon icon={faRoad} className='challenge-icon' />
            <a href="#">Vocabulary trainer</a>
          </li>
          <li>
            <FontAwesomeIcon icon={faFilm} className='challenge-icon' />
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
