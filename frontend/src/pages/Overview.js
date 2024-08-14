import React from 'react';
import rocketImage from '../assets/rocket.png';
import ContentBox from '../components/ContentBox';

function Overview() {
  return (
    <ContentBox>
      <div className="overview">
        <h1>Overview</h1>
        <p>This will be a huge project soon. Make things happen with Growento.com:</p>
        <img src={rocketImage} alt="Rocket" className="rocket" />

        {/* letzten Aktivitäte  */}
      </div>
    </ContentBox>
  );
}

export default Overview;