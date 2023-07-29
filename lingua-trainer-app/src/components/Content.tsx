import * as React from 'react';
import ChatMessageLeft from './ChatMessageLeft';
import ChatMessageRight from './ChatMessageRight';
import avatarA from  '../assets/img/profile/robot.png';
import avatarB from '../assets/img/profile/sample-avatar.jpg';

interface IContentProps {
}

const Content: React.FunctionComponent<IContentProps> = (props) => {
    
  return (
    <div className="chat-container">
        <ChatMessageLeft avatar={avatarA} message="Hello there! I am your Helpful language assistant here to teach you how to communicate in German." />
        <ChatMessageRight avatar={avatarB} message="Hi! How are you? It's so nice to be on this plaform and get to know you" />
        <ChatMessageLeft avatar={avatarA} message="I'm doing well, thank you!" />
        <ChatMessageRight avatar={avatarB} message="That's great to hear!" />
        <ChatMessageLeft avatar={avatarA} message="We are attempt a simple challenge are you prepared?" />
    </div>
  );
};

export default Content;
