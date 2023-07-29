import * as React from 'react';

interface IRightSidebarProps {
}

const RightSidebar: React.FunctionComponent<IRightSidebarProps> = (props) => {
  return (
    <div className="right-sidebar">
      <div className='empty'>
      </div>
      <div className="title-container">
        <h3>Trainer Feedback</h3>
      </div>
      <div className="dynamic-rectangle">
        <p>
          Great job! Just a small correction: "Projektmanagement" should be written as one word.
          Keep up the good work! feedback: Good attempt! 
        </p>
        <p>
          However, the word "Guten" is missing at the beginning of the sentence.
           Remember to start with the correct greeting in German. Give it another try!
          Hint: What is the German word for "morning"?
        </p>
      </div>
    </div>
  );
};

export default RightSidebar;
