import * as React from 'react';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Header from './Header'
import LeftSibar from './LeftSidebar'
import RightSidebar from './RightSidebar'
import Content from './Content';

interface IMainContentProps {
}

const MainContent: React.FunctionComponent<IMainContentProps> = (props) => {
  return (
    <Container fluid>
      <Row noGutters>
        <Col md={2} className='left-sidebar d-flex flex-column'>
          <LeftSibar />
        </Col>
        <Col md={8} className='main-content d-flex flex-column p-0'>
          <Header/>
          <Content/>
        </Col>
        <Col md={2} className='right-sidebar'>
          <RightSidebar />
        </Col>
      </Row>
    </Container>
  );
};

export default MainContent;
