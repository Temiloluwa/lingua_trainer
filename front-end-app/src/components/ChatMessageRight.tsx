import * as React from 'react';

interface IChatMessageRightProps {
    message: string;
    avatar: string;
}

const ChatMessageRight: React.FunctionComponent<IChatMessageRightProps> = ({message, avatar }) => {
  const styles = {
    marginRight: '15px'
  };
  return (
        <div className="chat-message-right">
          <div className="message" style={styles}>{message}</div>
          <div className="avatar-container">
            <img className="avatar" src={avatar} alt="Person B's Avatar" />
          </div>
        </div>
      );
};

export default ChatMessageRight;
