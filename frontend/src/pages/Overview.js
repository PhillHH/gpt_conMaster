import React from 'react';
import rocketImage from '../assets/rocket.png';
import ContentBox from '../components/ContentBox';
import InfoCard from '../components/InfoCard';

function Overview() {
  return (
    <ContentBox>
      <div className="overview">
        <h1>Overview 123</h1>
        <p>This will be a huge project soon. Make things happen with Growento </p>
        <img src={rocketImage} alt="Rocket" className="rocket" />
        <div className="info-cards">
          <InfoCard
            title="Expert Advice and Support"
            text="Our dedicated team is here to help you every step of the way, with expert guidance and tailored advice."
            image="path/to/your/expert-image.jpg"
            alt="Expert Support"
            linkText="Learn More"
            linkHref="#"
          />
          <InfoCard
            title="Quick Approval Process"
            text="Get pre-approved for your business loan in as little as 24 hours."
            image="path/to/your/approval-image.jpg"
            alt="Quick Approval"
            linkText="Learn More"
            linkHref="#"
          />
          <InfoCard
            title="Flexible Repayment Options"
            text="Choose a repayment plan that fits your budget, with flexible and affordable options to choose from."
            image="path/to/your/repayment-image.jpg"
            alt="Flexible Repayment"
            linkText="Learn More"
            linkHref="#"
          />
        </div>

        {/* letzten Aktivitäte  */}
      </div>
    </ContentBox>
  );
}

export default Overview;