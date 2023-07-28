import * as React from 'react';

interface IChatMessageLeftProps {
    message: string;
    avatar: string;
}

const ChatMessageLeft: React.FunctionComponent<IChatMessageLeftProps> = ({message, avatar }) => {
    return (
        <div className="chat-message-left">
          <div className="avatar-container">
            <img className="avatar" src={avatar} alt="Person A's Avatar" />
          </div>
          <div className="message">{message}</div>
        </div>
      );
};

export default ChatMessageLeft;
